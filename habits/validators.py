from datetime import timedelta

from rest_framework import serializers

from habits.models import Habit

"""
Валидаторы

???В связанные привычки могут попадать только привычки с признаком приятной привычки.
У приятной привычки не может быть вознаграждения или связанной привычки.
Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
Нельзя не выполнять привычку более 7 дней. Например, привычка 
может повторяться раз в неделю, но не раз в 2 недели. За одну неделю необходимо выполнить привычку хотя бы один раз."""
SCAM_URL = 'youtube.com'
def valid_one_field_out_of_two(val):
    if val["related_habit"] and val["reward"]:
        raise serializers.ValidationError("Вы можете выбрать ЛИБО связанную привычку ЛИБО вознаграждение, выберите что-то одно")

def time_performance(val):
    if val["time_to_complete"] > timedelta(seconds=120):
        raise serializers.ValidationError("Время выполнения привычке не должно быть больше 120 секунд")

def pleasant_in_related(val):
    if val["sign_of_pleasant_habit"]:
        val["related_habit"]
    raise serializers.ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки.")

def limit_of_periodicity(val):
    if val["periodicity"] > 7:
        raise serializers.ValidationError(
            "Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")



