from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_netpitch, name='netpitch'),
    path('profile/', views.profile_view, name='profile'),
]