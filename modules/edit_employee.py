import streamlit as st
from employee import (
    get_all_employees,
    get_employee,
    update_employee
)


def show_edit_employee():

    st.header("✏ Edit Employee")

    df = get_all_employees()

    if df.empty:
        st.warning("No employees found.")
        return

    employee_id = st.selectbox(
        "Select Employee ID",
        df["emp_id"]
    )

    employee = get_employee(employee_id)

    employee = employee.iloc[0]

    name = st.text_input(
        "Name",
        employee["name"]
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=65,
        value=int(employee["age"])
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"],
        index=["Male", "Female", "Other"].index(employee["gender"])
    )

    department = st.selectbox(
        "Department",
        ["IT", "HR", "Finance", "Sales", "Marketing"],
        index=["IT", "HR", "Finance", "Sales", "Marketing"].index(employee["department"])
    )

    designation = st.text_input(
        "Designation",
        employee["designation"]
    )

    joining_date = st.text_input(
        "Joining Date",
        employee["joining_date"]
    )

    salary = st.number_input(
        "Salary",
        value=float(employee["salary"])
    )

    if st.button("Update Employee"):

        update_employee(
            employee_id,
            name,
            age,
            gender,
            department,
            designation,
            joining_date,
            salary
        )

        st.success("Employee Updated Successfully!")