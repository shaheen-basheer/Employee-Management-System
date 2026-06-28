import streamlit as st

from database import create_tables
from modules.attendance_report import show_attendance_report

from modules.home import show_home
from modules.add_employee import show_add_employee
from modules.view_employee import show_view_employee
from modules.edit_employee import show_edit_employee
from modules.delete_employee import show_delete_employee
from modules.attendance import show_attendance

create_tables()

st.set_page_config(
    page_title="EMS Dashboard",
    page_icon="👨‍💼",
    layout="wide"
)

st.title("👨‍💼 Employee Management System")

st.caption(
    "A Python + Streamlit + SQLite application for managing employees."
)

st.divider()

st.sidebar.title("👨‍💼 EMS")
st.sidebar.markdown("---")

menu = st.sidebar.selectbox(
    "📂 HR Management",
    [
        "Home",
        "Add Employee",
        "View Employees",
        "Edit Employee",
        "Delete Employee",
        "Mark Attendance",
        "Attendance Report"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "Employee Management System\n\nVersion 1.0"
)

if menu == "Home":
    show_home()

elif menu == "Add Employee":
    show_add_employee()

elif menu == "View Employees":
    show_view_employee()

elif menu == "Edit Employee":
    show_edit_employee()

elif menu == "Delete Employee":
    show_delete_employee()

elif menu == "Mark Attendance":
    show_attendance()

elif menu == "Attendance Report":
    show_attendance_report()