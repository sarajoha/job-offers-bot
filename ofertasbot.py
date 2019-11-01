import telegram
import os
from dotenv import load_dotenv
from telegram.ext import Updater
import logging


load_dotenv()

# bot object
bot = telegram.Bot(token=os.getenv('TOKEN'))
print(bot.get_me())

# logger to see what's happening
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# bot will respond to /start
updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher
