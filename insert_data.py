# insert_data.py

import sqlite3

conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

employees = [
("Rahul",25,"Male","IT","Developer","2024-01-10",45000),
("Anjali",24,"Female","HR","HR Executive","2024-02-15",40000),
("Vikram",28,"Male","Finance","Accountant","2023-11-20",50000),
("Priya",26,"Female","IT","Tester","2024-03-01",42000),
("Arjun",29,"Male","Sales","Manager","2023-12-05",55000)
]

cursor.executemany("""
INSERT INTO employees
(name,age,gender,department,designation,joining_date,salary)
VALUES (?,?,?,?,?,?,?)
""", employees)

conn.commit()
conn.close()

print("Dummy Data Inserted")