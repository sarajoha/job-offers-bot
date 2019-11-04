import telegram
import os
from dotenv import load_dotenv
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
import logging
from telegram.ext import BaseFilter


load_dotenv()

# bot object
bot = telegram.Bot(token=os.getenv('TOKEN'))
print(bot.get_me())

# logger to see what's happening
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token=os.getenv('TOKEN'), use_context=True)
dispatcher = updater.dispatcher


# bot will respond to /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Soy un bot! Por favor hablame :)")
 
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


# add echo
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


# returns message in all caps
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)


# custom filter
class FilterJobs(BaseFilter):
    def filter(self, message):
        return 'python' in message.text

# Remember to initialize the class.
filter_jobs = FilterJobs()


def jobs(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Esto es ago de Python")
    # instead of send_message should send original message to specific user

jobs_handler = MessageHandler(filter_jobs, jobs)
dispatcher.add_handler(jobs_handler)


# catch unknown messages, must be the last handler
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="No entendí ese comando.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

# start bot
updater.start_polling()