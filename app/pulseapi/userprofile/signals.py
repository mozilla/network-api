from .models import UserProfile
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in


@receiver(user_logged_in, dispatch_uid="unique")
def set_user_profile(request, user, **kwargs):
    """
    This is a general signal handler for the "user logged in"
    signal, which makes sure that the logged in user has an
    associated pulse-specific user profile.
    """

    found = UserProfile.objects.filter(user=user)
    has_profile = len(found) == 1

    if has_profile is False:
        profile = UserProfile.objects.create(user=user)
        profile.save()
