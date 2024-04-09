from celery import shared_task
from datetime import datetime, timedelta
from config import settings
from habits.models import Habit
from services.send_tg_bot import create_message, send_message


@shared_task
def check_and_send():
    bot_token = settings.TELEGRAM_API_TOKEN
    """
        Отправляет напоминания о привычках пользователям через Telegram.
    """
    good_habit = Habit.objects.filter(sign_of_pleasant_habit=False)
    now_time = datetime.now().time()
    now_date = datetime.now().today()

    for habit in good_habit:
        if not habit.next_date:
            if habit.time < now_time:

                chat_id, message = create_message(habit)
                send_message(chat_id, message, bot_token)
                habit.next_date = now_date + timedelta(days=habit.periodicity)
                habit.save()

            elif habit.next_date <= now_date:

                chat_id, message = create_message(habit)
                send_message(chat_id, message, bot_token)
                habit.next_date = now_date + timedelta(days=habit.periodicity)
                habit.save()