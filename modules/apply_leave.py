import streamlit as st
from datetime import date

from employee import get_all_employees
from leave import apply_leave


def show_apply_leave():

    st.header("📝 Apply Leave")

    employees = get_all_employees()

    if employees.empty:
        st.warning("No employees available.")
        return

    # Create display text
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

    # IMPORTANT: Convert NumPy int to Python int
    emp_id = int(selected_employee["emp_id"])

    leave_type = st.selectbox(
        "Leave Type",
        [
            "Casual Leave",
            "Sick Leave",
            "Earned Leave",
            "Maternity Leave",
            "Paternity Leave"
        ]
    )

    start_date = st.date_input(
        "Start Date",
        value=date.today()
    )

    end_date = st.date_input(
        "End Date",
        value=date.today()
    )

    reason = st.text_area("Reason")

    if st.button("Apply Leave"):

        if reason.strip() == "":
            st.error("Reason cannot be empty.")
            return

        apply_leave(
            emp_id,
            leave_type,
            str(start_date),
            str(end_date),
            reason
        )

        st.success("✅ Leave Applied Successfully!")