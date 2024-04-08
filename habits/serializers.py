from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('id', 'owner', 'place', 'time', 'action', 'sign_of_pleasant_habit', 'periodicity', 'reward',
                  'time_to_complete', 'is_published')
