import os
import time
from telebot import TeleBot
from week import get_current_week as week

TOKEN = os.getenv('TOKEN')
bot = TeleBot(TOKEN)


@bot.message_handler(commands="week")
def week_number(message):
    bot.reply_to(message, f"Текущая неделя: {week()}")


while True:
    try:
        print('Starting...')
        bot.polling()
    except:
        print('Some error has occurred.')
    finally:
        print('Restarting...')
