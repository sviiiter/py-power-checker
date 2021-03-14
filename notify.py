from os import system
import telebot
from config import telegaToken, telegaGroupChatId


# TODO: add telegram bot
class Notification:
    def __init__(self, text, title='Внимание!'):
        self.text = text
        self.title = title

    def show_notification(self):
        command = f"" \
                  f"osascript -e 'display notification \"{self.text}\" with title \"{self.title}\"'" \
                  f""
        system(command)

    def telegram_bot(self):
        bot = telebot.TeleBot(telegaToken)
        bot.send_message(telegaGroupChatId, self.text)
