import streamlit as st

from database import create_tables

from modules.home import show_home
from modules.add_employee import show_add_employee
from modules.view_employee import show_view_employee
from modules.edit_employee import show_edit_employee
from modules.delete_employee import show_delete_employee

create_tables()

st.set_page_config(
    page_title="Employee Management System",
    page_icon="👨‍💼",
    layout="wide"
)

st.title("👨‍💼 Employee Management System")

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Home",
        "Add Employee",
        "View Employees",
        "Edit Employee",
        "Delete Employee"
    ]
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