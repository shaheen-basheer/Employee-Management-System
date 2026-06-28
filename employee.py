from database import get_connection
import pandas as pd


# -----------------------------
# Add Employee
# -----------------------------
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


# -----------------------------
# Get All Employees
# -----------------------------
def get_all_employees():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM employees ORDER BY emp_id",
        conn
    )

    conn.close()

    return df


# -----------------------------
# Get One Employee
# -----------------------------
def get_employee(emp_id):

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM employees WHERE emp_id=?",
        conn,
        params=(emp_id,)
    )

    conn.close()

    return df


# -----------------------------
# Update Employee
# -----------------------------
def update_employee(
    emp_id,
    name,
    age,
    gender,
    department,
    designation,
    joining_date,
    salary
):

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


# -----------------------------
# Delete Employee
# -----------------------------
def delete_employee(emp_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE emp_id=?",
        (emp_id,)
    )

    conn.commit()
    conn.close()


# -----------------------------
# Dashboard Statistics
# -----------------------------
def get_dashboard_stats():

    df = get_all_employees()

    if df.empty:
        return {
            "total": 0,
            "average_salary": 0,
            "departments": 0,
            "male": 0,
            "female": 0,
            "highest_salary": 0,
            "lowest_salary": 0
        }

    return {
        "total": len(df),
        "average_salary": int(df["salary"].mean()),
        "departments": df["department"].nunique(),
        "male": len(df[df["gender"] == "Male"]),
        "female": len(df[df["gender"] == "Female"]),
        "highest_salary": int(df["salary"].max()),
        "lowest_salary": int(df["salary"].min())
    }


# =====================================================
# DASHBOARD ANALYTICS
# =====================================================

# Department-wise Employee Count
def get_department_count():

    df = get_all_employees()

    if df.empty:
        return pd.DataFrame()

    return (
        df.groupby("department")
        .size()
        .reset_index(name="Employees")
    )


# Salary Distribution
def get_salary_distribution():

    df = get_all_employees()

    if df.empty:
        return pd.DataFrame()

    return df[["name", "salary"]]


# Gender Distribution
def get_gender_distribution():

    df = get_all_employees()

    if df.empty:
        return pd.DataFrame()

    return (
        df.groupby("gender")
        .size()
        .reset_index(name="Employees")
    )


# Department Salary Average
def get_department_salary():

    df = get_all_employees()

    if df.empty:
        return pd.DataFrame()

    return (
        df.groupby("department")["salary"]
        .mean()
        .reset_index()
    )