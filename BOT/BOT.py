import logger as log
from settings import TOKEN
import json
import operator
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

SURNAME, NAME, TEL_NUMBER = range(3)

