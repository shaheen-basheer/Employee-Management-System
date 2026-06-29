import streamlit as st

from leave import get_leave_history
from utils import export_dataframe


def show_leave_history():

    st.header("📋 Leave History")

    df = get_leave_history()

    if df.empty:

        st.info("No Leave Records Found")
        return

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("📤 Export Leave History")

    export_dataframe(
        df,
        "leave_history"
    )