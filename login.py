import streamlit as st 
from db import conn
from db import cursor
import bcrypt

# with open("style.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def login():
    main_container=st.container(
    horizontal_alignment='center',
    vertical_alignment='center',
    height=550,
    width=400,
    key='form')
    with main_container:
        content_container=st.container(
        width=300,
        key='content')
    button_container=st.container(
        width=300,
        horizontal=True,
        horizontal_alignment='distribute'
    )
    with content_container:
        st.title("Login",text_alignment='center',)
        username=st.text_input('Username',placeholder="Username",key='loginusername')
        password=st.text_input("Password",placeholder="Passord",
                               type='password',key='password')
        Login=st.button("Login",type='primary',key="Login")
    
    if Login:
        if username=="" and password=="":
            st.error("Please fill the required fields!")
        else:
            query=('''
                           select * from users where username=%s
                           ''')
            values=(username,)
            cursor.execute(query,values)
            
            user=cursor.fetchone()
            if user:
                user_id=user[0]
                user_name=user[1]
                db_password=user[2]
                if bcrypt.checkpw((password.encode()),db_password.encode()):
                    st.session_state.logged_in=True
                    st.session_state.user_id=user_id
                    st.session_state.username=user_name
                    st.success("Login Successfully")
                    st.rerun()
                else:
                    st.error("incorrect password!")
            else:
                st.error("User Not Found!")