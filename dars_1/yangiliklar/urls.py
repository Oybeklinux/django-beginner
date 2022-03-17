from django.urls import path
from .views import *

# 127.0.0.1:8000/
urlpatterns = [
    path("news/", yangiliklar),
    path("about/", about),
    path("news/edit/", ozgartirish),
    path("news/<int:id>", yangilik)
]