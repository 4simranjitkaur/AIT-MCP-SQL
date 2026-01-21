from app.db import get_connection
import psycopg2


def insert_user(name, email):
    conn = get_connection()
    if conn is None:
        print("No DB connection")
        return False

    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            (name, email)
        )
        conn.commit()
        print(f"User inserted: {email}")
        return True

    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        print(f"Email already exists: {email}")
        return False

    finally:
        cur.close()
        conn.close()


def get_all_users():
    conn = get_connection()
    if conn is None:
        print(" No DB connection")
        return []

    cur = conn.cursor()

    cur.execute("SELECT id, name, email FROM users")
    users = cur.fetchall()

    cur.close()
    conn.close()

    return users
