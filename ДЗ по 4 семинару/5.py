# №5 Записать в файл многочлен, являющийся суммой двух многочленов, которые хранятся в двух файлах

import random
# Метод создает многочлен заданной степени и записывает его в указанный в параметрах файл
def generete_polinomial_function(file_name, exponenta):
       
    exponent_list = []
    coefficient_list = []
    line = ''

    for i in range(exponenta, 0, -1):
        exponent_list.append(i)

    for i in range(exponenta):
        coefficient_list.append(random.randint(0, 100)) 

    with open(file_name, 'w') as data:
        data.write('')

    with open(file_name, 'w') as data:
        for i in range(exponenta):
            data.write(str(coefficient_list[i])+'x'+'^'+str(exponent_list[i])+'+')
        data.write(str(random.randint(0, 100))+' = 0')
# Вводить имя файла можно и с клавиатуры, как и показатель степени
# file_name = input("Введите имя файла, в который запишется многочлен ")
# exponenta = int(input("Введите показатель степени многочлена "))

generete_polinomial_function(file_name = 'file1.txt', exponenta = 3) # Записываем в файл file1.txt первый многочлен
generete_polinomial_function(file_name = 'file2.txt', exponenta = 3) # Записываем в файл file2.txt второй многочлен

def extraction_coefficients(file_name, exponenta):
# Метод извлекает из файла коэффициенты и возвращает список из этих коэффициентов, преобразованных в числа
    list1 = [] 
    str1 = ''
    with open(file_name, 'r') as data:
        line = data.readline()
    line = line.split('+') 
    last_coefficient = line[len(line)-1]
    position = last_coefficient.find(' ')
    last_coefficient = last_coefficient[:position]    
    line = line[:exponenta]
    for i in line:
        for simbol in i:
            if simbol != 'x':
                str1 += simbol 
            else:
                break
        list1.append(str1)
        str1 = ''    

    coefficient_list = []
    for i in range(exponenta):
        coefficient_list.append(int(list1[i]))
    coefficient_list.append(int(last_coefficient))

    return coefficient_list
# Для наглядности распечатываю списки с коэффициентами первого, второга и результирующего третьего многочлена
coefficient_list1 = extraction_coefficients('file1.txt', 3)
coefficient_list2 = extraction_coefficients('file2.txt', 3)

print(coefficient_list1, end=' ')
print(coefficient_list2, end=' ')

coefficient_list3 = []
for i in range(len(coefficient_list1)):
    coefficient_list3.append(coefficient_list1[i] + coefficient_list2[i])
print(coefficient_list3, end=' ')
# Записываем в файл третий результирующий многочлен
with open('file3.txt', 'w') as data:
    data.write('')

with open('file3.txt', 'w') as data:
    for i in range(len(coefficient_list3)-1):
        data.write(str(coefficient_list3[i])+'x'+'^'+str(len(coefficient_list3)-1-i)+'+')
    data.write(str(coefficient_list3[len(coefficient_list3)-1])+' = 0')
