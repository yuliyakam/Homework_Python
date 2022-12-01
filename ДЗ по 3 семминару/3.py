# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random
#
# def generator_list(count_of_number, down_border, up_border):
#     list = []
#     for i in range(count_of_number):
#         list.append(random.randint(down_border, up_border))
#     return list
#
# list1 = generator_list(5,0,10)
# print(list1)
# summa = 0
#
# for i in range(1, len(list1)-1, 2):
#     summa += list1[i]
#     i += 2
# print("Сумма элементов на нечетных позициях = ", summa)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# list = [2, 3, 4, 5, 6]
# if len(list) % 2:
#     for i in range((len(list) // 2) + 1):
#         print(list[i] * list[-i - 1], end=' ')
# else:
#     for i in range(len(list) // 2):
#         print(list[i] * list[-i - 1], end=' ')

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = [1.1, 1.2, 3.1, 5, 10.01]
# list1 = []
# for i in range(len(list)):
#     list1.append(list[i] - int(list[i]))
# print(max(list1) - min(list1))

# Напишите программу, которая будет преобразовывать десятичное число в двоичное
# (встроенными методами пользоваться нельзя).
# Пример:
# 45 -> 101101

# print("Введите десятичное число для преобразования его в двоичное ")
# number = int(input())
# binar_number = ''
#
# while number // 2 != 0:
#     binar_number += str(number % 2)
#     number = number // 2
#
# binar_number += '1'
# print(binar_number[:: -1])

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

#               Первый способ через списки:
# print("Введите колличество элементов последовательности ")
# n = int(input())
# list = [1, 1]
# list1 = []
# # Собираем последовательность Фибоначчи
# for i in range(n-2):
#     list.append(list[i] + list[i+1])
# # В соответствии с четностью позиции меняем знак элемента, сохраняем в новом списке
# for i in range(len(list)):
#     if i % 2 == 0:
#         list1.append(list[i])
#     else:
#         list1.append(list[i]*(-1))
#
# list.insert(0, 0)
# list2 = list1[:: -1]
# for i in range(len(list)):
#     list2.append(list[i])
# print(list2, end=' ')

#               Второй способ через функции и рекурсию:
#number = int(input("Введите целое число "))

# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# def negafibonacci(n):
#     return (-1) ** (n + 1) * fibonacci(n)
#
# list_fibonacci = []
# for i in range(number + 1):
#     list_fibonacci.append((negafibonacci(i)))
#
# list_fibonacci.reverse()
# list_fibonacci.pop(-1)
#
# for i in range(number + 1):
#     list_fibonacci.append(fibonacci(i))
# print(list_fibonacci)
