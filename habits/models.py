from datetime import timedelta

from django.db import models
from django.db.models.functions import datetime

from config import settings

NULLABLE = {"null": True, "blank": True}

class Habit(models.Model):
    # def get_default_date(self):
    #     return datetime.date.now() + timedelta(days=1)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="пользователь")
    place = models.CharField(max_length=150, verbose_name="место выполнения привычки")
    time = models.TimeField(default="12:00:00", max_length=170, verbose_name="время исполнения привычки")
    action = models.TextField(verbose_name="привычка - конкретное действие")
    sign_of_pleasant_habit = models.BooleanField(default=False, verbose_name="признак приятной привычки")
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name="связанная привычка", **NULLABLE)
    periodicity = models.PositiveIntegerField(default=1, verbose_name='периодичность(дни)')
    reward = models.CharField(max_length=150, verbose_name="вознаграждение", **NULLABLE)
    time_to_complete = models.DurationField(verbose_name="время на выполнение", **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='признак публикации')

    # def save(self, *args, **kwargs):
    #     if not self.date_validity:
    #         self.date_validity = datetime.date.today() + timedelta(days=1)
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f'я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

