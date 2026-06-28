import streamlit as st

from employee import get_all_employees
from salary import get_salary_raise_history


def show_salary_raise():

    st.header("📈 Salary Raise Tracking")

    employees = get_all_employees()

    if employees.empty:
        st.warning("No employees found.")
        return

    employees["display"] = employees.apply(
        lambda row: f"{int(row['emp_id'])} - {row['name']}",
        axis=1
    )

    selected = st.selectbox(
        "Select Employee",
        employees["display"]
    )

    emp = employees[
        employees["display"] == selected
    ].iloc[0]

    emp_id = int(emp["emp_id"])

    df = get_salary_raise_history(emp_id)

    if df.empty:
        st.info("No salary history available.")
        return

    st.subheader("Salary Growth")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.line_chart(
        df.set_index("month")["net_salary"]
    )