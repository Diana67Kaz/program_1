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

def delete_user(cursor, ID):
    command = """
    DELETE FROM user WHERE ID= ?
    """
    cursor.execute(command, (ID,))

def delete_user_2(cursor):
    command = """
    DELETE FROM user
    """
    cursor.execute(command)

def get_gender(cursor, gender):
    command = """
    SELECT * FROM user WHERE gender = ?
    """
    result = cursor.execute(command, (gender,))
    print(list(result))

with sqlite3.connect('data.db') as cursor:
    create_table_user(cursor)
    add_user(cursor, user('Иван', 'Иванов', 'male'))
    add_user(cursor, user('Анна', 'Петрова', 'female'))
    get_gender(cursor, 'male')
    #delete_user_2(cursor)


