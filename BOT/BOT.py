import re
from datetime import datetime
import time
from settings import TOKEN
import telebot
import random
import json

bot = telebot.TeleBot(TOKEN)

hello = []
hello_text = []
Statements = []


def load_statements():
    try:
        global Statements
        with open("Statements.json", "r", encoding="utf-8") as stat:
            Statements = json.load(stat)
    except:
        save_statements()
        load_statements()


def save_statements():
    with open("Statements.json", "w", encoding="utf-8") as stat:
        stat.write(json.dumps(Statements, ensure_ascii=False))


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
    elif "все заявления" in (message.text).lower():
        load_statements()
        if Statements == []:
            bot.send_message(message.from_user.id, "Список пуст")
        else:
            for i in Statements:
                id = i['ID']
                date = i['date']
                text = i['statement']
                bot.send_message(message.from_user.id,
                                 f"ID {id}. {date}, {text}")

    elif "заявление " in (message.text).lower():
        load_statements()
        week = 604800
        id = 0
        if Statements != []:
            id = 1 + Statements[-1]['ID']
        message.text = re.sub('заявление ', '', message.text)
        time_message = datetime.utcfromtimestamp(
            message.date).strftime('%Y-%m-%d')
        time_notification = datetime.utcfromtimestamp(
            message.date + week).strftime('%Y-%m-%d')
        statements_element = {"ID": id, "type": 'Заявление', "date": time_message,
                              "statement": message.text, "date_notif": time_notification}
        Statements.append(statements_element)
        save_statements()
        print(statements_element)
        bot.send_message(message.from_user.id,
                         f"Сохранил.\nТип: {statements_element['type']}"
                         f"\nДата: {statements_element['date']}"
                         f"\nТекст: {statements_element['statement']}"
                         f"\nДата напоминания: {statements_element['date_notif']}")
    else:
        bot.send_message(message.from_user.id,
                         "Я тебя не понимаю. 😔")


bot.polling(none_stop=True)
