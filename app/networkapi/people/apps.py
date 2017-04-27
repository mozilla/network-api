from django.apps import AppConfig

from networkapi.people.signals import setup_signals


class PeopleConfig(AppConfig):
    name = 'networkapi.people'
    verbose_name = 'people'

    def ready(self):
        setup_signals()
