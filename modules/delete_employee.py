import streamlit as st
from employee import get_all_employees, delete_employee


def show_delete_employee():

    st.header("🗑 Delete Employee")

    df = get_all_employees()

    if df.empty:
        st.warning("No employees available.")
        return

    employee_id = st.selectbox(
        "Select Employee ID",
        df["emp_id"]
    )

    employee = df[df["emp_id"] == employee_id].iloc[0]

    st.write("### Employee Details")

    st.write(f"**Name:** {employee['name']}")
    st.write(f"**Department:** {employee['department']}")
    st.write(f"**Designation:** {employee['designation']}")
    st.write(f"**Salary:** ₹{employee['salary']}")

    st.warning("This action cannot be undone.")

    confirm = st.checkbox("I confirm I want to delete this employee")

    if st.button("Delete Employee"):

        if confirm:

            delete_employee(employee_id)

            st.success("Employee deleted successfully!")

            st.rerun()

        else:

            st.error("Please confirm before deleting.")