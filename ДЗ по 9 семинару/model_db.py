import sqlite3


def connect():
    global conn, cursor
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()


def disconnect():
    conn.commit()
    conn.close()


def all(update, context):
    cursor.execute("select * from abonents")
    results = cursor.fetchall()
    update.message.reply_text(''.join([str(element) for element in results]))


def find_abonent(update, context):
    fl = 0
    name = update.message.text
    if name != name.title():
        update.message.reply_text('Введите фамилию с заглавной буквы!')
        name = update.message.text
    elif name == name.title():
        cursor.execute(f"select first_name from abonents")
        results = cursor.fetchall()
        for elements in results:
            if name in elements:
                cursor.execute(f"select * from abonents where first_name like '%{name}%'")
                result = cursor.fetchall()
                fl = 1
                update.message.reply_text(''.join([str(element) for element in result]))
    if fl == 0:
        update.message.reply_text("Контакт не найден")


def add_abonent(update, context):
    flag = 0
    first_name, name, phone = update.message.text.split()
    cursor.execute("select * from abonents")
    results = cursor.fetchall()
    for el in results:
        if int(phone) in el:
            update.message.reply_text("Такой номер уже существует!")
            flag = 1
            break
    if flag != 1:
        cursor.execute(
            f"insert into abonents (first_name, name, phone) "
            f"values ('{first_name}', '{name}', {phone})")
        update.message.reply_text("Контакт добавлен")


def update_info(update, context):
    sername, phone = update.message.text.split()
    cursor.execute(
        f"update abonents set phone={phone} where first_name='{sername}'"
    )
    update.message.reply_text("Изменения внесены")


def delete_abonent(update, context):
    first_name = update.message.text
    cursor.execute(
        f"delete from abonents where first_name='{first_name}'"
    )
    update.message.reply_text("Контакт удален")

