import sqlite3

class user:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender

def create_table_user(cursor):
    command = """
    CREATE TABLE IF NOT EXISTS USER(
        ID INTEGER PRIMARY KEY,
        name TEXT,
        surname TEXT,
        gender TEXT)
    """
    cursor.execute(command)

def add_user(cursor, user):
    command = """
    INSERT INTO user(name, surname, gender)
    VALUES(?, ?, ?)
    """
    cursor.execute(command, (user.name, user.surname, user.gender))

def get_user_list(cursor):
    command="""
        SELECT * FROM user
    """
    result = cursor.execute(command)
    users=list(result)
    #users = result.fetchall() # перевести в более понятный формат
    print(users)

def update_user_name(cursor, value, user_id):
    command = """
        UPDATE user
        SET name = ?
        WHERE id = ?
    """
    cursor.execute(command, (value, user_id))

def delete_users(cursor):
    command = """
    DELETE FROM user
    """
    cursor.execute(command)

def get_user(cursor, name):
    command = """
        SELECT * FROM user  
        WHERE name = ?
    """
    result = cursor.execute(command, (name,))
    print(list(result))

with sqlite3.connect('data.db') as cursor:
    create_table_user(cursor)
    delete_users(cursor)
    add_user(cursor, user('Иван', 'Иванов', 'male'))
    add_user(cursor, user('Пётр', 'Петров', 'male'))

    get_user(cursor, 'Пётр')


    #get_user_list(cursor)
    #update_user_name(cursor, 'Никита', 1)
    #get_user_list(cursor)
    #delete_users(cursor)
    #get_user_list(cursor)
