import os
import telebot
from src.api.api import Crypto
from loguru import logger

bot = telebot.TeleBot("2132611794:AAHmt-xSMAffOIdujvG5VRN_8iqsRB4CeXo")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['doge','DOGE','Doge'])
def doge_coin(message):
    logger.info("doge...")
    a = Crypto('doge')
    bot.send_message(message.chat.id, f"{a.price()}")

@bot.message_handler(commands=['btc','BTC','Bitcoin','BITCOIN'])
def btc_coin(message):
    logger.info("bitcoin...")
    a = Crypto('btc')
    bot.send_message(message.chat.id, f"{a.price()}")

bot.infinity_polling()

