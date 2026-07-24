import streamlit as st 
from db import conn,cursor


def logout():
    logout=st.sidebar.button("Logout",key='logout',type='primary')
    if logout:
        st.session_state.logged_in=False
        st.session_state.user_id=None
        st.session_state.username=""
        st.rerun()