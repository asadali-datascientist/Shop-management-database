import streamlit as st 
from db import conn,cursor


def dashboard():
    st.set_page_config(page_title="Dashboard",
                   layout='wide')

    st.title("🏪 Shop Dashboard")
    st.divider()
    cursor.execute("select count(*) from customer where  user_id=%s",
                   (st.session_state.user_id,))
    total_customer=cursor.fetchone()[0]

    cursor.execute("select count(*) from employee Where user_id=%s",
                   (st.session_state.user_id,))
    total_employee=cursor.fetchone()[0]

    cursor.execute("select sum(salary) from employee where user_id=%s",
                   (st.session_state.user_id,))
    result=cursor.fetchone()[0]
    total_employee_salary = result if result is not None else 0

    cursor.execute("select count(distinct category) from product where user_id=%s",
                   (st.session_state.user_id,))
    total_category=cursor.fetchone()[0]
    
    cursor.execute("SELECT SUM(total_amount) FROM sell_items where user_id=%s",
                   (st.session_state.user_id,))
    sales = cursor.fetchone()[0]
    total_sales=sales if sales is not None else 0

    c1,c2,c3=st.columns(3)
    with c1:
        st.metric(
                label="Total Employee",
                value=total_employee,
                label_visibility="collapsed")
    with c2:
        st.metric(
                    label="Total Salary",
                    value=f"Rs. {total_employee_salary:,.2f}",
                    label_visibility="collapsed")
    with c3:
        st.subheader("Total Categories")
        st.metric("🛒",total_category)
        
    c4,=st.columns(1)
    with c4:
        st.metric(
                label="Total Sales",
                value=f"Rs. {total_sales:,.2f}",
                label_visibility="collapsed")   
    st.divider()