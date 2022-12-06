# №1 Округлить число Пи по заданной точности

# Метод округления чисел
def my_raunding(number, number_raund):

    dr = number.split(".")
    str1 = dr[1]
    str2 = ''
    i = 0

    if len(dr[1]) == number_raund:    
        print("Ваше число уже округлено до нужного знака!")
        exit()
    
    while i < number_raund:
        str2 = str2 + str1[i] # В переменную str2 собираем дробную часть числа
        i += 1

    if int(str1[number_raund]) >= 5:# Проверяем следующую цифру числа после необходимой позиции округления
        a = int(str2[i - 1]) + 1 # Если >= 5, то преобразуем строку в список, чтобы вставить цифру больше на 1
        b = list(str2)
        b.insert(i - 1,str(a))
        b.pop() # Обрезаем до нужной позиции округления  
        print(dr[0] + "." + "".join(b))
    else:
        print(dr[0]+"."+str2) 

number = input("Введите число, которое вы хотите округлить, целую часть от дробной отделите точкой! ")
number_raund = int(input("Введите сколько знаков после точки нужно оставить "))
my_raunding(number, number_raund)

from math import pi
print(pi)
my_raunding(str(pi), number_raund=4)



