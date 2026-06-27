import streamlit as st
from employee import get_all_employees


def show_view_employee():

    st.header("📋 View Employees")

    df = get_all_employees()

    if df.empty:
        st.warning("No employees found.")
        return

    # ----------------------------
    # Search Box
    # ----------------------------

    search = st.text_input(
        "🔍 Search Employee by Name"
    )

    # ----------------------------
    # Department Filter
    # ----------------------------

    departments = ["All"] + sorted(df["department"].unique().tolist())

    selected_department = st.selectbox(
        "Department",
        departments
    )

    # ----------------------------
    # Apply Search
    # ----------------------------

    if search:

        df = df[
            df["name"].str.contains(
                search,
                case=False
            )
        ]

    # ----------------------------
    # Apply Department Filter
    # ----------------------------

    if selected_department != "All":

        df = df[
            df["department"] == selected_department
        ]

    # ----------------------------
    # Show Employee Count
    # ----------------------------

    st.success(f"Total Employees : {len(df)}")

    # ----------------------------
    # Display Table
    # ----------------------------

    st.dataframe(
        df,
        use_container_width=True
    )