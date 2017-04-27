from django.apps import AppConfig

from networkapi.features.signals import setup_signals


class FeaturesConfig(AppConfig):
    name = 'networkapi.features'
    verbose_name = 'features'

    def ready(self):
        setup_signals()