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
    elif "все заявления" in (message.text).lower():
        load_statements()
        count = 1
        for i in Statements:
            date = i['date']
            text = i['statement']
            bot.send_message(message.from_user.id, f"{count}. {date}, {text}")
            count += 1

    elif "заявление " in (message.text).lower():
        load_statements()
        week = 604800
        message.text = re.sub('Заявление ', '', message.text)
        time_message = datetime.utcfromtimestamp(
            message.date).strftime('%Y-%m-%d')
        time_notification = datetime.utcfromtimestamp(
            message.date + week).strftime('%Y-%m-%d')
        statements_element = {"type": 'Заявление', "date": time_message,
                              "statement": message.text, "date_notif": time_notification}
        Statements.append(statements_element)
        save_statements()
        print(statements_element)
        bot.send_message(message.from_user.id,
                         f"Сохранил.\nТип: {statements_element['type']}"
                         f"\nДата: {statements_element['date']}"
                         f"\nТекст: {statements_element['statement']}"
                         f"\nДата напоминания: {statements_element['date_notif']}")
        time.sleep(10)
        bot.send_message(message.from_user.id,
                         f"Напоминаю!.\nТип: {statements_element['type']}"
                         f"\nТекст: {statements_element['statement']}")

    else:
        bot.send_message(message.from_user.id,
                         "Я тебя не понимаю. 😔")


bot.polling(none_stop=True)
