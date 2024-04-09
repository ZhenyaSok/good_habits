from datetime import timedelta

from rest_framework import serializers


"""
Валидаторы

???В связанные привычки могут попадать только привычки с признаком приятной привычки.
У приятной привычки не может быть вознаграждения или связанной привычки.
"""

def valid_one_field_out_of_two(val):
    if val["related_habit"] and val["reward"]:
        raise serializers.ValidationError("Вы можете выбрать ЛИБО связанную привычку ЛИБО вознаграждение, выберите что-то одно")

def time_performance(val):
    if val["time_to_complete"] > timedelta(seconds=120):
        raise serializers.ValidationError("Время выполнения привычке не должно быть больше 120 секунд")

def pleasant_in_related(val):
    if val['related_habit']:
        if not val['related_habit'].sign_of_pleasant_habit:
        # if val["sign_of_pleasant_habit"]:
        #     val["related_habit"].
            raise serializers.ValidationError("В связанные привычки могут попадать только привычки "
                                              "с признаком приятной привычки.")


def limit_of_periodicity(val):
    if val["periodicity"] > 7:
        raise serializers.ValidationError(
            "Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")


def only_pleasant_in_related(val):
    if val["sign_of_pleasant_habit"]:
        if val['related_habit'] or val['reward']:
            # if val["pleasant_in_related"] and val["reward"] or val["pleasant_in_related"] and val["related_habit"]:
            raise serializers.ValidationError('У приятной привычки не может быть'
                                              ' вознаграждения или связанной привычки')




