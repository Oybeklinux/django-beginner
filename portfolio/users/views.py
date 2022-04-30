from django.shortcuts import redirect, render
from .models import Profil
from django.contrib.auth import authenticate, login
# Create your views here.

def profiles(request):
    users = Profil.objects.all()
    context = {
        "users": users
    }
    return render(request, 'users/profiles.html', context)

def profile(request, id):
    user = Profil.objects.get(id=id)
    context = {
        "user": user
    }
    return render(request, 'users/profile.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')
        
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            print('Bunday login va parol mavjud emas')


    return render(request, "users/login.html")