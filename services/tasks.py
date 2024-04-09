# from celery import shared_task
# from datetime import datetime, timedelta
from config import settings
# from habits.models import Habit
# from services.send_tg_bot import create_message, send_message
import telebot
# import os
from celery import shared_task
from datetime import datetime, timedelta, timezone
from habits.models import Habit


API_KEY = settings.TELEGRAM_API_TOKEN

@shared_task
def your_habits():
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


# @shared_task
# def your_habits():
#     now = datetime.now(tz=timezone.utc)
#     bot = telebot.TeleBot(API_KEY)
#     habits = Habit.objects.filter(time__lte=now)
#
#     for habit in habits:
#         chat_id = habit.owner.chat_id
#         message = (f'В {habit.time.strftime("%H:%M")} '
#                    f'вы планировали сделать {habit.action} в {habit.place}')
#
#         try:
#             bot.send_message(chat_id=chat_id,
#                                         text=message)
#             habit.time += timedelta(days=habit.periodicity)
#             break
#
#         except Exception as e:
#             print(e)
#
#         finally:
#             habit.save()









# def check_and_send():
#     bot_token = settings.TELEGRAM_API_TOKEN
#     """
#         Отправляет напоминания о привычках пользователям через Telegram.
#     """
#     good_habit = Habit.objects.filter(sign_of_pleasant_habit=False)
#     now_time = datetime.now().time()
#     now_date = datetime.now().today()
#
#     for habit in good_habit:
#         if not habit.next_date:
#             if habit.time < now_time:
#
#                 chat_id, message = create_message(habit)
#                 send_message(chat_id, message, bot_token)
#                 habit.next_date = now_date + timedelta(days=habit.periodicity)
#                 habit.save()
#
#             elif habit.next_date <= now_date:
#
#                 chat_id, message = create_message(habit)
#                 send_message(chat_id, message, bot_token)
#                 habit.next_date = now_date + timedelta(days=habit.periodicity)
#                 habit.save()