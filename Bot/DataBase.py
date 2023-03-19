import sqlite3

con = sqlite3.connect('TelegramBase.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS telegram (
    line INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id BIGINT UNIQUE NOT NULL,
    username text);''')


def input_on_bd(user_id, username):
    cur.execute(f"INSERT INTO telegram (user_id, username) VALUES"
                f"('{user_id}', '{username}')")
    con.commit()


con.commit()
