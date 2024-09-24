from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.welcome_page, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('create-profile/', views.create_profile, name='create_profile'),
    path('writer-profile/', views.writer_profile_view, name='writer_profile'),
    path('producer-profile/', views.producer_profile_view, name='producer_profile'),
    path('profile/', views.profile_view, name='profile'),
]