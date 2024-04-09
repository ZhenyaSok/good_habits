from rest_framework import serializers
from habits.models import Habit
from habits.validators import valid_one_field_out_of_two, time_performance, pleasant_in_related, limit_of_periodicity, \
    only_pleasant_in_related


class AdvisableHabitSerializer(serializers.ModelSerializer):
    """Приятная привычка"""

    class Meta:
        model = Habit
        fields = ('id', 'owner', 'place', 'time', 'action', 'periodicity', 'time_to_complete',
                  'is_published', 'sign_of_pleasant_habit')

class HabitSerializer(serializers.ModelSerializer):
    """Привычка"""

    class Meta:
        model = Habit
        fields = '__all__'


class HabitCreateSerializer(serializers.ModelSerializer):
    """Создание привычки"""

    class Meta:
        model = Habit
        fields = ('id', 'owner', 'place', 'time', 'action', 'sign_of_pleasant_habit', 'related_habit',
                  'periodicity', 'reward', 'time_to_complete', 'is_published')

        """Валидация для сериализатора"""
        validators = [
            valid_one_field_out_of_two,
            time_performance,
            pleasant_in_related,
            limit_of_periodicity,
            only_pleasant_in_related,
        ]


