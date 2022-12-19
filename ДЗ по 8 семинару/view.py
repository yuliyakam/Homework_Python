def show_menu():
    print("Выберите команду:\n1 - показать всех сотрудников\n2 - добавить сотрудника\n3 - изменить данные сотрудника"
          "\n4 - удалить сотрудника\n5 - экспорт в txt\n6 - импорт из txt\n7 - импорт из csv")
    try:
        select = int(input())
        if not select in [1, 2, 3, 4, 5, 6, 7]:
            raise ValueError
        return select
    except Exception:
        print("Error")
        exit()

def show_employes(spisok):
    print("Список всех сотрудников")
    for i, sotrudnik in enumerate(spisok):
        if i == 0:
            print(' ', *sotrudnik)
        else:
            print(i, *sotrudnik)

def add_emloyes():
    print("Введите Фамилию Имя Телефон и Должность через пробел: ")
    data = input().split()
    return data

def update_emploey():
    change = int(input("Введите номер строки для перезаписи и нажмите Enter: "))
    string = input("Введите строку, которую хотите записать. Порядок полей:\n"
                   "Фамилию Имя Телефон Должность (разделитель между полями - пробел)")
    return change, string

def delete():
    print("Введие номер строки для удаления ")
    number = int(input())
    return number