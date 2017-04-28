from django.db.models.signals import post_save, post_delete

from networkapi.utility.build import build_static_site
from networkapi.features.models import Feature


def setup_signals():
    post_save.connect(build_static_site, sender=Feature)
    post_delete.connect(build_static_site, sender=Feature)
