import telegram
import os
from dotenv import load_dotenv
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
import logging
from telegram.ext import BaseFilter


load_dotenv()

# logger to see what's happening
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger('Ofertas_trabajo_bot')

logger.info('El programa esta corriendo')

# bot will respond to /start
def start(update, context):
    logger.info('He recibido un comando start')
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Soy un bot! Por favor hablame :) PS: Estoy en periodo de pruebas)")


# returns message in all caps
def caps(update, context):
    logger.info('He recibido un comando caps')
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


# add echo
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def jobs(update, context):
    logger.info("Estoy en el callback de jobs")
    # logger.info(update.effective_chat)
    # logger.info(context)
    # logger.info(update)
    context.bot.send_message(chat_id=os.getenv('USER_ID'), text=update.message.text)
    # instead of send_message should send original message to specific user
    #sending messages to myself with the user_id variable


# catch unknown messages, must be the last handler
def unknown(update, context):
    logger.info('He recibido un comando desconocido')
    context.bot.send_message(chat_id=update.effective_chat.id, text="No entendí ese comando.")


# custom filter
class FilterJobs(BaseFilter):
    def filter(self, message):
        if message.text:
            return 'python' or 'sistemas' or 'programación' in message.text.lower()

# Remember to initialize the class.
filter_jobs = FilterJobs()

# jobs_handler = MessageHandler(filter_jobs, jobs)

# command that returns a list of messages, filters them by the input and dates

# start bot
if __name__ == '__main__':

    updater = Updater(token=os.getenv('TOKEN'), use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('caps', caps))
    # dispatcher.add_handler(MessageHandler(Filters.regex(r'python'), jobs))
    dispatcher.add_handler(MessageHandler(filter_jobs, jobs))
    # dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()

# MessageHandlers should answer to messager written in group chats