import logging
import model_db
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from token_1 import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = token1

def start(update, context):
    model_db.connect()
    update.message.reply_text(
    "Привет. Выберите команду\n/all- посмотреть список контактов\n/find - поиск по фамилии\n/add - добавить"
    "\n/update - изменить номер абонента с заданной фамилией\n/delete - удалить абонента с заданной фамилией"
    "\n/stop - остановить бота")

def find(update, context):
    update.message.reply_text("Введите фамилию c заглавной буквы  ")
    return 1

def add(update, context):
    update.message.reply_text("Введите Фамилию Имя телефон через пробел ")
    return 1

def delete(update, context):
    update.message.reply_text("Кого удалить из контактов? Введите фамилию")
    return 1

def update(update, context):
    update.message.reply_text("Введите Фамилию и новый номер телефона через пробел ")
    return 1

def stop(update, context):
    update.message.reply_text("Всего доброго!")
    model_db.disconnect()
    return ConversationHandler.END

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    find_handler = ConversationHandler(
        entry_points=[CommandHandler('find', find)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, model_db.find_abonent)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    add_handler = ConversationHandler(
        entry_points=[CommandHandler('add', add)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, model_db.add_abonent)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    delete_handler = ConversationHandler(
        entry_points=[CommandHandler('delete', delete)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, model_db.delete_abonent)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    update_handler = ConversationHandler(
        entry_points=[CommandHandler('update', update)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, model_db.update_info)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    start_handler = CommandHandler('start', start)
    read_handler = CommandHandler('all', model_db.all)
    dp.add_handler(start_handler)
    dp.add_handler(read_handler)
    dp.add_handler(find_handler)
    dp.add_handler(add_handler)
    dp.add_handler(delete_handler)
    dp.add_handler(update_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

