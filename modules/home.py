import streamlit as st
import plotly.express as px

from employee import (
    get_dashboard_stats,
    get_department_count,
    get_salary_distribution,
    get_gender_distribution,
    get_department_salary
)

from salary import (
    get_total_payroll,
    get_top_paid_employees,
    get_department_payroll
)


def show_home():

    st.header("📊 Employee Management Dashboard")

    stats = get_dashboard_stats()

    total_payroll = get_total_payroll()

    # ==========================================
    # KPI CARDS
    # ==========================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "👥 Total Employees",
            stats["total"]
        )

    with c2:
        st.metric(
            "💰 Avg Salary",
            f"₹ {stats['average_salary']:,}"
        )

    with c3:
        st.metric(
            "💵 Total Payroll",
            f"₹ {int(total_payroll):,}"
        )

    with c4:
        st.metric(
            "🏢 Departments",
            stats["departments"]
        )

    st.divider()

    # ==========================================
    # FIRST ROW
    # ==========================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🏢 Department-wise Employee Count")

        dept_df = get_department_count()

        if not dept_df.empty:

            fig = px.bar(
                dept_df,
                x="department",
                y="Employees",
                text="Employees",
                color="Employees"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    with col2:

        st.subheader("💰 Salary Distribution")

        salary_df = get_salary_distribution()

        if not salary_df.empty:

            fig = px.histogram(
                salary_df,
                x="salary",
                nbins=10
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    st.divider()

    # ==========================================
    # SECOND ROW
    # ==========================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("👨 Gender Distribution")

        gender_df = get_gender_distribution()

        if not gender_df.empty:

            fig = px.pie(
                gender_df,
                names="gender",
                values="Employees",
                hole=0.45
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    with col2:

        st.subheader("💼 Average Salary by Department")

        dept_salary = get_department_salary()

        if not dept_salary.empty:

            fig = px.bar(
                dept_salary,
                x="salary",
                y="department",
                orientation="h",
                text_auto=".2s"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    st.divider()

    # ==========================================
    # THIRD ROW
    # ==========================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🏆 Top 5 Highest Paid Employees")

        top_df = get_top_paid_employees()

        if not top_df.empty:

            fig = px.bar(
                top_df,
                x="net_salary",
                y="name",
                orientation="h",
                text="net_salary",
                color="net_salary"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    with col2:

        st.subheader("🏢 Department Payroll")

        payroll_df = get_department_payroll()

        if not payroll_df.empty:

            fig = px.pie(
                payroll_df,
                names="department",
                values="payroll",
                hole=0.45
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )