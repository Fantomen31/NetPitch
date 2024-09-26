from django.contrib import admin
from .models import Genre, Profile, PitchDeck, CollaborationRequest

# Register the Genre model
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register the Profile model
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'bio',)
    search_fields = ('user__username', 'bio')
    list_filter = ('user_type',)

# Register the PitchDeck model
@admin.register(PitchDeck)
class PitchDeckAdmin(admin.ModelAdmin):
    list_display = ('title', 'pitch_type', 'writer', 'genre', 'theme')
    search_fields = ('title', 'writer__username', 'theme')
    list_filter = ('pitch_type', 'genre')

# Register the CollaborationRequest model
@admin.register(CollaborationRequest)
class CollaborationRequestAdmin(admin.ModelAdmin):
    list_display = ('pitch', 'producer', 'message')
    search_fields = ('pitch__title', 'producer__user__username')