import sqlite3

conn = sqlite3.connect("employee.db")

cursor = conn.cursor()

cursor.execute("DELETE FROM attendance")

conn.commit()

conn.close()

print("Attendance table cleared successfully.")