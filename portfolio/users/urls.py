from django.urls import path
from .views import *

# 127.0.0.1:8000/
urlpatterns = [
    path("", profiles, name="profiles"),
    path("login/", login_user, name="login"),
    path("register/", register_user, name="register"),
    path("logout/", logout_user, name="logout"),
    path("account/", account, name="account"),
    path("account_edit/", account_edit, name="account_edit"),
    path("profiles/<str:id>", profile, name="profile"),
]