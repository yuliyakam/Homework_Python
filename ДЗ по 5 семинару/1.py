#№1 Программа извлекает из текста все слова, содержащие "абв"

list_text = ['ПРИВЕТ', 'ЗАБВЕНИЕ', 'ПОКА']
s = 'абв'
#           Через  filter
spisok = list(filter(lambda i: s not in i.lower(), list_text))
#           Через списочное выражение
list1 = [i for i in list_text if s not in i.lower()]

print(spisok)
print(list1)