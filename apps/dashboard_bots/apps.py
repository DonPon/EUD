from django.apps import AppConfig

class DashboardBotsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.dashboard_bots'
    verbose_name = 'Dashboard'

    def ready(self):
        from .registration import register_dashboard_models
        register_dashboard_models()
