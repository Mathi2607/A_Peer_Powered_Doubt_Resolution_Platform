from utils.db import get_db

def save_message(sender,receiver,message):

    conn = get_db()

    conn.execute("""
    INSERT INTO chats(sender,receiver,message)
    VALUES(?,?,?)
    """,(sender,receiver,message))

    conn.commit()
    conn.close()


def get_messages(user1,user2):

    conn = get_db()

    msgs = conn.execute("""
    SELECT * FROM chats
    WHERE (sender=? AND receiver=?)
    OR (sender=? AND receiver=?)
    """,(user1,user2,user2,user1)).fetchall()

    conn.close()

    return msgs

from utils.db import get_db

def get_chat_users(username):

    conn = get_db()

    users = conn.execute("""

    SELECT DISTINCT
    CASE
        WHEN sender=? THEN receiver
        ELSE sender
    END as chat_user

    FROM chats

    WHERE sender=? OR receiver=?

    """,(username,username,username)).fetchall()

    conn.close()

    return users