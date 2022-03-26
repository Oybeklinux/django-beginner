from django.urls import path
from .views import *

# 127.0.0.1:8000/
urlpatterns = [
    path("projects/", projects, name="projects"),
    path("projects/<uuid:id>", project,  name="project"),
]