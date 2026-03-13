from utils.db import get_db

def create_user(username,email,phone,education,skill,password):
    conn = get_db()
    conn.execute("""
    INSERT INTO users (username,email,phone,education,skill,password)
    VALUES (?,?,?,?,?,?)
    """,(username,email,phone,education,skill,password))
    conn.commit()
    conn.close()

def get_user(username,password):
    conn = get_db()
    user = conn.execute("""
    SELECT * FROM users WHERE username=? AND password=?
    """,(username,password)).fetchone()
    conn.close()
    return user

def get_all_users():
    conn = get_db()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return users

def search_users(skill):
    conn = get_db()
    users = conn.execute("""
    SELECT * FROM users WHERE skill LIKE ?
    """,('%'+skill+'%',)).fetchall()
    conn.close()
    return users

from utils.db import get_db

def get_user_by_username(username):

    conn = get_db()

    user = conn.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    ).fetchone()

    conn.close()

    return user