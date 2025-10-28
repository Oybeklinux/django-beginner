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
    
    path("skill_add/", skill_add, name="skill_add"),
    path("skill_edit/<str:id>", skill_edit, name="skill_edit"),
    path("skill_delete/<str:id>", skill_delete, name="skill_delete")
]