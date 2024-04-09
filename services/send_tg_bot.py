from config import settings
import requests


URL = 'https://api.telegram.org/bot'
TOKEN = settings.TELEGRAM_API_TOKEN
chat_id = settings.TELEGRAM_ID

class TelegramBot:
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_API_TOKEN
    chat_id = settings.TELEGRAM_ID

    def send_message(self, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': self.chat_id,
                'text': text
            }
        )
        print(text)



def create_message(habit):
    """Функция создания сообщения"""
    if habit.owner.chat_id:
        chat_id = habit.owner.chat_id
        message = f"Напоминание: {habit.action} в {habit.place} в {habit.time.strftime('%H:%M')}"

    if habit.reward:
        message += f" Награда за выполнение: {habit.reward}."

    if habit.related_habit:
        related_habit_action = habit.related_habit.action
        message += f" Связанная привычка: {related_habit_action}."

    return chat_id, message