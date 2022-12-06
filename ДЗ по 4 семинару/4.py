# №4 Записать в файл многочлен заданной степени с рандомными коэффициентами

import random

k = int(input("Введите степень многочлена "))
exponent_list = []
coefficient_list = []

for i in range(k, 0, -1):
    exponent_list.append(i)

for i in range(k):
    coefficient_list.append(random.randint(0, 100)) 

with open('file.txt', 'w') as data:
    data.write('')

with open('file.txt', 'w') as data:
    for i in range(k):
        data.write(str(coefficient_list[i])+'x'+'^'+str(exponent_list[i])+'+')
    data.write(str(random.randint(0, 100))+' = 0')
