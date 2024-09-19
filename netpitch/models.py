from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('Writer', 'Writer'),
        ('producer', 'Producer'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.user.username