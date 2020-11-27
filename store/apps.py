from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class StoreConfig(AppConfig):
    name = 'store'

    def ready(self):
        import store.signals