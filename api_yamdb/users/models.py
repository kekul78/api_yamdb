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
                            default='user', blank=True)
    email = models.EmailField(unique=True)
    confirmation_code = models.CharField(max_length=128, blank=True)

    def save(self, *args, **kwargs):
        print(self.is_superuser)
        if self.is_superuser:
            self.role = 'admin'
        super().save()
