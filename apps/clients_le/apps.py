from django.apps import AppConfig

class ClientsLeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.clients_le'
    verbose_name = 'LE Clients'

    def ready(self):
        from .registration import register_le_clients_models
        register_le_clients_models()
