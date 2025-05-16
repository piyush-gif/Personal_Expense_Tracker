from database import connect_db


def add_expense (date, amount, category, description):
  conn = connect_db()
  cursor = conn.cursor()

  cursor.execute ("""
  INSERT INTO expenses (date, amount, category, description)
  VALUES (?, ?, ?, ?)
  """,(date, amount, category, description))

  conn.commit()
  conn.close()


add_expense("2025-05-16", 12.50, "Food", "Lunch at cafe")
add_expense("2025-05-16", 12.12, "Sport", "Bought a BasketBall")