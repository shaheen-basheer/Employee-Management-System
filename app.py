import streamlit as st

from database import create_tables

# -----------------------------
# Employee Modules
# -----------------------------
from modules.home import show_home
from modules.add_employee import show_add_employee
from modules.view_employee import show_view_employee
from modules.edit_employee import show_edit_employee
from modules.delete_employee import show_delete_employee

# -----------------------------
# Attendance Modules
# -----------------------------
from modules.attendance import show_attendance
from modules.attendance_report import show_attendance_report

# -----------------------------
# Salary Modules
# -----------------------------
from modules.salary import show_salary
from modules.salary_history import show_salary_history
from modules.salary_slip import show_salary_slip
from modules.salary_raise import show_salary_raise

# -----------------------------
# Leave Modules
# -----------------------------
from modules.apply_leave import show_apply_leave
from modules.manage_leave import show_manage_leave
from modules.leave_history import show_leave_history

# -----------------------------
# Database
# -----------------------------
create_tables()

# -----------------------------
# Streamlit Config
# -----------------------------
st.set_page_config(
    page_title="Employee Management System",
    page_icon="👨‍💼",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("👨‍💼 Employee Management System")

st.caption(
    "Python • Streamlit • SQLite • Pandas • Plotly"
)

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("👨‍💼 EMS")

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "🏠 Dashboard",

        "➕ Add Employee",
        "👥 View Employees",
        "✏ Edit Employee",
        "🗑 Delete Employee",

        "📝 Mark Attendance",
        "📊 Attendance Report",

        "💰 Generate Salary",
        "📄 Salary Slip",
        "📚 Salary History",
        "📈 Salary Raise Tracking",

        "📝 Apply Leave",
        "✅ Manage Leave",
        "📋 Leave History"
    ]
)

st.sidebar.markdown("---")
st.sidebar.success("Version 1.0")

# -----------------------------
# Routing
# -----------------------------
if menu == "🏠 Dashboard":
    show_home()

elif menu == "➕ Add Employee":
    show_add_employee()

elif menu == "👥 View Employees":
    show_view_employee()

elif menu == "✏ Edit Employee":
    show_edit_employee()

elif menu == "🗑 Delete Employee":
    show_delete_employee()

elif menu == "📝 Mark Attendance":
    show_attendance()

elif menu == "📊 Attendance Report":
    show_attendance_report()

elif menu == "💰 Generate Salary":
    show_salary()

elif menu == "📄 Salary Slip":
    show_salary_slip()

elif menu == "📚 Salary History":
    show_salary_history()

elif menu == "📈 Salary Raise Tracking":
    show_salary_raise()

elif menu == "📝 Apply Leave":
    show_apply_leave()

elif menu == "✅ Manage Leave":
    show_manage_leave()

elif menu == "📋 Leave History":
    show_leave_history()