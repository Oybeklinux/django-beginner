from django.urls import path
from .views import *

# 127.0.0.1:8000/
urlpatterns = [
    path("", profiles, name="profiles"),
    path("profiles/<str:id>", profile, name="profile"),
]