import sqlite3

conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM leave_requests")

conn.commit()
conn.close()

print("Leave records cleared.")