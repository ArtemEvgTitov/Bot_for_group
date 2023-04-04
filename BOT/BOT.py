from settings import TOKEN
import telebot
import random
import json

bot = telebot.TeleBot(TOKEN)

work_schedule = []
hello = []
hello_text = []


def load_hello():
    global hello
    global hello_text
    with open("hello.json", "r", encoding="utf-8") as fh:
        hello = json.load(fh)
    with open("hello_text.json", "r", encoding="utf-8") as fh:
        hello_text = json.load(fh)


def load_graf():
    global work_schedule
    try:
        with open("work_schedule.json", "r", encoding="utf-8") as graf:
            work_schedule = json.load(graf)
    except:
        print("Графика нет")


def is_part_in_list(str_, words):
    for word in words:
        if word in str_:
            return True
    return False


@bot.message_handler(content_types=['text', 'photo'])
def get_text_messages(message):
    load_hello()
    load_graf()
    if is_part_in_list(message.text, hello_text):
        random_photo = random.choice(hello)
        bot.send_photo(
            message.chat.id, photo=f'{random_photo}')
    elif message.text == 'Бот график':
        graf = work_schedule[0]
        bot.send_photo(
            message.chat.id, photo=f'{graf}')
    else:
        bot.send_message(message.from_user.id,
                         "Я тебя не понимаю. 😔")


bot.polling(none_stop=True)
