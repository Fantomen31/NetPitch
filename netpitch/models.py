from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('Writer', 'Writer'),
        ('Producer', 'Producer'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.user.username

class PitchDeck(models.Model):
    PITCH_TYPE_CHOICES = [
        ('Film', 'Film'),
        ('TV Show', 'TV Show'),
    ]

    title = models.CharField(max_length=255)
    synopsis = models.TextField()
    genre = models.ForeignKey('netpitch.Genre', on_delete=models.SET_NULL, null=True)  # String reference for Genre
    pitch_type = models.CharField(max_length=10, choices=PITCH_TYPE_CHOICES)
    writer = models.ForeignKey('netpitch.Profile', on_delete=models.CASCADE)  # String reference for Profile

    def __str__(self):
        return self.title

class CollaborationRequest(models.Model):
    pitch = models.ForeignKey('netpitch.PitchDeck', on_delete=models.CASCADE)  # Use string reference for PitchDeck
    producer = models.ForeignKey('netpitch.Profile', on_delete=models.CASCADE)  # Use string reference for Profile
    message = models.TextField()

    def __str__(self):
        return f"Collaboration request for {self.pitch.title} by {self.producer.user.username}"