# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример:
# Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('file1.txt', 'w') as data:
    data.write('')

with open('file1.txt', 'w') as data:
    data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

with open('file1.txt', 'r') as data:
    line1 = data.readline()

with open('file2.txt', 'w') as data:
    data.write('')

count1 = 1

with open('file2.txt', 'a') as data:
    for i in range(1, len(line1)):
        if line1[i] == line1[i - 1]:
            count1 += 1
        else:
            data.write(str(count1) + line1[i - 1])
            count1 = 1
with open('file2.txt', 'a') as data:
    data.write(str(count1) + line1[- 1])

with open("file2.txt", "r") as data:
    line2 = data.readline()

with open('file.txt', 'w') as data:
    data.write('')

count_num = ''
with open('file.txt', 'a') as data:
    for i in range(len(line2)):
        if line2[i].isdigit():
            count_num += line2[i]
        else:
            for j in range(int(count_num)):
                data.write(line2[i])
            count_num = ''
