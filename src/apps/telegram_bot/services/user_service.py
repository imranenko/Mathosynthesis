import sqlite3
import os
from pathlib import Path

# Database path: src/apps/telegram_bot/services/user_service.py
# Root is 5 levels up: services <- telegram_bot <- apps <- src <- project_root
DB_FILE = Path(__file__).resolve().parent.parent.parent.parent.parent / "data" / "users.db"

def init_db():
    """Create the users table if it doesn't exist."""
    os.makedirs(DB_FILE.parent, exist_ok=True)
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                file_lang TEXT DEFAULT 'en',
                ui_lang TEXT DEFAULT 'en'
            )
        """)

def get_user_settings(user_id):
    """Retrieve settings for a specific user ID."""
    init_db()
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.execute(
            "SELECT file_lang, ui_lang FROM users WHERE user_id = ?",
            (user_id,)
        )
        row = cursor.fetchone()
        if row:
            return {"file_lang": row[0], "ui_lang": row[1]}
    return {"file_lang": "en", "ui_lang": "en"}

def update_user_settings(user_id, **kwargs):
    """
    Update user settings in the database.
    Supported kwargs: file_lang, interface_lang.
    """
    init_db()
    if not kwargs:
        return

    allowed_keys = ["file_lang", "ui_lang"]
    set_clauses = []
    values = []
    
    for key, value in kwargs.items():
        if key in allowed_keys:
            set_clauses.append(f"{key} = ?")
            values.append(value)
    
    if not set_clauses:
        return

    # UPSERT pattern for SQLite 3.24+
    set_stmt = ", ".join(set_clauses)
    query = f"""
        INSERT INTO users (user_id, {", ".join(kwargs.keys())})
        VALUES (?, {", ".join(["?"] * len(kwargs))})
        ON CONFLICT(user_id) DO UPDATE SET {set_stmt}
    """
    
    upsert_values = [user_id] + list(kwargs.values()) + values
    
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute(query, upsert_values)