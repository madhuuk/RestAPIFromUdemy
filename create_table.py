import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,username text,password text)"

create_table1 = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY,name text,price INTEGER)"

cur.execute(create_table)

cur.execute(create_table1)

conn.commit()

conn.close()