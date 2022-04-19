from django.shortcuts import render
from .models import Profil
# Create your views here.

def profiles(request):
    users = Profil.objects.all()
    context = {
        "users": users
    }
    return render(request, 'users/profiles.html', context)