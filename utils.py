import pandas as pd
import streamlit as st


def export_dataframe(df, filename):

    if df.empty:

        st.warning("No data available to export.")
        return

    excel_file = f"{filename}.xlsx"

    csv_file = f"{filename}.csv"

    # Excel
    df.to_excel(
        excel_file,
        index=False
    )

    # CSV
    df.to_csv(
        csv_file,
        index=False
    )

    col1, col2 = st.columns(2)

    with col1:

        with open(excel_file, "rb") as file:

            st.download_button(
                label="📥 Download Excel",
                data=file,
                file_name=excel_file,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    with col2:

        with open(csv_file, "rb") as file:

            st.download_button(
                label="📥 Download CSV",
                data=file,
                file_name=csv_file,
                mime="text/csv"
            )