import os
import telebot
from src.api.api import doge,btc
from loguru import logger



bot = telebot.TeleBot(os.environ['TELEGRAM_BOT_TOKEN'])



bot = telebot.TeleBot("5008852964:AAFkLqhkdnk2Nx8cFvoqlE-sZju-mSJASro")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['doge','DOGE','Doge'])
def doge_coin(message):
    logger.info("doge...")
    a = doge()
    bot.send_message(message.chat.id, f"{a}")

@bot.message_handler(commands=['btc','BTC','Bitcoin','BITCOIN'])
def doge_coin(message):
    logger.info("bitcoin...")
    a = btc()
    bot.send_message(message.chat.id, f"{a}")

bot.infinity_polling()

