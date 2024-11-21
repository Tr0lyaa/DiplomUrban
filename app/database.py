import sqlite3

data1 = [["Зима", 22000], ["Весна", 35000], ["Лето", 20000], ["Осень", 16000]]
data2 = [["Понедельник", 120], ["Вторник", 445], ["Среда", 105], ["Четверг", 400], ["Пятница", 140]]

connection = sqlite3.connect("data/data.db")
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Data_1(
    id INTEGER PRIMARY KEY,
    season TEXT NOT NULL,
    money INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Data_2(
    id INTEGER PRIMARY KEY,
    day TEXT NOT NULL,
    sales INTEGER,
    worker TEXT
    )
    ''')

    connection.commit()


initiate_db()


def create_data1():
    for i in range(4):
        cursor.execute("INSERT INTO Data_1 (season, money) VALUES (?, ?)",
                       (data1[i][0], data1[i][1]))
    connection.commit()


def create_data2():
    for i in range(5):
        cursor.execute("INSERT INTO Data_2 (day, sales, worker) VALUES (?, ?, ?)",
                       (data2[i][0], data2[i][1], "Работник 1" if i % 2 == 0 else "Работник 2"))
    connection.commit()


def get_all_data(data):
    all_data = cursor.execute(f"SELECT * FROM {data}").fetchall()
    connection.commit()
    return all_data
