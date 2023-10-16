from django.apps import AppConfig


class LogCuttingSawnLogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'logcutting_sawnlog'

    def ready(self):
        import logcutting_sawnlog.signals  # Import the signals module
