from django.core.management import BaseCommand

from services.send_tg_bot import TelegramBot


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        bot = TelegramBot()
        bot.send_message('Тест')
