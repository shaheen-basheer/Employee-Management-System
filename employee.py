from database import get_connection
import pandas as pd


def add_employee(name, age, gender, department, designation, joining_date, salary):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO employees
    (name, age, gender, department, designation, joining_date, salary)
    VALUES (?,?,?,?,?,?,?)
    """,
    (name, age, gender, department, designation, joining_date, salary))

    conn.commit()
    conn.close()


def get_all_employees():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM employees ORDER BY emp_id",
        conn
    )

    conn.close()

    return df


def get_employee(emp_id):

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM employees WHERE emp_id=?",
        conn,
        params=(emp_id,)
    )

    conn.close()

    return df


def update_employee(emp_id, name, age, gender, department,
                    designation, joining_date, salary):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE employees
    SET
        name=?,
        age=?,
        gender=?,
        department=?,
        designation=?,
        joining_date=?,
        salary=?
    WHERE emp_id=?
    """,
    (
        name,
        age,
        gender,
        department,
        designation,
        joining_date,
        salary,
        emp_id
    ))

    conn.commit()
    conn.close()


# -------------------------
# NEW FUNCTION
# -------------------------

def delete_employee(emp_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE emp_id=?",
        (emp_id,)
    )

    conn.commit()
    conn.close()