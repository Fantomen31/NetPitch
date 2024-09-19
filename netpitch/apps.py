from django.apps import AppConfig

#class ProfileForm(forms.ModelForm):
    #class Meta:
       # model = Profile
       # fields = ['bio', 'profile_image', 'user_type']

class NetpitchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'netpitch'
