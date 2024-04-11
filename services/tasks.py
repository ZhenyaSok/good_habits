
from config import settings
import telebot
from celery import shared_task
from datetime import datetime, timedelta, timezone
from habits.models import Habit
from services.send_tg_bot import TelegramBot

API_KEY = settings.TELEGRAM_API_TOKEN


'''Вариант 1: Рассылка уведомление происходит при помощи class TelegramBot (в файле send_tg_bot)'''

@shared_task
def your_habits():
    now = datetime.now(tz=timezone.utc)
    bot = TelegramBot()
    habits = Habit.objects.filter(time__lte=now)

    for habit in habits:
        message = (f'В {habit.time.strftime("%H:%M")} '
                   f'вы планировали {habit.action} в {habit.place}')

        try:
            bot.send_message(text=message)
            habit.time += timedelta(days=habit.periodicity)
            break

        except Exception as e:
            print(e)

        finally:
            habit.save()


"""Вариант 2: при задействовании этой функции в периодическую задача,
рассылка будет происходить при помощи готовой библиотеки для рассылки в телеграмм (telebot)"""
def send_habits():
    now = datetime.now(tz=timezone.utc)
    bot = telebot.TeleBot(API_KEY)
    habits = Habit.objects.filter(time__lte=now)

    for habit in habits:
        chat_id = habit.owner.chat_id
        message = (f'В {habit.time.strftime("%H:%M")} '
                   f'вы планировали сделать {habit.action} в {habit.place}')

        try:
            bot.send_message(chat_id=chat_id,
                                        text=message)
            habit.time += timedelta(days=habit.periodicity)
            break

        except Exception as e:
            print(e)

        finally:
            habit.save()
