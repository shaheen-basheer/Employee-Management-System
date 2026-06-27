import pandas as pd
from database import get_connection

conn = get_connection()

df = pd.read_sql_query(
    "SELECT * FROM employees",
    conn
)

print(df)

conn.close()