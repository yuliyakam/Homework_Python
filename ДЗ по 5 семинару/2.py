# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

#               Человек против человека:

# import random
#
# def game(name, bank, step):
#     count = 0
#     name = name.title()
#     print(name +", cколько монет вы хотите взять? В начале игры вы решили брать не больше " + step + " монет ")
#     while bank > 0:
#         hod = int(input("Ваша ставка: "))
#         bank -= hod
#         print("Осталось " + str(bank) + "монет")
#         count += 1
#     if count % 2:
#         print(name + ", ты победитель, ПОЗДРАВЛЯЮ!")
#     else:
#         print(name + ", сожалею, ты проиграл. Может попробуешь ещё раз?")
#
# bank1 = int(input("Давайте сыграем! Какое количество монет на кону? "))
# step = input("Отлично! Определите максимальное количество монет, которое можно взять ")
# name_first_gamer = input("Введите имя первого игрока ")
# name_second_gamer = input("Введите имя второго игрока ")
# first_step = random.randint(1, 2)
# if first_step == 1:
#     print("Начинает игру " + name_first_gamer.title())
#     game(name_first_gamer, bank1, step)
# else:
#     print("Начинает игру " + name_second_gamer.title())
#     game(name_second_gamer, bank1, step)

#               Игра против бота c небольшим интелектом:)

import random

def game(name, bank, step):
    count = 0
    name = name.title()
    print(name +", cколько монет вы хотите взять? В начале игры вы решили брать не больше " + str(step) + " монет ")
    while bank > 0:
        hod = int(input("Ваша ставка: "))
        if hod <= step and hod <= bank:
            bank -= hod
            print("Осталось " + str(bank) + " монет")
            count += 1
            if bank > 0 and bank != step + 2 and bank != 1 and bank != step and bank > step:
                hod_bot = random.randint(1, step)
                bank -= hod_bot
                print("Бот сделал ход = " + str(hod_bot) + " Осталось " + str(bank) + " монет")
                count += 1
            elif bank == step + 2 or bank == 1:
                hod_bot = 1
                bank -= hod_bot
                print("Бот сделал ход = " + str(hod_bot) + " Осталось " + str(bank) + " монет")
                count += 1
            elif bank <= step and bank > 0:
                print("Бот сделал ход = " + str(bank) + " Осталось 0 монет")
                bank = 0
                count += 1
            else:
                break
        else:
            print("Вы хотите взять слишком много!")

    if count % 2:
        print(name + ", ты победитель, ПОЗДРАВЛЯЮ!")
    else:
        print(name + ", сожалею, ты проиграл. Может попробуешь ещё раз?")

def game_bot(name, bank, step):
    count = 0
    name = name.title()
    print("В начале игры решили брать не больше " + str(step) + " монет. Бот делает шаг ")
    while bank > 0:
        if bank != step + 2 and bank != 1 and bank != step:
            hod = random.randint(1, step)
            bank -= hod
            print("Бот сделал ход = " + str(hod) + " Осталось " + str(bank) + " монет")
            count += 1
        elif bank == step + 2 or bank == 1:
            hod = 1
            bank -= hod
            print("Бот сделал ход = " + str(hod) + " Осталось " + str(bank) + " монет")
            count += 1
        elif bank <= step:
            print("Бот сделал ход = " + str(bank) + " Осталось 0 монет")
            bank = 0
            count += 1
        if bank > 0:
            gamer_hod = int(input("Ваша ставка: "))
            if gamer_hod <= step and hod <= bank:
                bank -= gamer_hod
                count += 1
            else:
                while gamer_hod > step:
                    print("Вы хотите взять слишком много! Cтавка должна быть не больше  " + f"{step}")
                    gamer_hod = int(input("Ваша ставка: "))
                bank -= gamer_hod
                count += 1
        else:
            break

    if count % 2:
        print(name + ", ты победитель, ПОЗДРАВЛЯЮ!")
    else:
        print(name + ", сожалею, ты проиграл. Может попробуешь ещё раз?")

bank1 = int(input("Давайте сыграем! Какое количество монет на кону? "))
step = int(input("Отлично! Определите максимальное количество монет, которое можно взять "))
name_first_gamer = input("Введите ваше имя ")
name_second_gamer = 'бот'
first_step = random.randint(1, 2)
if first_step == 1:
    print("Начинает игру " + name_first_gamer.title())
    game(name_first_gamer, bank1, step)
else:
    print("Начинает игру " + name_second_gamer.title())
    game_bot(name_second_gamer, bank1, step)

