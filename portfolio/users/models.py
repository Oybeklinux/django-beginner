import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import Signal

# Create your models here.
class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    info = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    social_github = models.CharField(max_length=200, null=True, blank=True)
    social_facebook = models.CharField(max_length=200, null=True, blank=True)
    social_youtube = models.CharField(max_length=200, null=True, blank=True)
    social_instagram = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="profiles", default="profiles/default_profile.webp")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  

    def __str__(self) -> str:
        return str(self.user.username)


class Skill(models.Model):
    user = models.ForeignKey(Profil, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
 
    def __str__(self) -> str:
        return str(self.name)

def create_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        Profil.objects.create(
            user=user
        )
    else:
        profile = Profil.objects.get(user=user)
        profile.email = user.email
        profile.name = f"{user.first_name} {user.last_name}"
        profile.save()

def delete_user(sender, instance, **kwargs):
    profile = instance
    user = profile.user
    user.delete()

Signal.connect(post_save, create_profile, sender=User)
Signal.connect(post_delete, delete_user, sender=Profil)