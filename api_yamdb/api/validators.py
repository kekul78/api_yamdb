from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_year(value):
    """
    Проверка валидности года.
    """
    if value > timezone.now().year:
        raise ValidationError(
            ('Год %(value)s больше текущего!'),
            params={'value': value},
        )
