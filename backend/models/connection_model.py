from utils.db import get_db


def send_request(user1, user2, request_type):
    conn = get_db()

    conn.execute("""
    INSERT INTO connections(user1, user2, status, request_type)
    VALUES (?, ?, ?,?)
    """, (user1, user2, "pending", request_type))

    conn.commit()
    conn.close()


def get_request_status(user1,user2):

    conn=get_db()

    status=conn.execute("""
    SELECT * FROM connections
    WHERE user1=? AND user2=?
    """,(user1,user2)).fetchone()

    conn.close()

    return status

def get_received_requests(username):

    conn=get_db()

    requests=conn.execute("""
    SELECT * FROM connections
    WHERE user2=? AND status='pending'
    """,(username,)).fetchall()

    conn.close()

    return requests


def accept_request(request_id):
    conn = get_db()

    req = conn.execute("""
    SELECT * FROM connections WHERE id=?
    """,(request_id,)).fetchone()

    conn.execute("""
    UPDATE connections
    SET status='accepted'
    WHERE id=?
    """, (request_id,))

    conn.commit()
    conn.close()

    return req


def reject_request(request_id):
    conn = get_db()

    req = conn.execute("""
    SELECT * FROM connections WHERE id=?
    """,(request_id,)).fetchone()

    conn.execute("""
    UPDATE connections
    SET status='rejected'
    WHERE id=?
    """, (request_id,))

    conn.commit()
    conn.close()

    return req


def is_connected(user1,user2):

    conn=get_db()

    connection=conn.execute("""
    SELECT * FROM connections
    WHERE ((user1=? AND user2=?)
    OR (user1=? AND user2=?))
    AND status='accepted'
    """,(user1,user2,user2,user1)).fetchone()

    conn.close()

    return connection

def get_requested_mentors(username):

    conn = get_db()

    mentors = conn.execute("""
    SELECT * FROM connections
    WHERE user1=?
    """,(username,)).fetchall()

    conn.close()

    return mentors