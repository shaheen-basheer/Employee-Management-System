from database import get_connection
import pandas as pd


# ----------------------------------------
# Generate Salary
# ----------------------------------------

def generate_salary(
    emp_id,
    basic_salary,
    bonus,
    tax,
    pf,
    month
):

    net_salary = basic_salary + bonus - tax - pf

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO salary
        (
            emp_id,
            basic_salary,
            tax,
            pf,
            net_salary,
            month
        )
        VALUES (?,?,?,?,?,?)
        """,
        (
            emp_id,
            basic_salary,
            tax,
            pf,
            net_salary,
            month
        )
    )

    conn.commit()
    conn.close()


# ----------------------------------------
# Salary History
# ----------------------------------------

def get_salary_history():

    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT

            salary.id,
            employees.emp_id,
            employees.name,
            salary.month,
            salary.basic_salary,
            salary.tax,
            salary.pf,
            salary.net_salary

        FROM salary

        JOIN employees

        ON salary.emp_id = employees.emp_id

        ORDER BY salary.month DESC
        """,
        conn
    )

    conn.close()

    return df


# ----------------------------------------
# Salary Slip
# ----------------------------------------

def get_salary_slip(emp_id, month):

    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT

            employees.name,
            employees.department,
            employees.designation,

            salary.month,
            salary.basic_salary,
            salary.tax,
            salary.pf,
            salary.net_salary

        FROM salary

        JOIN employees

        ON salary.emp_id = employees.emp_id

        WHERE salary.emp_id=? AND salary.month=?
        """,
        conn,
        params=(emp_id, month)
    )

    conn.close()

    return df


# ----------------------------------------
# Salary Raise Tracking
# ----------------------------------------

def get_salary_raise_history(emp_id):

    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT

            month,
            basic_salary,
            tax,
            pf,
            net_salary

        FROM salary

        WHERE emp_id=?

        ORDER BY id
        """,
        conn,
        params=(emp_id,)
    )

    conn.close()

    return df