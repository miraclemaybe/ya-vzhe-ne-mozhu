import sqlite3

def script(file):
    try:
        sqlite_connection = sqlite3.connect("menu.db")
        cursor = sqlite_connection.cursor()

        with open(file, 'r') as file:
            script = file.read()
        
        cursor.executescript(script)    
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        return error
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def select_menu(category):
    try:
        sqlite_connection = sqlite3.connect("menu.db")
        cursor = sqlite_connection.cursor()

        select_query = 'SELECT id, product_name, price FROM menu WHERE category = ?'

        cursor.execute(select_query, (category,))
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        return error
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def select_product(category, id):
    try:
        sqlite_connection = sqlite3.connect("menu.db")
        cursor = sqlite_connection.cursor()

        select_query = '''SELECT product_name, price FROM menu WHERE id = ? AND category = ?'''

        cursor.execute(select_query, (id, category))
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        return error
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def select_reviews():
    try:
        sqlite_connection = sqlite3.connect("menu.db")
        cursor = sqlite_connection.cursor()

        select_query = 'SELECT author_review, review FROM reviews'

        cursor.execute(select_query)
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        return error
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def createTable():
    try:
        sqlite_connection = sqlite3.connect("menu.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")

        create_table_query = '''CREATE TABLE IF NOT EXISTS reviews(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                author_review VARCHAR(255) NOT NULL,
                                review VARCHAR(255) NOT NULL
                                );'''
        cursor.execute(create_table_query)
        sqlite_connection.commit()
        print("Таблица создана успешно.")
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")  



# ("japanese friend", "すしがらくた https://www.youtube.com/watch?v=BleYAt1PrhA"),
# ("Anomin", "thay don`t recognized me 10\10"),
# ("Vikusya_2009(beer enjoyer)", "where`s cherry beer? 9\10");

def insertData(id, name):
    try:
        sqlite_connection = sqlite3.connect("menu.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")

        data_tuple = (id, name)
        insert_data_query = '''INSERT INTO reviews (author_review, review)
                               VALUES (?, ?);'''
        cursor.execute(insert_data_query, data_tuple)
        sqlite_connection.commit()
        print("Запись успешно добавлена.")
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")   



