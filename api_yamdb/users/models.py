from django.db import models
from django.contrib.auth.models import AbstractUser
from users.validators import validate_forbidden_username

USER = 'user'

CHOICES = (
    (USER, 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Админ')
)
MAX_LENGTH_ROLE = max(len(ROLE[0]) for ROLE in CHOICES)
MAX_LENGTH_ELSE = 150


class UserModel(AbstractUser):
    bio = models.TextField('Биография', blank=True)
    role = models.CharField(max_length=MAX_LENGTH_ROLE, choices=CHOICES,
                            default=USER, blank=True)
    email = models.EmailField(unique=True)
 #   confirmation_code = models.CharField(max_length=MAX_LENGTH_ELSE,
 #                                        blank=True)
    username = models.CharField(max_length=MAX_LENGTH_ELSE, unique=True,
                                validators=[validate_forbidden_username])

    class Meta:
        verbose_name = 'Участники'
        verbose_name_plural = 'Участники'
        ordering = ['username']

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == 'moderator'
