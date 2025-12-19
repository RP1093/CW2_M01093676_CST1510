import sqlite3

def create_user_table(conn):
    cur = conn.cursor()
    sql = '''CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    hash_password TEXT NOT NULL);
    '''
    cur.execute(sql)
    conn.commit()