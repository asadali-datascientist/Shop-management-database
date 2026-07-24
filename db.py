import mysql.connector
import streamlit as st 

conn = mysql.connector.connect(
    host=st.secrets["DB_HOST"],
    port=int(st.secrets["DB_PORT"]),
    user=st.secrets["DB_USER"],
    password=st.secrets["DB_PASSWORD"],
    database=st.secrets["DB_NAME"]
)
cursor=conn.cursor()