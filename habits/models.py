from datetime import timedelta

from django.db import models
from django.db.models.functions import datetime

from config import settings

NULLABLE = {"null": True, "blank": True}
"""
Описание задач
Добавьте необходимые модели привычек.
Реализуйте эндпоинты для работы с фронтендом.
Создайте приложение для работы с Telegram и рассылками напоминаний.
Модели
В книге хороший пример привычки описывается как конкретное действие, которое можно уложить в одно предложение:

Чем отличается полезная привычка от приятной и связанной?
Полезная привычка — это само действие, которое пользователь будет совершать и получать за его выполнение определенное вознаграждение (приятная привычка или любое другое вознаграждение).

Приятная привычка — это способ вознаградить себя за выполнение полезной привычки. Приятная привычка указывается в качестве связанной для полезной привычки (в поле «Связанная привычка»).

Например: в качестве полезной привычки вы будете выходить на прогулку вокруг квартала сразу же после ужина. Вашим вознаграждением за это будет приятная привычка — принять ванну с пеной. То есть такая полезная привычка будет иметь связанную привычку.

Рассмотрим другой пример: полезная привычка — «я буду не опаздывать на еженедельную встречу с друзьями в ресторан». В качестве вознаграждения вы заказываете себе десерт. В таком случае полезная привычка имеет вознаграждение, но не приятную привычку.

Признак приятной привычки — булево поле, которые указывает на то, что привычка является приятной, а не полезной."""
class Habit(models.Model):
    # def get_default_date(self):
    #     return datetime.date.now() + timedelta(days=1)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="пользователь")
    place = models.CharField(max_length=350, verbose_name="место выполнения привычки")
    time = models.TimeField(verbose_name="время исполнения привычки")
    action = models.TextField(verbose_name="привычка - конкретное действие")
    sign_of_pleasant_habit = models.BooleanField(default=True, verbose_name="признак полезной привычки")
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name="связанная привычка", **NULLABLE)
    # periodicity = models.DateField(default=datetime.datetime.today()+timedelta(days=1), verbose_name="периодичность")
    # date_validity = models.DateField(default=get_default_date)
    periodicity = models.DecimalField(default=1, min=1, max=7, verbose_name='периодичность(в днях)')
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

