from django.contrib.auth.models import AbstractUser
from django.db import models

from habits.models import NULLABLE


class UserRoles(models.TextChoices):
    MEMBER = 'member', 'Пользователь'
    MODERATOR = 'moderator', 'Модератор'


class User(AbstractUser):
    username = None

    telegram = models.CharField(max_length=35, unique=True, verbose_name='телеграм')
    chat_id = models.PositiveBigIntegerField(default=0, verbose_name='номер чата', **NULLABLE)
    update_id = models.PositiveBigIntegerField(default=0, verbose_name='номер последнего сообщения', **NULLABLE)

    role = models.CharField(max_length=9, choices=UserRoles.choices, default='member')

    USERNAME_FIELD = "telegram"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
