from database import connect_db

def get_all_expenses():
  conn = connect_db()
  cursor = conn.cursor()

  cursor.execute("SELECT * FROM expenses")

  rows= cursor.fetchall()
  conn.close()

  return rows