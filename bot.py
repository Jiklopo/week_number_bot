import os
import telebot
import logging
from flask import Flask, request
from telebot import TeleBot
from week import get_current_week as week

TOKEN = os.getenv('TOKEN')
bot = TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands="week")
def week_number(message):
    bot.reply_to(message, f"Текущая неделя: {week()}")


if "HEROKU" in list(os.environ.keys()):
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)

    server = Flask(__name__)


    @server.route("/bot", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200


    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url="https://week-number-bot.herokuapp.com/")
        return "?", 200


    server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
else:
    bot.remove_webhook()
    bot.polling(none_stop=True)
