from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import PitchDeck, CollaborationRequest
from .forms import (
    UserRegistrationForm, ProfileCreationForm,
    ProfileForm, PitchDeckForm, CollaborationRequestForm
)


# Single sign-up view that creates both user and profile
def signup(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileCreationForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)

            messages.success(request, "Signup successful!")
            return redirect('profile_view')
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileCreationForm()

    return render(
        request, 'netpitch/signup.html', {
            'user_form': user_form,
            'profile_form': profile_form,
        }
    )


@login_required
def profile_view(request):
    profile = request.user.profile

    if profile.user_type == 'Writer':
        pitch_decks = PitchDeck.objects.filter(writer=profile.user)
        writer_collaboration_requests = CollaborationRequest.objects.filter(
            pitch__in=pitch_decks
        )
    else:
        pitch_decks = None
        writer_collaboration_requests = None

    if profile.user_type == 'Producer':
        collaboration_requests = CollaborationRequest.objects.filter(
            producer=profile
        )
    else:
        collaboration_requests = None

    return render(
        request, 'netpitch/profile.html', {
            'profile': profile,
            'pitch_decks': pitch_decks,
            'writer_collaboration_requests': writer_collaboration_requests,
            'collaboration_requests': collaboration_requests,
            'is_profile_page': True,
        }
    )


@login_required
def update_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(
            request.POST, request.FILES, instance=profile
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)

    return render(
        request, 'netpitch/update_profile.html', {'form': form}
    )


def welcome_page(request):
    all_pitch_decks = None
    if request.user.is_authenticated:
        all_pitch_decks = PitchDeck.objects.all()

    return render(
        request, 'netpitch/welcome_page.html', {
            'all_pitch_decks': all_pitch_decks
        }
    )


@login_required
def user_page(request):
    return redirect('profile_view')


@login_required
def submit_pitch_deck(request):
    if request.method == 'POST':
        form = PitchDeckForm(request.POST, request.FILES)
        if form.is_valid():
            pitch_deck = form.save(commit=False)
            pitch_deck.writer = request.user
            pitch_deck.save()

            messages.success(
                request, "Pitch deck submitted successfully!"
            )
            return redirect('pitch_deck_detail', pk=pitch_deck.pk)
    else:
        form = PitchDeckForm()

    return render(
        request, 'netpitch/submit_pitch_deck.html', {'form': form}
    )


@login_required
def edit_pitch_deck(request, pk):
    pitch_deck = get_object_or_404(PitchDeck, pk=pk, writer=request.user)

    if request.method == 'POST':
        form = PitchDeckForm(
            request.POST, request.FILES, instance=pitch_deck
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Pitch deck updated successfully!")
            return redirect('profile_view')
    else:
        form = PitchDeckForm(instance=pitch_deck)

    return render(
        request, 'netpitch/edit_pitch_deck.html', {
            'form': form, 'pitch_deck': pitch_deck
        }
    )


@login_required
def delete_pitch_deck(request, pk):
    pitch_deck = get_object_or_404(PitchDeck, pk=pk, writer=request.user)

    if request.method == 'POST':
        pitch_deck.delete()
        messages.success(request, "Pitch deck deleted successfully!")
        return redirect('profile_view')

    return render(
        request, 'netpitch/pitch_deck_detail.html', {
            'pitch_deck': pitch_deck
        }
    )


@login_required
def pitch_deck_detail(request, pk):
    pitch_deck = get_object_or_404(PitchDeck, pk=pk)
    return render(
        request, 'netpitch/pitch_deck_detail.html', {
            'pitch_deck': pitch_deck
        }
    )


@login_required
def submit_collaboration_request(request, pk):
    pitch_deck = get_object_or_404(PitchDeck, pk=pk)
    profile = request.user.profile

    if profile.user_type != 'Producer':
        return redirect('home')

    if request.method == 'POST':
        form = CollaborationRequestForm(request.POST)
        if form.is_valid():
            collaboration_request = form.save(commit=False)
            collaboration_request.producer = profile
            collaboration_request.pitch = pitch_deck
            collaboration_request.save()

            messages.success(
                request, "Collaboration request submitted successfully!"
            )
            return redirect('pitch_deck_detail', pk=pitch_deck.pk)
    else:
        form = CollaborationRequestForm()

    return render(
        request, 'netpitch/submit_collaboration_request.html', {
            'form': form, 'pitch_deck': pitch_deck
        }
    )


@login_required
def accept_collaboration_request(request, request_id):
    collaboration_request = get_object_or_404(
        CollaborationRequest, id=request_id
    )

    if request.user.profile == collaboration_request.pitch.writer.profile:
        collaboration_request.status = 'Accepted'
        collaboration_request.save()
        messages.success(request, "Collaboration request accepted.")
    else:
        messages.error(
            request, "You do not have permission to accept this request."
        )

    return redirect('profile_view')


@login_required
def decline_collaboration_request(request, request_id):
    collaboration_request = get_object_or_404(
        CollaborationRequest, id=request_id
    )

    if request.user.profile == collaboration_request.pitch.writer.profile:
        collaboration_request.status = 'Declined'
        collaboration_request.save()
        messages.success(request, "Collaboration request declined.")
    else:
        messages.error(
            request, "You do not have permission to decline this request."
        )

    return redirect('profile_view')


@login_required
def clear_collaboration_request(request, request_id):
    collaboration_request = get_object_or_404(
        CollaborationRequest, id=request_id
    )

    if (request.user.profile == collaboration_request.pitch.writer.profile or
            request.user.profile == collaboration_request.producer):
        collaboration_request.delete()
        messages.success(request, "Collaboration request cleared.")
    else:
        messages.error(
            request, "You do not have permission to clear this request."
        )

    return redirect('profile_view')
