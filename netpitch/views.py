from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import Profile, PitchDeck, CollaborationRequest
from .forms import UserRegistrationForm, ProfileCreationForm, ProfileForm, PitchDeckForm, CollaborationRequestForm

# Single sign-up view that creates both user and profile
def signup(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileCreationForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            # Create the user
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # Create the profile and link it to the user
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # Log in the user after account creation
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome to NetPitch.')

            return redirect('profile_view')  # Redirect to profile after signup
        else:
            messages.error(request, 'There was an error in your sign-up form. Please correct the errors below.')
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileCreationForm()

    return render(request, 'netpitch/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

@login_required
def profile_view(request):
    profile = request.user.profile

    # Get the writer's pitch decks and their corresponding collaboration requests
    if profile.user_type == 'Writer':
        pitch_decks = PitchDeck.objects.filter(writer=profile.user)
        writer_collaboration_requests = CollaborationRequest.objects.filter(pitch__in=pitch_decks)
    else:
        pitch_decks = None
        writer_collaboration_requests = None

    # Get the producer's collaboration requests if they are a producer
    if profile.user_type == 'Producer':
        collaboration_requests = CollaborationRequest.objects.filter(producer=profile)
    else:
        collaboration_requests = None

    return render(request, 'netpitch/profile.html', {
        'profile': profile,
        'pitch_decks': pitch_decks,
        'writer_collaboration_requests': writer_collaboration_requests,
        'collaboration_requests': collaboration_requests,
        'is_profile_page': True,  # Pass this to the template
    })

# Update Profile View
@login_required
def update_profile(request):
    profile = request.user.profile  # Get the logged-in user's profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)  # Bind form with submitted data
        if form.is_valid():
            form.save()  # Save the updated profile
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile_view')  # Redirect to the profile view after successful update
        else:
            messages.error(request, 'There was an error updating your profile. Please try again.')
    else:
        messages.warning(request, 'Are you sure you want to update your profile?')
        form = ProfileForm(instance=profile)  # Pre-fill form with user's current profile data

    return render(request, 'netpitch/update_profile.html', {'form': form})

# Simple welcome page view
def welcome_page(request):
    all_pitch_decks = None
    
    # If user is logged in, fetch all pitch decks
    if request.user.is_authenticated:
        all_pitch_decks = PitchDeck.objects.all()

    return render(request, 'netpitch/welcome_page.html', {'all_pitch_decks': all_pitch_decks})

# User profile page redirect
@login_required
def user_page(request):
    return redirect('profile')  # Reuse profile_view for simplicity

# PitchDeck Submission
@login_required
def submit_pitch_deck(request):
    if request.method == 'POST':
        form = PitchDeckForm(request.POST, request.FILES)
        if form.is_valid():
            pitch_deck = form.save(commit=False)
            pitch_deck.writer = request.user  # Link to the writer's profile
            pitch_deck.save()
            messages.success(request, 'Pitch deck submitted successfully!')
            return redirect('pitch_deck_detail', pk=pitch_deck.pk)  # Redirect to details page
        else:
            messages.error(request, 'There was an error submitting the pitch deck. Please correct the errors below.')
    else:
        form = PitchDeckForm()
    
    return render(request, 'netpitch/submit_pitch_deck.html', {'form': form})

# Edit Pitch Deck View
@login_required
def edit_pitch_deck(request, pk):
    pitch_deck = get_object_or_404(PitchDeck, pk=pk, writer=request.user)

    if request.method == 'POST':
        form = PitchDeckForm(request.POST, request.FILES, instance=pitch_deck)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pitch deck updated successfully!')
            return redirect('profile_view')
        else:
            messages.error(request, 'There was an error updating the pitch deck. Please try again.')
    else:
        messages.warning(request, 'Are you sure you want to update this pitch deck?')
        form = PitchDeckForm(instance=pitch_deck)

    return render(request, 'netpitch/edit_pitch_deck.html', {'form': form, 'pitch_deck': pitch_deck})

# Delete Pitch Deck View
@login_required
def delete_pitch_deck(request, pk):
    pitch_deck = get_object_or_404(PitchDeck, pk=pk, writer=request.user)

    if request.method == 'POST':
        pitch_deck.delete()
        messages.success(request, 'Pitch deck deleted successfully.')
        return redirect('profile_view')  # Redirect to profile after deletion
    else:
        messages.warning(request, 'Are you sure you want to delete this pitch deck?')

    return render(request, 'netpitch/pitch_deck_detail.html', {'pitch_deck': pitch_deck})

# PitchDeck View
@login_required
def pitch_deck_detail(request, pk):
    pitch_deck = get_object_or_404(PitchDeck, pk=pk)
    return render(request, 'netpitch/pitch_deck_detail.html', {'pitch_deck': pitch_deck})

# Collaboration request View
@login_required
def submit_collaboration_request(request, pk):
    pitch_deck = get_object_or_404(PitchDeck, pk=pk)
    profile = request.user.profile

    # Ensure only producers can submit collaboration requests
    if profile.user_type != 'Producer':
        messages.error(request, 'You must be a Producer to submit a collaboration request.')
        return redirect('home')  # Redirect to home if the user is not a producer

    if request.method == 'POST':
        form = CollaborationRequestForm(request.POST)
        if form.is_valid():
            collaboration_request = form.save(commit=False)
            collaboration_request.producer = profile
            collaboration_request.pitch = pitch_deck
            collaboration_request.save()

            messages.success(request, 'Your collaboration request has been submitted successfully!')
            return redirect('pitch_deck_detail', pk=pitch_deck.pk)  # Redirect back to the pitch deck detail page
        else:
            messages.error(request, 'There was an error submitting your collaboration request.')
    else:
        form = CollaborationRequestForm()

    return render(request, 'netpitch/submit_collaboration_request.html', {
        'form': form,
        'pitch_deck': pitch_deck,
    })

# View to accept a collaboration request
@login_required
def accept_collaboration_request(request, request_id):
    collaboration_request = get_object_or_404(CollaborationRequest, id=request_id)
    
    # Ensure only the writer can accept the request
    if request.user.profile == collaboration_request.pitch.writer.profile:
        collaboration_request.status = 'Accepted'
        collaboration_request.save()
        messages.success(request, 'Collaboration request accepted.')
    else:
        messages.error(request, 'You do not have permission to accept this request.')

    return redirect('profile_view')

# View to decline a collaboration request
@login_required
def decline_collaboration_request(request, request_id):
    collaboration_request = get_object_or_404(CollaborationRequest, id=request_id)

    # Ensure only the writer can decline the request
    if request.user.profile == collaboration_request.pitch.writer.profile:
        collaboration_request.status = 'Declined'
        collaboration_request.save()
        messages.success(request, 'Collaboration request declined.')
    else:
        messages.error(request, 'You do not have permission to decline this request.')

    return redirect('profile_view')

# View to clear a collaboration request from the profile view
@login_required
def clear_collaboration_request(request, request_id):
    collaboration_request = get_object_or_404(CollaborationRequest, id=request_id)

    # Allow both writers and producers to clear the request
    if (request.user.profile == collaboration_request.pitch.writer.profile or
        request.user.profile == collaboration_request.producer):
        collaboration_request.delete()
        messages.success(request, 'Collaboration request cleared.')
    else:
        messages.error(request, 'You do not have permission to clear this request.')

    return redirect('profile_view')