import os
import telebot
from datetime import datetime, timedelta
from flask import Flask, request
from telebot import TeleBot, types

TOKEN = os.getenv('TOKEN')
SEMESTER_START = datetime.strptime(os.getenv('SEMESTER_START'), '%d/%m/%y %H:%M:%S')
APP_URL = 'http://week-number-bot.herokuapp.com/'
bot = TeleBot(TOKEN)
server = Flask(__name__)


def get_current_week():
    d = datetime.today() + timedelta(hours=6) - SEMESTER_START
    return f'Текущая неделя: {d.days // 7 + 1}'


@bot.message_handler(commands="week")
def week_number(message):
    bot.reply_to(message, get_current_week())


@bot.inline_handler(lambda query: True)
def inline_week_number(query):
    r = types.InlineQueryResultArticle(id='1', title='Номер недели', input_message_content=types.InputTextMessageContent(message_text=get_current_week()))
    bot.answer_inline_query(query.id, [r])


@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=os.getenv('PORT', 5000))