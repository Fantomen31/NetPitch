from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
from .forms import UserRegistrationForm
from .forms import ProfileCreationForm

# Create your views here.



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
            login(request, user)

            return redirect('netpitch/profile.html')  # Redirect to profile page after creating the profile
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileCreationForm()

    return render(request, 'netpitch/create-profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'netpitch/profile.html', {'form': form})

