import streamlit as st
from datetime import datetime

from employee import get_all_employees
from salary import generate_salary


def show_salary():

    st.header("💰 Generate Salary")

    employees = get_all_employees()

    if employees.empty:
        st.warning("No employees found.")
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

    emp_id = int(selected_employee["emp_id"])

    st.subheader("Salary Details")

    basic_salary = st.number_input(
        "Basic Salary (₹)",
        min_value=0.0,
        step=1000.0
    )

    bonus = st.number_input(
        "Bonus (₹)",
        min_value=0.0,
        step=500.0
    )

    tax = st.number_input(
        "Tax Deduction (₹)",
        min_value=0.0,
        step=500.0
    )

    pf = st.number_input(
        "PF Deduction (₹)",
        min_value=0.0,
        step=500.0
    )

    month = st.text_input(
        "Month",
        value=datetime.now().strftime("%B %Y")
    )

    st.divider()

    net_salary = basic_salary + bonus - tax - pf

    st.metric(
        "Net Salary",
        f"₹ {net_salary:,.2f}"
    )

    if st.button("Generate Salary"):

        generate_salary(
            emp_id,
            basic_salary,
            bonus,
            tax,
            pf,
            month
        )

        st.success("✅ Salary Generated Successfully!")