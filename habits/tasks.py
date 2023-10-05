import datetime

from celery import shared_task

from habits.models import Habit, PleasantHabit
from habits.telegram import send_message


@shared_task
def send_notification():
    now_hour = datetime.datetime.now().hour
    now_minute = datetime.datetime.now().minute

    habits = Habit.objects.filter(
        time__hour=now_hour,
        time__minute=now_minute
    )
    pleasant_habits = PleasantHabit.objects.filter(
        time__hour=now_hour,
        time__minute=now_minute
    )

    for h in habits:
        action = h.action
        place = h.place
        time = h.time
        username = h.user.telegram
        send_message(
            username,
            f'Вам нужно сделать {action} в {place} в {time}'
        )

    for h in pleasant_habits:
        action = h.action
        place = h.place
        time = h.time
        username = h.user.telegram
        send_message(
            username,
            f'Вам нужно сделать {action} в {place} в {time}'
        )
