import streamlit as st
from datetime import date

from employee import get_all_employees

from attendance import (
    mark_attendance,
    attendance_exists
)


def show_attendance():

    st.header("📝 Mark Attendance")

    employees = get_all_employees()

    if employees.empty:
        st.warning("No employees found.")
        return

    # Create display list like: "1 - Rahul"
    employees["display"] = employees.apply(
        lambda row: f"{int(row['emp_id'])} - {row['name']}",
        axis=1
    )

    selected_display = st.selectbox(
        "Select Employee",
        employees["display"]
    )

    selected_employee = employees[
        employees["display"] == selected_display
    ].iloc[0]

    # IMPORTANT: Convert NumPy int to normal Python int
    emp_id = int(selected_employee["emp_id"])

    attendance_date = st.date_input(
        "Select Date",
        value=date.today()
    )

    status = st.selectbox(
        "Attendance Status",
        [
            "Present",
            "Absent",
            "Half-Day"
        ]
    )

    if st.button("Save Attendance"):

        if attendance_exists(
            emp_id,
            str(attendance_date)
        ):

            st.error(
                "Attendance already marked for this employee on this date."
            )

        else:

            mark_attendance(
                emp_id,
                str(attendance_date),
                status
            )

            st.success(
                "✅ Attendance Saved Successfully!"
            )