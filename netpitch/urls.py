from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_page, name='home'),
    path('signup/', views.signup, name='signup'),
    path('create-profile/', views.create_profile, name='create_profile'),
    path('profile/', views.profile_view, name='profile'),
]