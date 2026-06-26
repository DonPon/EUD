from django.apps import AppConfig

class RepaperingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.repapering'

    def ready(self):
        from apps.repapering.registration import register_repapering_models
        register_repapering_models()

