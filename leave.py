from database import get_connection
import pandas as pd
from datetime import datetime


# ----------------------------------------
# Apply Leave
# ----------------------------------------

def apply_leave(
    emp_id,
    leave_type,
    start_date,
    end_date,
    reason
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO leave_requests
        (
            emp_id,
            leave_type,
            start_date,
            end_date,
            reason,
            applied_on
        )
        VALUES (?,?,?,?,?,?)
        """,
        (
            emp_id,
            leave_type,
            start_date,
            end_date,
            reason,
            str(datetime.today().date())
        )
    )

    conn.commit()
    conn.close()


# ----------------------------------------
# Pending Leave Requests
# ----------------------------------------

def get_pending_leaves():

    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT

            leave_requests.id,
            employees.name,
            employees.department,
            leave_requests.leave_type,
            leave_requests.start_date,
            leave_requests.end_date,
            leave_requests.reason,
            leave_requests.status

        FROM leave_requests

        JOIN employees

        ON leave_requests.emp_id = employees.emp_id

        WHERE status='Pending'

        ORDER BY start_date
        """,
        conn
    )

    conn.close()

    return df


# ----------------------------------------
# Approve Leave
# ----------------------------------------

def approve_leave(request_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE leave_requests

        SET status='Approved'

        WHERE id=?
        """,
        (request_id,)
    )

    conn.commit()
    conn.close()


# ----------------------------------------
# Reject Leave
# ----------------------------------------

def reject_leave(request_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE leave_requests

        SET status='Rejected'

        WHERE id=?
        """,
        (request_id,)
    )

    conn.commit()
    conn.close()


# ----------------------------------------
# Leave History
# ----------------------------------------

def get_leave_history():

    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT

            leave_requests.id,
            employees.name,
            employees.department,
            leave_requests.leave_type,
            leave_requests.start_date,
            leave_requests.end_date,
            leave_requests.reason,
            leave_requests.status,
            leave_requests.applied_on

        FROM leave_requests

        JOIN employees

        ON leave_requests.emp_id = employees.emp_id

        ORDER BY leave_requests.start_date DESC
        """,
        conn
    )

    conn.close()

    return df


# ----------------------------------------
# Leave Statistics
# ----------------------------------------

def get_leave_statistics():

    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT

            status,
            COUNT(*) as Count

        FROM leave_requests

        GROUP BY status
        """,
        conn
    )

    conn.close()

    return df


# ----------------------------------------
# Department Leave Count
# ----------------------------------------

def get_department_leave_count():

    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT

            employees.department,
            COUNT(*) as Leaves

        FROM leave_requests

        JOIN employees

        ON leave_requests.emp_id = employees.emp_id

        GROUP BY employees.department
        """,
        conn
    )

    conn.close()

    return df