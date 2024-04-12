import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


def is_username_exist(username: str) -> bool:
    db = sqlite3.connect("./tracker.db", check_same_thread=False)
    cursor = db.cursor()

    search_sql = ''' SELECT username FROM users WHERE username = ?'''
    search_result = cursor.execute(search_sql, [username]).fetchall()

    db.close()

    if len(search_result) == 1:
        return True
    else:
        return False

def check_password(username: str, password: str) -> bool:
    db = sqlite3.connect("./tracker.db", check_same_thread=False)
    cursor = db.cursor()

    actual_password = cursor.execute("SELECT hash FROM users WHERE username = ?", [username]).fetchall()[0][0]
    db.close()

    if check_password_hash(actual_password, password):
        return True
    else:
        return False

def add_user(username: str, password: str) -> None:
    db = sqlite3.connect("./tracker.db", check_same_thread=False)
    cursor = db.cursor()

    encrypted_password = generate_password_hash(password)
    cursor.execute("INSERT INTO users (username, hash) VALUES(?, ?)",   
                   [username, encrypted_password])
    db.commit()

    db.close()


def get_user_id(username: str) -> str:
    db = sqlite3.connect("./tracker.db", check_same_thread=False)
    cursor = db.cursor()

    user_id = cursor.execute("SELECT id FROM users WHERE username = ?", [username]).fetchall()[0][0]
    db.close()
    return user_id

