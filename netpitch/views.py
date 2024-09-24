from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Profile, PitchDeck, CollaborationRequest
from .forms import UserRegistrationForm, ProfileCreationForm, ProfileForm

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

            return redirect('profile_view')  # Redirect to profile after signup
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileCreationForm()

    return render(request, 'netpitch/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

# Universal profile view for both Writer and Producer
@login_required
def profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect back to profile after successful update
    else:
        form = ProfileForm(instance=profile)  # Pre-fill form with user's profile info

    pitch_decks = PitchDeck.objects.filter(writer=profile) if profile.user_type == 'Writer' else None
    collaboration_requests = CollaborationRequest.objects.filter(producer=profile) if profile.user_type == 'Producer' else None

    return render(request, 'netpitch/profile.html', {
        'profile': profile,
        'form': form,
        'pitch_decks': pitch_decks,
        'collaboration_requests': collaboration_requests,
    })

# Simple welcome page view
def welcome_page(request):
    return render(request, 'netpitch/welcome_page.html')

# User profile page redirect
@login_required
def user_page(request):
    return redirect('profile_view')  # Reuse profile_view for simplicity