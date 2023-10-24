from django.db import models
from django.contrib.auth.models import AbstractUser

#User = get_user_model()

CHOICES = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Админ')
)


class UserModel(AbstractUser):
    bio = models.TextField('Биография', blank=True)
    role = models.CharField(max_length=16, choices=CHOICES,
                            default='Пользователь', blank=True)
    email = models.EmailField(unique=True)
