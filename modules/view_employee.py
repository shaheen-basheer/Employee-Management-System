import streamlit as st
from employee import get_all_employees


def show_view_employee():

    st.header("📋 View Employees")

    df = get_all_employees()

    if df.empty:
        st.warning("No employees found.")
        return

    col1, col2 = st.columns(2)

    with col1:
        search = st.text_input(
            "🔍 Search Employee"
        )

    with col2:

        departments = ["All"] + sorted(
            df["department"].unique().tolist()
        )

        department = st.selectbox(
            "🏢 Department",
            departments
        )

    if search:

        df = df[
            df["name"].str.contains(
                search,
                case=False
            )
        ]

    if department != "All":

        df = df[
            df["department"] == department
        ]

    st.success(f"Employees Found : {len(df)}")

    display_df = df[[
        "emp_id",
        "name",
        "department",
        "designation",
        "salary"
    ]].copy()

    display_df.columns = [
        "ID",
        "Name",
        "Department",
        "Designation",
        "Salary"
    ]

    display_df["Salary"] = display_df["Salary"].apply(
        lambda x: f"₹{x:,.0f}"
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )