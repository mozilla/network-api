from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    name = 'pulseapi.userprofile'
    verbose_name = 'user profiles'

    def ready(self):
        from pulseapi.userprofile import signals

        if signals is None:
            print("Error loading signal monitoring")
