import sqlite3

def connect_db():
    """Connect to the SQLite database (or create it if it doesn't exist)."""
    conn = sqlite3.connect("expenses.db")
    return conn

def create_expenses_table():
  conn = connect_db()
  cursor = conn.cursor()

  cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      date TEXT NOT NULL,
      amount REAL NOT NULL,
      category TEXT NOT NULL,
      description TEXT
      )
      """)
  
  conn.commit()
  conn.close()