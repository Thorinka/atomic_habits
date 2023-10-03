from rest_framework import serializers

from habits.models import Habit, PleasantHabit
from habits.validators import EstimatedTimeValidator, PeriodicityValidator


class HabitSerializer(serializers.ModelSerializer):
    periodicity = serializers.IntegerField(default=1)

    class Meta:
        model = Habit
        fields = ('id', 'user', 'place', 'time', 'action', 'connected_habit', 'periodicity', 'reward', 'estimated_time',
                  'is_public')
        validators = [EstimatedTimeValidator(field='estimated_time'),
                      PeriodicityValidator(field='periodicity')]


class PleasantHabitSerializer(serializers.ModelSerializer):
    periodicity = serializers.IntegerField(default=1)

    class Meta:
        model = PleasantHabit
        fields = ('id', 'user', 'place', 'time', 'action', 'periodicity', 'estimated_time', 'is_public')
        validators = [EstimatedTimeValidator(field='estimated_time'),
                      PeriodicityValidator(field='periodicity')]
