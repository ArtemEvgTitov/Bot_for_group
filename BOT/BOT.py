import logger as log
from settings import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


# def message(update, _):
#     text = update.message.text
#     if text == 'Создать контакт':
#         log.text_in_log('Нажата кнопка "Создать контакт"')
#         update.message.reply_text(
#             'Для отмены введите /cancel\n\nВведите фамилию')
#         return SURNAME
#     elif text == 'Изменить контакт':
#         log.text_in_log('Нажата кнопка "Изменить контакт"')
#         load()
#         temp = ''
#         if contact == []:
#             update.message.reply_text(
#                 f'В телефонной книге отсутствуют контакты')
#             cancel(update, _)
#         else:
#             for i in contact:
#                 temp += f'id: {i["id"] + 1}. {i["surname"]} {i["name"]} тел. {i["tel"]} ({i["comment"]})\n---------------------\n'
#             update.message.reply_text(
#                 f'{temp}\nВведите id контакта для изменения')
#             return EDIT
#     elif text == 'Поиск':
#         log.text_in_log('Нажата кнопка "Поиск"')
#         update.message.reply_text(
#             'Введите данные для поиска\n/cancel')
#         return SEARCH
#     elif text == 'Все контакты':
#         log.text_in_log('Нажата кнопка "Все контакты"')
#         all_cont(update, _)
#     elif text == 'Удалить все контакты':
#         log.text_in_log('Нажата кнопка "Удалить все контакты"')
#         reply_keyboard = [['Да', 'Нет']]
#         markup_key = ReplyKeyboardMarkup(
#             reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
#         update.message.reply_text(
#             'Вы уверены, что хотите удалить все контакты?\n/cancel', reply_markup=markup_key,)
#         return DELETE_ALL
#     elif text == 'Удалить контакт':
#         log.text_in_log('Нажата кнопка "Удалить контакт"')
#         load()
#         temp = ''
#         if contact == []:
#             update.message.reply_text(
#                 f'В телефонной книге отсутствуют контакты')
#             cancel(update, _)
#         else:
#             for i in contact:
#                 temp += f'id: {i["id"] + 1}. {i["surname"]} {i["name"]} тел. {i["tel"]} ({i["comment"]})\n---------------------\n'
#             update.message.reply_text(
#                 f'{temp}\nВведите id контакта для удаления')
#             return DEL_CONT
#     else:
#         log.text_in_log('Я не понял, что он хотел от меня')
#         update.message.reply_text('Я тебя не понимаю')
#         cancel(update, _)

# if __name__ == '__main__':
#     updater = Updater(token=TOKEN)
#     dispatcher = updater.dispatcher

#     start_handler = CommandHandler('start', start)
#     bot_handler = ConversationHandler(
#         entry_points=[MessageHandler(Filters.text, message)],
#         states={
#             SURNAME: [MessageHandler(Filters.text & ~Filters.command, surname)],
#             NAME: [MessageHandler(Filters.text & ~Filters.command, name)],
#             TEL: [MessageHandler(Filters.text & ~Filters.command, tel)],
#             COMMENT: [MessageHandler(Filters.text & ~Filters.command, comment)],
#             SEARCH: [MessageHandler(Filters.text & ~Filters.command, search)],
#             END_SEARCH: [MessageHandler(Filters.text & ~Filters.command, end_search)],
#             DELETE_ALL: [MessageHandler(Filters.text & ~Filters.command, delete_all)],
#             DEL_CONT: [MessageHandler(Filters.text & ~Filters.command, del_cont)],
#             DEl_C: [MessageHandler(Filters.text & ~Filters.command, del_c)],
#             EDIT: [MessageHandler(Filters.text & ~Filters.command, edit)],
#             EDITOR: [MessageHandler(Filters.text & ~Filters.command, editor)],
#             EDIT_SURNAME: [MessageHandler(Filters.text & ~Filters.command, edit_surname)],
#             EDIT_NAME: [MessageHandler(Filters.text & ~Filters.command, edit_name)],
#             EDIT_TEL: [MessageHandler(Filters.text & ~Filters.command, edit_tel)],
#             EDIT_COMMENT: [MessageHandler(Filters.text & ~Filters.command, edit_comment)],
#         },
#         fallbacks=[CommandHandler('cancel', cancel)],
#     )
#     message_handler = MessageHandler(Filters.text, message)


# dispatcher.add_handler(start_handler)
# dispatcher.add_handler(bot_handler)
# dispatcher.add_handler(message_handler)

# updater.start_polling()
# updater.idle()