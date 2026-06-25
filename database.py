import sqlite3

conn = sqlite3.connect("employee.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    department TEXT,
    designation TEXT,
    joining_date TEXT,
    salary REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emp_id INTEGER,
    date TEXT,
    status TEXT,
    FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS salary(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emp_id INTEGER,
    basic_salary REAL,
    tax REAL,
    pf REAL,
    net_salary REAL,
    month TEXT,
    FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")