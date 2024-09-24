from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('Writer', 'Writer'),
        ('Producer', 'Producer'),
    ]

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = Profile.objects.create(user=user, user_type=self.cleaned_data['user_type'])
            profile.save()
        return user

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_image', 'user_type']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_image']