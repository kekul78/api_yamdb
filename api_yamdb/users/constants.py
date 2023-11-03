# constants.py

"""Модуль для констант."""

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'

CHOICES = (
    (USER, 'Пользователь'),
    (MODERATOR, 'Модератор'),
    (ADMIN, 'Админ')
)
MAX_LENGTH_ROLE = max(len(ROLE[0]) for ROLE in CHOICES)
MAX_LENGTH_ELSE = 150
MAX_LENGTH = 150
