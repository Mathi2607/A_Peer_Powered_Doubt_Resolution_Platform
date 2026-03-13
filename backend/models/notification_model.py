from utils.db import get_db


def create_notification(sender, receiver, message):

    conn = get_db()

    conn.execute("""
    INSERT INTO notifications(sender,receiver,message,status)
    VALUES(?,?,?,?)
    """,(sender,receiver,message,"unread"))

    conn.commit()
    conn.close()



def get_notifications(user):

    conn = get_db()

    notes = conn.execute("""
    SELECT * FROM notifications
    WHERE receiver=? AND status='unread'
    """,(user,)).fetchall()

    conn.close()

    return notes



def mark_as_read(note_id):

    conn = get_db()

    conn.execute("""
    UPDATE notifications
    SET status='read'
    WHERE id=?
    """,(note_id,))

    conn.commit()
    conn.close()