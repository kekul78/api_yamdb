from django.db import models
from django.contrib.auth.models import AbstractUser
from users.validators import validate_forbidden_username
import users.constants as const


class UserModel(AbstractUser):
    bio = models.TextField('Биография', blank=True)
    role = models.CharField(max_length=const.MAX_LENGTH_ROLE, choices=const.CHOICES,
                            default=const.USER, blank=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=const.MAX_LENGTH_ELSE, unique=True,
                                validators=[validate_forbidden_username])

    class Meta:
        verbose_name = 'Участники'
        verbose_name_plural = 'Участники'
        ordering = ('username',)

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == 'moderator'
