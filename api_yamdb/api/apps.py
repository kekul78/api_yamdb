from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Обозначение класса с именем приложения - api,
    в котором идет работа с api для Yamdb"""
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'api'
    verbose_name: str = 'Программный интерфейс приложения'
