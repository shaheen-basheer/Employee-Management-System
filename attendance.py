from database import get_connection
import pandas as pd


# ---------------------------------
# Check Attendance Exists
# ---------------------------------

def attendance_exists(emp_id, date):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM attendance
        WHERE emp_id=? AND date=?
        """,
        (emp_id, date)
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None


# ---------------------------------
# Mark Attendance
# ---------------------------------

def mark_attendance(emp_id, date, status):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO attendance
        (emp_id, date, status)
        VALUES (?,?,?)
        """,
        (emp_id, date, status)
    )

    conn.commit()
    conn.close()


# ---------------------------------
# Get Attendance
# ---------------------------------

def get_all_attendance():

    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT

            attendance.id,
            employees.emp_id,
            employees.name,
            attendance.date,
            attendance.status

        FROM attendance

        JOIN employees

        ON attendance.emp_id = employees.emp_id

        ORDER BY attendance.date DESC
        """,
        conn
    )

    conn.close()

    return df


# ---------------------------------
# Monthly Attendance Report
# ---------------------------------

def calculate_monthly_attendance():

    df = get_all_attendance()

    if df.empty:
        return pd.DataFrame()

    # Convert date column
    df["date"] = pd.to_datetime(df["date"])

    # Current Month
    current_month = pd.Timestamp.today().month
    current_year = pd.Timestamp.today().year

    df = df[
        (df["date"].dt.month == current_month) &
        (df["date"].dt.year == current_year)
    ]

    if df.empty:
        return pd.DataFrame()

    results = []

    for employee in df["name"].unique():

        emp_df = df[df["name"] == employee]

        working_days = len(emp_df)

        present = len(
            emp_df[
                emp_df["status"] == "Present"
            ]
        )

        half_day = len(
            emp_df[
                emp_df["status"] == "Half-Day"
            ]
        )

        absent = len(
            emp_df[
                emp_df["status"] == "Absent"
            ]
        )

        attendance_percentage = (
            (
                present +
                (half_day * 0.5)
            ) / working_days
        ) * 100

        results.append({

            "Employee": employee,

            "Working Days": working_days,

            "Present": present,

            "Absent": absent,

            "Half-Day": half_day,

            "Attendance %": round(
                attendance_percentage,
                2
            )

        })

    return pd.DataFrame(results)