import sqlite3
import pandas as pd

conn = sqlite3.connect("employee.db")

df = pd.read_sql_query(
    "SELECT * FROM leave_requests",
    conn
)

print(df)

conn.close()