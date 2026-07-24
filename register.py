import streamlit as st 
from db import conn,cursor
import bcrypt
import re

# with open("style.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def register():
    main_container=st.container(
    horizontal_alignment='center',
    vertical_alignment='center',
    height=650,
    width=400,
    key='form1')
    with main_container:
        content_container=st.container(
        width=350,
        key='content')
    button_container=st.container(
        width=350,
        horizontal=True,
        horizontal_alignment='distribute'
    )
    with content_container:
        st.title("Create Account",text_alignment='center',)
        username=st.text_input('Username',placeholder="Username",key='regusername')
        password=st.text_input("Password",placeholder="Passord",key='regpassword')
        confirm_password=st.text_input("Confirm Password",
                                       placeholder="Confirm Passord",
                                       key='confirmpassword')
        st.write("\n")
        register=st.button("Create Account",type='primary',key="create_account")
        if register:
            pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
            
            if username=="" and password=="" and confirm_password=="":
                st.error("Please fill the required fields!")
            elif not re.match(pattern, password):
                          st.error("""
                                Password must contain:
                                - At least 8 characters
                                - One uppercase letter
                                - One number
                                - One special character (@$!%*?&)""")
            elif password!=confirm_password:
                st.error("Password not match!")
            else:
                cursor.execute('''
                               select* from users where username=%s
                               ''',(username,))
                if cursor.fetchone():
                    st.error("Username already exist!")
                else:
                    hashed_password=bcrypt.hashpw(password.encode(),
                                                  bcrypt.gensalt()).decode()
                    cursor.execute('''
                                   insert into users(username,password)
                                   values(%s,%s)
                                   ''',(username,hashed_password,))
                    conn.commit()
                    st.success("Account Created Successfully")            