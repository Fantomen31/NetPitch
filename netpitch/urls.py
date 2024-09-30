from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.welcome_page, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', views.profile_view, name='profile_view'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('submit-pitch-deck/', views.submit_pitch_deck, name='submit_pitch_deck'),
    path('pitch-deck/<int:pk>/', views.pitch_deck_detail, name='pitch_deck_detail'),  # Detail view
]