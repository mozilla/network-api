from django.db.models.signals import post_save

from networkapi.utility.build import build_static_site
from networkapi.news.models import News

post_save.connect(build_static_site, sender=News)
