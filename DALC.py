import sqlite3 as sql
from Models import *

# USERS
conn =  sql.connect('./Data/Data.db')

conn.execute('''
    CREATE TABLE IF NOT EXISTS USERS (
	USER_ID integer PRIMARY KEY AUTOINCREMENT not null,
    NAME TEXT not null,
    EMAIL TEXT not null,
    PASSWORD TEXT not null,
    PHONE INTEGER null
);
''')

conn.close()


def addUser(user):
    conn =  sql.connect('./Data/Data.db')
    conn.execute(f"INSERT INTO USERS (NAME,EMAIL,PASSWORD,PHONE) VALUES('{user.name}' , '{user.email}' ,'{user.password}', {user.phone})")
    conn.commit()
    conn.close()

def getAllUsers():
    users = []
    conn =  sql.connect('./Data/Data.db')
    for row in conn.execute("SELECT * FROM USERS"):
        u = User()
        u.id = row[0]
        u.name = row[1]
        u.email = row[2]
        u.password = row[3]
        u.phone = row[4]
        users.append(u)
    
    conn.close()
    return users

def getUSerByID(id):
    conn =  sql.connect('./Data/Data.db')
    user = User()
    for row in conn.execute(f"SELECT * FROM USERS WHERE USER_ID = {id}"):
        user = User()
        user.id = row[0]
        user.name = row[1]
        user.email = row[2]
        user.password = row[3]
        user.phone = row[4]
    
    conn.close()
    return user

def editUser(user):
    conn = sql.connect("./Data/Data.db")
    conn.execute(f"UPDATE USERS SET NAME = '{user.name}', EMAIL = '{user.email}', PHONE = {user.phone} . PASSWORD = '{user.password}' WHERE USER_ID = {user.id};")
    conn.commit()
    conn.close()

def deleteUser(email,password):
    conn = sql.connect("./Data/Data.db")
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM USERS WHERE EMAIL = ? AND PASSWORD = ?",(email,password))
    conn.commit()
    conn.close() 



# Books


def connection():
    connection = sql.connect("./Data/Data.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS BOOK(
                    BOOK_ID INTEGER PRIMARY KEY ,
                    TITLE TEXT,
                    AUTHOR TEXT,
                    YEAR INTEGER,
                    ISBN integer)''')
    connection.commit()
    connection.close()

def insertBook(title, author, year, isbn):
    connection = sql.connect("./Data/Data.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO BOOK VALUES (null, ?, ?, ?, ?)", (title, author, year, isbn))
    connection.commit()
    connection.close()


def deleteBook(ID):
    connection = sql.connect("./Data/Data.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM BOOK WHERE BOOK_ID = ?", (ID ))
    connection.commit()
    connection.close()

def update(ID, title, author, year, isbn):
    connection = sql.connect("./Data/Data.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE BOOK SET TITLE = ?, AUTHOR = ?, YEAR = ?, ISBN = ? WHERE BOOK_ID = ?", (title, author, year, isbn , ID))
    connection.commit()
    connection.close()

def viewBooks():
    connection = sql.connect("./Data/Data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM BOOK")
    rows = cursor.fetchall()
    connection.close()
    return rows
connection() 