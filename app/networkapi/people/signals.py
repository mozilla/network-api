from django.db.models.signals import post_save
from django.dispatch import receiver

from networkapi.utility.build import build_static_site
from networkapi.people.models import Person


@receiver(post_save, sender=Person)
def post_save_callback(sender, instance, **kwargs):
    build_static_site(sender, instance, **kwargs)
