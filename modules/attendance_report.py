import streamlit as st
import pandas as pd

from attendance import (
    get_all_attendance,
    calculate_monthly_attendance
)


def show_attendance_report():

    st.header("📋 Attendance Report")

    attendance_df = get_all_attendance()

    if attendance_df.empty:
        st.warning("No attendance records found.")
        return

    # ----------------------------------
    # Filters
    # ----------------------------------

    st.subheader("🔍 Filter Attendance")

    col1, col2 = st.columns(2)

    with col1:

        search_name = st.text_input(
            "Search Employee"
        )

    with col2:

        status_filter = st.selectbox(
            "Attendance Status",
            [
                "All",
                "Present",
                "Absent",
                "Half-Day"
            ]
        )

    filtered_df = attendance_df.copy()

    if search_name:

        filtered_df = filtered_df[
            filtered_df["name"].str.contains(
                search_name,
                case=False
            )
        ]

    if status_filter != "All":

        filtered_df = filtered_df[
            filtered_df["status"] == status_filter
        ]

    st.divider()

    st.subheader("📄 Attendance Records")

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("📊 Monthly Attendance Summary")

    summary = calculate_monthly_attendance()

    if summary.empty:

        st.info(
            "No attendance available for the current month."
        )

        return

    summary["Status"] = summary["Attendance %"].apply(
        lambda x: "⚠ Below 75%" if x < 75 else "✅ Good"
    )

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ----------------------------------
    # Employees Below 75%
    # ----------------------------------

    st.subheader("🚨 Employees Below 75% Attendance")

    low_attendance = summary[
        summary["Attendance %"] < 75
    ]

    if low_attendance.empty:

        st.success(
            "🎉 No employees are below 75% attendance."
        )

    else:

        st.dataframe(
            low_attendance,
            use_container_width=True,
            hide_index=True
        )