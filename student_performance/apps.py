from django.apps import AppConfig


class StudentPerformanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student_performance'

    def ready(self):
        import student_performance.signals