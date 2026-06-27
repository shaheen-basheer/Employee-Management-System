import streamlit as st
import pandas as pd

from employee import (
    get_dashboard_stats,
    get_all_employees
)


def show_home():

    st.header("🏠 Employee Dashboard")

    stats = get_dashboard_stats()

    # ----------------------------
    # Dashboard Cards
    # ----------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("👥 Employees", stats["total"])

    with col2:
        st.metric("💰 Avg Salary", f"₹{stats['average_salary']:,}")

    with col3:
        st.metric("🏢 Departments", stats["departments"])

    with col4:
        st.metric("👨 Male", stats["male"])

    st.divider()

    # ----------------------------
    # Salary Statistics
    # ----------------------------

    col5, col6 = st.columns(2)

    with col5:
        st.metric(
            "💸 Highest Salary",
            f"₹{stats['highest_salary']:,}"
        )

    with col6:
        st.metric(
            "💵 Lowest Salary",
            f"₹{stats['lowest_salary']:,}"
        )

    st.divider()

    df = get_all_employees()

    if df.empty:
        st.info("No employees available.")
        return

    # ----------------------------
    # Charts
    # ----------------------------

    col7, col8 = st.columns(2)

    with col7:

        st.subheader("📊 Employees by Department")

        dept = (
            df.groupby("department")
            .size()
            .reset_index(name="Employees")
            .set_index("department")
        )

        st.bar_chart(dept)

    with col8:

        st.subheader("👨 Gender Distribution")

        gender = (
            df.groupby("gender")
            .size()
            .reset_index(name="Count")
            .set_index("gender")
        )

        st.bar_chart(gender)

    st.divider()

    # ----------------------------
    # Recent Employees
    # ----------------------------

    st.subheader("🆕 Recent Employees")

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
        display_df.tail(5),
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ----------------------------
    # Department Summary
    # ----------------------------

    st.subheader("🏢 Department Summary")

    summary = (
        df.groupby("department")
        .agg(
            Employees=("emp_id", "count"),
            Average_Salary=("salary", "mean")
        )
        .reset_index()
    )

    summary["Average_Salary"] = summary["Average_Salary"].apply(
        lambda x: f"₹{x:,.0f}"
    )

    summary.columns = [
        "Department",
        "Employees",
        "Average Salary"
    ]

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )