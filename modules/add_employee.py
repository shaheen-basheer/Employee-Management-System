import streamlit as st
from employee import add_employee


def show_add_employee():

    st.header("➕ Add Employee")

    name = st.text_input("Employee Name")

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=65,
        step=1
    )

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female",
            "Other"
        ]
    )

    department = st.selectbox(
        "Department",
        [
            "IT",
            "HR",
            "Finance",
            "Sales",
            "Marketing"
        ]
    )

    designation = st.text_input("Designation")

    joining_date = st.date_input("Joining Date")

    salary = st.number_input(
        "Salary",
        min_value=0.0,
        step=1000.0
    )

    if st.button("Add Employee"):

        if name.strip() == "":
            st.error("Employee Name cannot be empty.")

        elif designation.strip() == "":
            st.error("Designation cannot be empty.")

        else:

            add_employee(
                name,
                age,
                gender,
                department,
                designation,
                str(joining_date),
                salary
            )

            st.success("Employee Added Successfully!")