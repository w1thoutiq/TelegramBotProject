import sqlite3

"""Здесь я надеюсь все ясно"""

con = sqlite3.connect('TelegramBase.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS telegram (
    line INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id BIGINT UNIQUE NOT NULL,
    username text);''')

con.commit()