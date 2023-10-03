from django.conf import settings
from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class PleasantHabit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='создатель привычки',
                             **NULLABLE)
    place = models.CharField(max_length=25, verbose_name='место для привычки')
    time = models.TimeField(verbose_name='когда нужно выполнить привычку')
    action = models.CharField(max_length=150, verbose_name='действие')
    is_pleasant = models.BooleanField(default=True, verbose_name='приятная привычка')
    periodicity = models.SmallIntegerField(default=1, verbose_name='периодичность')
    estimated_time = models.SmallIntegerField(verbose_name='время на выполнение')
    is_public = models.BooleanField(default=True, verbose_name='публичная привычка')


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='создатель привычки',
                             **NULLABLE)
    place = models.CharField(max_length=25, verbose_name='место для привычки')
    time = models.TimeField(verbose_name='когда нужно выполнить привычку')
    action = models.CharField(max_length=150, verbose_name='действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='приятная привычка')
    connected_habit = models.ForeignKey(PleasantHabit, on_delete=models.SET_NULL, verbose_name='связанная привычка',
                                        **NULLABLE)
    periodicity = models.SmallIntegerField(default=1, verbose_name='периодичность')
    reward = models.CharField(max_length=150, verbose_name='награда', **NULLABLE)
    estimated_time = models.SmallIntegerField(verbose_name='время на выполнение')
    is_public = models.BooleanField(default=True, verbose_name='публичная привычка')
