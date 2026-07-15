import sqlite3

DATABASE = "lexflow.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def init_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        document_type TEXT,
        name TEXT,
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    connection.commit()
    connection.close()
