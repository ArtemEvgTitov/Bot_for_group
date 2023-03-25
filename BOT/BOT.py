import logger as log
from settings import TOKEN
import random
import json
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
hello = []
hello_text = []


def message(update, _):
    text = update.message.text
    load_hello()
    if text == 'Бот график':
        update.message.reply_text(
            'https://t.me/c/1159615196/69')
    elif text in hello_text:
        random_photo = random.choice(hello)
        update.message.reply_text(random_photo)

def load_hello():
    global hello
    global hello_text
    with open("hello.json", "r", encoding="utf-8") as fh:
        hello = json.load(fh)
    with open("hello_text.json", "r", encoding="utf-8") as fh:
        hello_text = json.load(fh)

if __name__ == '__main__':
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    message_handler = MessageHandler(Filters.text, message)

dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()