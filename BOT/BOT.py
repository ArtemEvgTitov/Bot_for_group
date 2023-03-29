from settings import TOKEN
import telebot
import random
import json
import re
from telebot import types

bot = telebot.TeleBot(TOKEN)

films = []
hello = []
hello_text = []

def load_hello():
    global hello
    global hello_text
    with open("hello.json", "r", encoding="utf-8") as fh:
        hello = json.load(fh)
    with open("hello_text.json", "r", encoding="utf-8") as fh:
        hello_text = json.load(fh)

def is_part_in_list(str_, words):
    for word in words:
        if word in str_:
            return True
    return False
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    load_hello()
    if is_part_in_list(message.text, hello_text):
        random_photo = random.choice(hello)
        bot.send_photo(
            message.chat.id, photo=f'{random_photo}')
    else:
        bot.send_message(message.from_user.id,
                         "Я тебя не понимаю. 😔")


bot.polling(none_stop=True)