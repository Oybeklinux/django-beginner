from django.urls import path
from .views import *

# 127.0.0.1:8000/
urlpatterns = [
    path("", profiles, name="profiles"),
<<<<<<< HEAD
    path("profiles/<str:id>", profile, name="profile"),
=======
>>>>>>> 5391a44d5ef19d4c88411fff1be6d3426b2ba557
]