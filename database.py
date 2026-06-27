import sqlite3


DATABASE_NAME = "employee.db"


def get_connection():
    """
    Creates and returns a connection to the SQLite database.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
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


if __name__ == "__main__":
    create_tables()
    print("Database Ready")