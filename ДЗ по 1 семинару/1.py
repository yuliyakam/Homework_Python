# №1 Программа принимает цифру, обозначающую день недели и выдает, является ли этот день выходным
# def day_of_week(days_number):
#     list = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
#     if days_number == 5 or days_number == 6:
#         print(list[days_number]," - это выходной день")
#     if days_number>=0 and days_number<=4:
#         print(list[days_number]," - это не выходной день")
#     else:
#         print("Такого дня недели не существует")
#
# print("Введите номер дня недели, где 0 это Понедельник\n")
# days_number = int(input())
# day_of_week(days_number)

# №2 Программа проверки истинности выраженя не(Х V У V Z)=неХ и неУ и неZ для всех значений предикат
# list = [True,False]
# for i in list:
#     for j in list:
#         for k in list:
#             print(i, j, k)
#             if (not(i or j or k)) ==((not i ) and (not j) and (not k)):
#                 print(True)
#             else:
#                 print(False)

# №3 Программа принимает на вход координаты точек, причем х не 0 и у не 0. Выдает номер четверти плоскости,
# в которой находится эта точка.
# print("Введите координату Х")
# x = int(input())
# print("Введите координату Y")
# y = int(input())
# if x != 0 and y !=0:
#     if x > 0 and y > 0:
#         print('Точка в I четверти')
#     if x < 0 and y > 0:
#         print('Точка во II четверти')
#     if x < 0 and y < 0:
#         print('Точка в III четверти')
#     if x > 0 and y < 0:
#         print('Точка в IV четверти')
# else:
#     print("Точка лежит на оси координат или является началом")

# №4 Программа по заданному номеру четверти выводит возможные координаты точки
# print("Введите номер четверти от 1 до 4")
# num = int(input())
# if num >= 1 and num <= 4:
#     if num == 1:
#         print(' x > 0 and y > 0')
#     if num == 2:
#         print(' x < 0 and y > 0')
#     if num == 3:
#         print('x < 0 and y < 0')
#     if num == 4:
#         print('x > 0 and y < 0')
# else:
#     print("Введите корректное значение номера четверти")

# №5 Программа принимает на вход координаты 2х точек и определяет расстояние между ними в пространствею прим:(3,6)
# (2,1)=5,09
# print("Введите координату первой точки")
# x1 = int(input())
# y1 = int(input())
# print("Введите координаты второй точки")
# x2 = int(input())
# y2 = int(input())
#
# distance =((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
#
# print("Расстояние между точками = ", round(distance,3))


