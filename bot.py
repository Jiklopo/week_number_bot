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
    cnt = 0
    try:
        print('Starting...')
        bot.polling()
    except:
        #cnt = 1
        print('Some error has occurred.')
    finally:
        time.sleep(10 + 600 * cnt)
        print('Restarting...')
        cnt = 0
