import sqlite3


connection = sqlite3.connect("users_db.sqlite")

cursor = connection.cursor()

sql_query = """ CREATE TABLE users(
    id integer  PRIMARY KEY AUTOINCREMENT,
    userName text NOT NULL,
    email text NOT NULL,
    paswd text NOT NULL
)"""

cursor.execute(sql_query)