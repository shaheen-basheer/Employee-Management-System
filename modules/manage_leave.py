import streamlit as st

from leave import (
    get_pending_leaves,
    approve_leave,
    reject_leave
)


def show_manage_leave():

    st.header("✅ Manage Leave Requests")

    df = get_pending_leaves()

    if df.empty:
        st.success("No Pending Leave Requests")
        return

    for _, row in df.iterrows():

        st.subheader(row["name"])

        st.write(f"Department : {row['department']}")
        st.write(f"Leave Type : {row['leave_type']}")
        st.write(f"Start Date : {row['start_date']}")
        st.write(f"End Date : {row['end_date']}")
        st.write(f"Reason : {row['reason']}")

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                f"Approve {row['id']}"
            ):

                approve_leave(row["id"])

                st.success("Leave Approved")

                st.rerun()

        with col2:

            if st.button(
                f"Reject {row['id']}"
            ):

                reject_leave(row["id"])

                st.error("Leave Rejected")

                st.rerun()

        st.divider()