from token_1 import *
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
import logging
import random

reply_keyboard = [['/play', '/settings', '/rules', '/close', '/stop']]

candies = 50
step = 15
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False, resize_keyboard=True)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = token1


def start(update, context):
    global candies
    candies = 50
    name = f"{update.message.from_user.first_name} {update.message.from_user.last_name}"
    update.message.reply_text(
        f"Привет, {name}! Давай поиграем? Чтобы узнать правила игры нажми /rules\nначать игру нажми /play"
        f"\nизменить настройки нажми /settings\nзакрыть клавиатуру нажми /close\nостановить бота - введи команду "
        f"/stop или нажмите кнопку /stop",
        reply_markup=markup
    )


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def rules(update, context):
    update.message.reply_text(
        "На столе лежат конфеты. Играют человек и компьютер, делая ход друг после друга. В начале игры нужно"
        " определить количество конфет на кону и количество конфет, которое можно взять за один раз. Для этого"
        " необходимо нажать settings и ввести 2 числа через пробел. Первое - банк(общее колиество), второе - ход."
        "По умолчанию банк = 50, а максимум за ход = 15. Первый ход делает человек. Все конфеты оппонента "
        "достаются сделавшему последний ход. Для запуска игры по умолчанию нажмите /play")


def settings(update, context):
    update.message.reply_text("Введите количество конфет на кону и максимально возможное количество на ход через "
                              "пробел")
    return 1


def set_settings(update, context):
    global candies
    global step
    candies, step = map(int, update.message.text.split())
    update.message.reply_text("Правила установлены, начинаем! Нажмите /play", reply_markup=markup)
    return ConversationHandler.END


def play(update, context):
    update.message.reply_text(f"На кону {candies} конфет. Ваш ход. Какое количество конфет вы берете?"
                              f"(Максимальное = {step} )", reply_markup=ReplyKeyboardRemove())
    reply_keyboard1 = [['/stop']]
    markup1 = ReplyKeyboardMarkup(reply_keyboard1, one_time_keyboard=False, resize_keyboard=True)
    update.message.reply_text("Если вы хотите остановить игру нажмите stop", reply_markup=markup1)
    return 1


def play_step(update, context):
    global candies
    candiy = int(update.message.text)
    if candiy > step:
        update.message.reply_text(f"Число должно быть меньше {step}!")
        return 1
    candies -= candiy
    if candies == 0:
        update.message.reply_text("Поздравляю, Вы победили!", reply_markup=markup)
        candies = 50
        return ConversationHandler.END
    if candies <= step:
        update.message.reply_text("Игра окончена, я забираю оставшиеся конфеты, я победил! ", reply_markup=markup)
        candies = 50
        return ConversationHandler.END
    else:
        if candies % (step + 1) == 0:
            update.message.reply_text(f"На кону {candies} конфет, я беру {random.randint(1, step)}, следующий ход ваш")
            candies -= random.randint(1, step)
        else:
            update.message.reply_text(f"На кону {candies} конфет, я беру {candies % (step + 1)}, следующий ход ваш")
            candies -= candies % (step + 1)
    if candies <= step:
        update.message.reply_text("Поздравляю, Вы победили!", reply_markup=markup)
        candies = 50
        return ConversationHandler.END


def stop(update, context):
    update.message.reply_text("Всего доброго! Если передумаете, я с удовольствием сыграю ещё раз, просто введите "
                              "команду /start")
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    settings_hundler = ConversationHandler(
        entry_points=[CommandHandler('settings', settings)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, set_settings)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    play_hundler = ConversationHandler(
        entry_points=[CommandHandler('play', play)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, play_step)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("stop", stop))
    dp.add_handler(CommandHandler("close", close_keyboard))
    dp.add_handler(settings_hundler)
    dp.add_handler(play_hundler)


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
