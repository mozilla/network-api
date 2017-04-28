from django.apps import AppConfig


class FeaturesConfig(AppConfig):
    name = 'networkapi.features'
    verbose_name = 'features'

    def ready(self):
        from networkapi.features.signals import setup_signals
        setup_signals()
