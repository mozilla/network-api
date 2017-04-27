from django.apps import AppConfig

from networkapi.news.signals import setup_signals


class NewsConfig(AppConfig):
    name = 'networkapi.news'
    verbose_name = 'news'

    def ready(self):
        setup_signals()
