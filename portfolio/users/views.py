from django.shortcuts import render
from .models import Profil
# Create your views here.

def profiles(request):
    users = Profil.objects.all()
    context = {
        "users": users
    }
<<<<<<< HEAD
    return render(request, 'users/profiles.html', context)

def profile(request, id):
    user = Profil.objects.get(id=id)
    context = {
        "user": user
    }
    return render(request, 'users/profile.html', context)
=======
    return render(request, 'users/profiles.html', context)
>>>>>>> 5391a44d5ef19d4c88411fff1be6d3426b2ba557
