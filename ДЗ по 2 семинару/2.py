# №1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0.56 -> 11

# print("Введите вещественное число\n")
# sum = 0
# str = input()                             # Код Лили
# for i in range(len(str)):             # for i in str:
#     if str[i].isdigit():              #   if i.isdigit():
#         sum += int(str[i])                    # sum += int(i)
# print("Сумма цифр числа = ", sum)

# №2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# count = 1
#
# print("Введите  число N \n")
# n = int(input())
# for i in range(1, n+1):
#     count = count * i
#     print(count, end=' ')

# №3 Задайте список из n чисел последовательности (1+1/n)*n выведите на экран их сумму.
#
# print("Введите  число N \n")
# n = int(input())
# summa = 0

# for i in range(1, n+1):
#     summa = summa + (1+1/i) ** i
# print(round(summa, 2))

# №4 Задайте числами список из N элементов, заполненных из промежутка [-N, N]. Найдите произведение элементов на указан
# ных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
#           Решение, где номера позиций множителей находятся в программе:
# list = []
# position_list = []
# product = 1

# print("Введите число N ")
# n = int(input())

# for i in range(-n, n+1):
#     list.append(i)
# print('Последовательность элементов: \n', list, end=' ')
# print("\n Произведение скольких элементов вы хотите найти?\n")
# count = int(input())
#
# print("Введите номера позиций элементов, произведение которых вы хотите найти\n")
# while count != 0:
#     position_list.append(input())
#     count -= 1
#
# for i in position_list:
#     product = int(list[int(i)]) * product
# print('\n','Произведение = ', product)

#           Решение, где номера позиций множителей находятся в файле file.txt:
list = []
position_list = []
product = 1

print("Введите число N ")
n = int(input())

for i in range(-n, n + 1):
    list.append(i)
print('Последовательность элементов: \n', list, end=' ')
print("\n Произведение скольких элементов вы хотите найти?\n")
count = int(input())

# Очистка файла перед записью
with open('file.txt', 'w') as data:
    data.write('')

# Запись в файл позиций множителей
print("Введите номера позиций элементов, произведение которых вы хотите найти\n")
while count != 0:
    with open('file.txt', 'a') as data:
        data.write(input(''))
        data.write('\n')
        count -= 1

# Открытие файла для получения данных           # with open('file.txt', 'r') as f:
path = 'file.txt'                                   # inds = f.readlines()
data = open(path, 'r')                              # multiple = 1
for line in data:                               # for i in inds:
    product = list[int(line)] * product             # multiple *= list[int(i)]
data.close()                                    # print(multiple)

print('\n', 'Произведение = ', product)

# №5 Реализуйте алгоритм перемешивания списка (shuffle использовать нельзя, другие методы из библиотеки random - можно).
#           Первый способ перевернуть массив:
# list = [1, 2, 3, 4, 5, 6, 7, 8]
#
# for i in range(len(list) // 2):
#     current = list[i]
#     list[i] = list[-i-1]
#     list[-i - 1] = current
# print(list)
#           Второй способ:
# import random
#
# list = [1, 2, 3, 4, 5, 6, 7, 8]
# positoin = []
# mixed_list = []
#
# while len(list) != len(positoin):
#     j = random.randint(0, len(list)-1)
#     if not j in positoin:
#         positoin.append(j)
# print(list)
# print(positoin)
#
# for i in range(len(list)):
#     mixed_list.append(list[positoin[i]])
# print(mixed_list, end=' ')
#               Третий способ:
# import random
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in range(0, len(numbers)):
#     k = random.randint(0, len(numbers) - 1)
#     numbers[i], numbers[k] = numbers[k], numbers[i]
# print(numbers)















