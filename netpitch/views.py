from django.http import HttpResponse 
from .forms import ProfileForm
from django.shortcuts import render

# Create your views here.

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': form})

def my_netpitch(request):
    return HttpResponse("Hello NetPitch!")