import streamlit as st 
from db import conn
from db import cursor
from login import login
from register import register
from page.dashboard import dashboard
from page.product import product
from page.employee import employee
#from page.customer import customer
from page.sell_items import sell
from page.stock import stock
from page.about import about
from logout import logout


st.set_page_config(
    page_title="Shop Management",
    layout='wide',
    page_icon='🏪',
    initial_sidebar_state="expanded"
)

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state.logged_in=False
    if "user_id" not in st.session_state:
        st.session_state.user_id=None
    if "username" not in st.session_state:   
        st.session_state.username="user_name"
  
if not st.session_state.logged_in:  
        menu=st.sidebar.selectbox("Menu",
        ["Login","Register"],key='sidebar')

        if menu=="Login":
            login()
        else:
            register()
else:
    st.sidebar.title("Store Management")
    st.sidebar.write(f"Welcome {st.session_state.username}")
    page=st.sidebar.radio(
        "Select an option",['📈Dashboard','🛒Product',
                            '👨‍💼Employee',
                            '🗠 Stock','🤝Sell','🛍️about']
    )
    if logout:
        logout()
    if page=='📈Dashboard':
        dashboard()
    elif page=="🛒Product":
        product()
    elif page=="👨‍💼Employee":
        employee()
    # elif page=="💁‍♂️Customer":
    #     customer()
    elif page=="🤝Sell":
            sell()
    elif page=="🗠 Stock":
            stock()
    elif page=="🛍️about":
        about()