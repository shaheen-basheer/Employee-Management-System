import streamlit as st

from employee import get_all_employees
from salary import (
    get_salary_history,
    get_salary_slip
)


def show_salary_slip():

    st.header("📄 Salary Slip")

    employees = get_all_employees()

    if employees.empty:
        st.warning("No employees found.")
        return

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

    emp_id = int(selected_employee["emp_id"])

    history = get_salary_history()

    months = history[
        history["emp_id"] == emp_id
    ]["month"].unique().tolist()

    if len(months) == 0:

        st.info("No salary generated for this employee.")

        return

    selected_month = st.selectbox(
        "Select Month",
        months
    )

    slip = get_salary_slip(
        emp_id,
        selected_month
    )

    if slip.empty:

        st.warning("Salary Slip Not Found.")

        return

    row = slip.iloc[0]

    st.divider()

    st.subheader("Employee Details")

    col1, col2 = st.columns(2)

    with col1:

        st.write(f"**Employee:** {row['name']}")
        st.write(f"**Department:** {row['department']}")

    with col2:

        st.write(f"**Designation:** {row['designation']}")
        st.write(f"**Month:** {row['month']}")

    st.divider()

    st.subheader("Salary Breakdown")

    st.write(f"**Basic Salary :** ₹ {row['basic_salary']:,.2f}")
    st.write(f"**Tax :** ₹ {row['tax']:,.2f}")
    st.write(f"**PF :** ₹ {row['pf']:,.2f}")

    st.divider()

    st.success(
        f"Net Salary : ₹ {row['net_salary']:,.2f}"
    )