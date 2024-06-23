import pymysql


conn = pymysql.connect(
    host='sql8.freesqldatabase.com',
    database='sql8715658',
    user='sql8715658',
    password='T1GB4DABb2',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
    
)

cursor = conn.cursor()

sql_query = """ CREATE TABLE users(
    id integer  PRIMARY KEY AUTO_INCREMENT,
    userName text NOT NULL,
    email text NOT NULL,
    paswd text NOT NULL
)"""

cursor.execute(sql_query)
conn.close()