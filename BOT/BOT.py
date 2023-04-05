import re
from datetime import datetime
from settings import TOKEN
import telebot
import random
import json

bot = telebot.TeleBot(TOKEN)

hello = []
hello_text = []
Statements = []


def load_statements():
    global Statements
    with open("Statements.json", "r", encoding="utf-8") as stat:
        Statements = json.load(stat)

def save_statements():
    with open("Statements.json", "w", encoding="utf-8") as stat:
        stat.write(json.dumps(Statements, ensure_ascii=False))
    print("Заявление сохранено")

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
    elif "Заявление " in message.text:
        message.text = re.sub('Заявление ', '', message.text)
        time = datetime.utcfromtimestamp(message.date).strftime('%Y-%m-%d')
        statements_element = {"type": 'Заявление', "date": time, "statement": message.text}
        Statements.append(statements_element)
        save_statements()
        print(statements_element)
        bot.send_message(message.from_user.id,
                         f"Сохранил.\nТип: {statements_element['type']}"
                         f"\nДата: {statements_element['date']}"
                         f"\nТекст: {statements_element['statement']}")

    else:
        bot.send_message(message.from_user.id,
                         "Я тебя не понимаю. 😔")


bot.polling(none_stop=True)
