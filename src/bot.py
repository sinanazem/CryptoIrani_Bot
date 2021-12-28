import os
import telebot
from src.api.api import Crypto
from loguru import logger

telegram_bot_token = os.environ['TELEGRAMBOT_TOKEN']

class Bot():

    def __init__(self):
        self.bot = telebot.TeleBot(telegram_bot_token)
        logger.info("start bot...")
    def run(self):

        @self.bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            self.bot.reply_to(message, "Howdy, how are you doing?")

        @self.bot.message_handler(commands=['doge','DOGE','Doge'])
        def doge_coin(message):
            logger.info("doge...")
            a = Crypto('doge')
            self.bot.send_message(message.chat.id, f"{a.price()}")

        @self.bot.message_handler(commands=['btc','BTC','Bitcoin','BITCOIN'])
        def btc_coin(message):
            logger.info("bitcoin...")
            a = Crypto('btc')
            self.bot.send_message(message.chat.id, f"{a.price()}")

        self.bot.infinity_polling()

if __name__ == "__main__":
    obj = Bot()
    obj.run()
