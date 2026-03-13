from utils.db import get_db

def get_videos(skill):

    conn = get_db()

    videos = conn.execute("""
    SELECT * FROM skills
    WHERE skill_name LIKE ?
    """,('%'+skill+'%',)).fetchall()

    conn.close()

    return videos