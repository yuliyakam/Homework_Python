#№1 Программа принимает цифру, обозначающую день недели и выдает, является ли этот день выходным
def day_of_week(days_number):
    list = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    if days_number == 5 or days_number == 6:
        print(list[days_number]," - это выходной день")
    if days_number>=0 and days_number<=4:
        print(list[days_number]," - это не выходной день")
    else:
        print("Такого дня недели не существует")

print("Введите номер дня недели, где 0 это Понедельник\n")
days_number = int(input())
day_of_week(days_number)