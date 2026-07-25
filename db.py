import mysql.connector
import streamlit as st 

conn = mysql.connector.connect(
    host=st.secrets["DB_HOST"],
    port=int(st.secrets["DB_PORT"]),
    user=st.secrets["DB_USER"],
    password=st.secrets["DB_PASSWORD"],
    database=st.secrets["DB_NAME"],
    autocommit=True
)
conn.ping(reconnect=True, attempts=3, delay=2)
cursor=conn.cursor()