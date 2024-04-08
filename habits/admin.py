from django.contrib import admin
from habits.models import Habit


@admin.register(Habit)
class HabitListSettingsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'place', 'time', 'action', 'sign_of_pleasant_habit', 'related_habit',
                    'periodicity', 'reward', 'time_to_complete', 'is_published')
    search_fields = ('pk',)


