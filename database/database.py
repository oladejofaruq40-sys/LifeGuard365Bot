import sqlite3
from datetime import datetime

DATABASE_NAME = "lifeguard365.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            user_id INTEGER PRIMARY KEY,
            first_name TEXT,
            username TEXT,
            subscribed INTEGER DEFAULT 1,
            created_at TEXT,
            updated_at TEXT
        )
    """)

    connection.commit()
    connection.close()


def add_subscriber(user_id, first_name="", username=""):
    connection = get_connection()
    now = datetime.utcnow().isoformat()

    connection.execute("""
        INSERT INTO subscribers (
            user_id,
            first_name,
            username,
            subscribed,
            created_at,
            updated_at
        )
        VALUES (?, ?, ?, 1, ?, ?)
        ON CONFLICT(user_id)
        DO UPDATE SET
            first_name = excluded.first_name,
            username = excluded.username,
            subscribed = 1,
            updated_at = excluded.updated_at
    """, (
        user_id,
        first_name,
        username,
        now,
        now
    ))

    connection.commit()
    connection.close()


def remove_subscriber(user_id):
    connection = get_connection()

    connection.execute("""
        UPDATE subscribers
        SET subscribed = 0,
            updated_at = ?
        WHERE user_id = ?
    """, (
        datetime.utcnow().isoformat(),
        user_id
    ))

    connection.commit()
    connection.close()


def get_subscribers():
    connection = get_connection()

    cursor = connection.execute("""
        SELECT user_id
        FROM subscribers
        WHERE subscribed = 1
    """)

    subscribers = [row["user_id"] for row in cursor.fetchall()]

    connection.close()

    return subscribers


def get_subscriber_count():
    connection = get_connection()

    cursor = connection.execute("""
        SELECT COUNT(*) AS total
        FROM subscribers
        WHERE subscribed = 1
    """)

    count = cursor.fetchone()["total"]

    connection.close()

    return count