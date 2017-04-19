from django.db.models.signals import post_save
from django.dispatch import receiver

from networkapi.utility.build import build_static_site
from networkapi.news.models import News


@receiver(post_save, sender=News)
def post_save_callback(sender, instance, **kwargs):
    build_static_site(sender, instance, **kwargs)
