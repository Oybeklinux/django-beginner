from django.db.models.signals import post_save, post_delete
from django.dispatch import Signal, receiver
from django.contrib.auth.models import User
from .models import Profil

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        Profil.objects.create(
            user=user
        )
    else:
        try:
            profile = Profil.objects.get(user=user)
            profile.email = user.email
            profile.name = f"{user.first_name} {user.last_name}"
            profile.save()
        except:
            pass


@receiver(post_delete, sender=Profil)
def delete_user(sender, instance, **kwargs):
    profile = instance
    user = profile.user
    user.delete()