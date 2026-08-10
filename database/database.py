from pathlib import Path
import sqlite3
from datetime import datetime, timezone


# Store the database in the project root.
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "lifeguard365.db"


def get_connection():
    """Create and return a SQLite database connection."""
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    """Create required database tables if they do not exist."""
    connection = get_connection()

    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS subscribers (
                user_id INTEGER PRIMARY KEY,
                first_name TEXT DEFAULT '',
                username TEXT DEFAULT '',
                subscribed INTEGER NOT NULL DEFAULT 1,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """
        )

        connection.commit()

    finally:
        connection.close()


def add_subscriber(
    user_id: int,
    first_name: str = "",
    username: str = "",
):
    """Add a subscriber or reactivate an existing subscriber."""
    now = datetime.now(timezone.utc).isoformat()

    connection = get_connection()

    try:
        connection.execute(
            """
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
            """,
            (
                user_id,
                first_name,
                username,
                now,
                now,
            ),
        )

        connection.commit()

    finally:
        connection.close()


def remove_subscriber(user_id: int):
    """Deactivate a subscriber without deleting their record."""
    now = datetime.now(timezone.utc).isoformat()

    connection = get_connection()

    try:
        connection.execute(
            """
            UPDATE subscribers
            SET subscribed = 0,
                updated_at = ?
            WHERE user_id = ?
            """,
            (now, user_id),
        )

        connection.commit()

    finally:
        connection.close()


def get_subscribers():
    """Return IDs of all currently active subscribers."""
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            SELECT user_id
            FROM subscribers
            WHERE subscribed = 1
            ORDER BY created_at ASC
            """
        )

        return [row["user_id"] for row in cursor.fetchall()]

    finally:
        connection.close()


def get_subscriber_count() -> int:
    """Return the number of active subscribers."""
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            SELECT COUNT(*) AS total
            FROM subscribers
            WHERE subscribed = 1
            """
        )

        return cursor.fetchone()["total"]

    finally:
        connection.close()