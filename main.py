from database import create_expenses_table
from reports import get_all_expenses

create_expenses_table()
print(get_all_expenses())