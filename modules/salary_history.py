import streamlit as st

from salary import get_salary_history
from utils import export_dataframe


def show_salary_history():

    st.header("📜 Salary History")

    df = get_salary_history()

    if df.empty:
        st.warning("No salary records found.")
        return

    st.subheader("🔍 Search")

    search = st.text_input(
        "Search Employee"
    )

    if search:

        df = df[
            df["name"].str.contains(
                search,
                case=False
            )
        ]

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("📤 Export Salary History")

    export_dataframe(
        df,
        "salary_history"
    )