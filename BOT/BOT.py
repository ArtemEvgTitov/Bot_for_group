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
work_schedule = []


def message(update, _):
    text = update.message.text
    load()
    if text == 'Бот график':
        update.message.reply_text(work_schedule[0])
    elif text == '#график':
        work_schedule.append(text)
        save()
    elif text in hello_text:
        random_photo = random.choice(hello)
        update.message.reply_text(random_photo)

def load():
    global hello
    global hello_text
    global work_schedule
    with open("hello.json", "r", encoding="utf-8") as fh:
        hello = json.load(fh)
    with open("hello_text.json", "r", encoding="utf-8") as fh:
        hello_text = json.load(fh)
    with open("work_schedule.json", "r", encoding="utf-8") as fh:
        work_schedule = json.load(fh)

def save():
    with open("work_schedule.json", "w", encoding="utf-8") as graf:
        graf.write(json.dumps(work_schedule, ensure_ascii=False))

if __name__ == '__main__':
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    message_handler = MessageHandler(Filters.text, message)

dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()