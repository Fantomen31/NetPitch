from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Profile, PitchDeck, CollaborationRequest, Genre
from .forms import CustomUserCreationForm, ProfileCreationForm, UserRegistrationForm, ProfileForm

# Views here.
@login_required
def writer_profile_view(request):
    profile = request.user.profile
    if profile.user_type == 'Writer':
        pitch_decks = PitchDeck.objects.filter(writer=profile)  # Get pitch decks by the writer
        return render(request, 'netpitch/writer_profile.html', {
            'profile': profile,
            'pitch_decks': pitch_decks
        })
    else:
        return redirect('home')  # Redirect if not a writer

@login_required
def producer_profile_view(request):
    profile = request.user.profile
    if profile.user_type == 'Producer':
        # Fetch the collaboration requests made by this producer
        collaboration_requests = CollaborationRequest.objects.filter(producer=profile)
        return render(request, 'netpitch/producer_profile.html', {
            'profile': profile,
            'collaboration_requests': collaboration_requests
        })
    else:
        return redirect('home')  # Redirect if not a producer


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

            return redirect('profile')  # Redirect to profile page after creating the profile
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileCreationForm()

    return render(request, 'netpitch/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

def welcome_page(request):
    #Renders the welcome page where users can choose to log in or sign up.
    return render(request, 'netpitch/welcome_page.html')


def create_profile(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileCreationForm(request.POST, request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            # Create the user
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # Create the profile
            profile = profile_form.save(commit=False)
            profile.user = user  # Link the profile to the user
            profile.save()

            # Log in the user after account creation
            login(request, user)  # Use the login function to log in the user

            return redirect('profile')  # Redirect to profile page after creating the profile
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileCreationForm()

    return render(request, 'netpitch/create_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


@login_required
def profile_view(request):
    profile = request.user.profile

    # Redirect based on user type
    if profile.user_type == 'Writer':
        return redirect('writer_profile')
    elif profile.user_type == 'Producer':
        return redirect('producer_profile')
    else:
        # Handle the case where the user type doesn't match expected values
        return HttpResponse("Invalid profile type")


@login_required
def user_page(request):
    # Get the user's profile
    profile = request.user.profile
    
    if profile.user_type == 'Writer':
        # Get pitch decks submitted by the writer
        pitch_decks = PitchDeck.objects.filter(writer=profile)
        
        # Render the writer-specific template
        return render(request, 'netpitch/writer_page.html', {
            'profile': profile,
            'pitch_decks': pitch_decks
        })
    
    elif profile.user_type == 'Producer':
        # Get collaboration requests made by the producer
        collaborations = CollaborationRequest.objects.filter(producer=profile)
        
        # Render the producer-specific template
        return render(request, 'netpitch/producer_page.html', {
            'profile': profile,
            'collaborations': collaborations
        })

    # Add a fallback option if needed
    return render(request, 'netpitch/profile.html', {'profile': profile})