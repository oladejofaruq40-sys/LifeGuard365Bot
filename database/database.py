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

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS user_progress (
                user_id INTEGER PRIMARY KEY,
                current_streak INTEGER NOT NULL DEFAULT 0,
                longest_streak INTEGER NOT NULL DEFAULT 0,
                quiz_completed INTEGER NOT NULL DEFAULT 0,
                quiz_correct INTEGER NOT NULL DEFAULT 0,
                tips_viewed INTEGER NOT NULL DEFAULT 0,
                last_activity_date TEXT DEFAULT NULL,
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

# ============================================================
# USER PROGRESS
# ============================================================

def get_or_create_progress(user_id: int):
    """Return a user's progress, creating it if necessary."""

    now = datetime.now(timezone.utc).isoformat()

    connection = get_connection()

    try:
        connection.execute(
            """
            INSERT INTO user_progress (
                user_id,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?)
            ON CONFLICT(user_id) DO NOTHING
            """,
            (user_id, now, now),
        )

        connection.commit()

        cursor = connection.execute(
            """
            SELECT *
            FROM user_progress
            WHERE user_id = ?
            """,
            (user_id,),
        )

        row = cursor.fetchone()

        return dict(row) if row else None

    finally:
        connection.close()


def record_activity(user_id: int):
    """
    Record daily user activity and update the safety streak.

    Returns the updated progress record.
    """

    today = datetime.now(timezone.utc).date()

    progress = get_or_create_progress(user_id)

    last_activity = progress["last_activity_date"]

    connection = get_connection()

    try:
        current_streak = progress["current_streak"]
        longest_streak = progress["longest_streak"]

        if last_activity is None:
            current_streak = 1

        else:
            last_date = datetime.fromisoformat(last_activity).date()

            difference = (today - last_date).days

            if difference == 0:
                # Already recorded activity today.
                current_streak = max(current_streak, 1)

            elif difference == 1:
                # Consecutive day.
                current_streak += 1

            else:
                # Streak has been broken.
                current_streak = 1

        longest_streak = max(
            longest_streak,
            current_streak,
        )

        now = datetime.now(timezone.utc).isoformat()

        connection.execute(
            """
            UPDATE user_progress
            SET
                current_streak = ?,
                longest_streak = ?,
                last_activity_date = ?,
                updated_at = ?
            WHERE user_id = ?
            """,
            (
                current_streak,
                longest_streak,
                today.isoformat(),
                now,
                user_id,
            ),
        )

        connection.commit()

        return get_or_create_progress(user_id)

    finally:
        connection.close()


def record_tip_view(user_id: int):
    """Record that a user viewed a safety tip."""

    record_activity(user_id)

    connection = get_connection()

    try:
        connection.execute(
            """
            UPDATE user_progress
            SET
                tips_viewed = tips_viewed + 1,
                updated_at = ?
            WHERE user_id = ?
            """,
            (
                datetime.now(timezone.utc).isoformat(),
                user_id,
            ),
        )

        connection.commit()

    finally:
        connection.close()


def record_quiz_result(
    user_id: int,
    correct_answers: int,
):
    """Record a completed quiz and its correct answers."""

    record_activity(user_id)

    connection = get_connection()

    try:
        connection.execute(
            """
            UPDATE user_progress
            SET
                quiz_completed = quiz_completed + 1,
                quiz_correct = quiz_correct + ?,
                updated_at = ?
            WHERE user_id = ?
            """,
            (
                correct_answers,
                datetime.now(timezone.utc).isoformat(),
                user_id,
            ),
        )

        connection.commit()

    finally:
        connection.close()


def get_user_progress(user_id: int):
    """Return a user's progress information."""

    progress = get_or_create_progress(user_id)

    return progress
