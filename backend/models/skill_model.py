from utils.db import get_db

def add_skill(skill):

    conn = get_db()

    conn.execute("""
    INSERT INTO skills(skill_name)
    VALUES(?)
    """,(skill,))

    conn.commit()
    conn.close()


def get_skills():

    conn = get_db()

    skills = conn.execute("""
    SELECT * FROM skills
    """).fetchall()

    conn.close()

    return skills


def delete_skill(skill_id):

    conn = get_db()

    conn.execute("""
    DELETE FROM skills
    WHERE id=?
    """,(skill_id,))

    conn.commit()
    conn.close()