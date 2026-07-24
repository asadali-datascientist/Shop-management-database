import streamlit as st 
from db import conn,cursor
import pandas as pd
from datetime import date

def employee():
    st.set_page_config(page_title="Employee",
                       page_icon="🤵",
                   layout='wide')
    st.title("🤵Employee Management")
    st.divider()
    menu=st.selectbox("Select an option",['Add Employee',
                                          'View Employee','Update Employee','Delete Employee'])
    st.divider()
    if menu=="Add Employee":
        st.header("➕ Add Employee")
        serial_number=st.text_input("Enter Employee id",placeholder='Id')
        name=st.text_input("Enter Employee Name",placeholder="Name")
        phone=st.text_input("Enter Employee Phone Number",placeholder="Number")
        salary=st.number_input("Enter Employee Salary",placeholder="Salary",step=1)
        address=st.text_area("Enter Employee address",placeholder="Address")
        join_date=st.date_input("Enter Employee Join date",
                                min_value=date(1970,1,1),max_value=date.today())
        if st.button("Add Employee",type='primary'):
            if name.strip()=="" and phone.strip()=="" and address.strip()=="" and salary<=0:
                st.error("Please fill the required fields!")
            else:
                cursor.execute('''
                               insert into employee(emp_serial_number,name,phone,
                               address,salary,join_date,user_id)
                               values (%s,%s,%s,%s,%s,%s,%s)
                               ''',(serial_number,name,phone,address,salary,
                                    join_date,
                                    st.session_state.user_id,))
                conn.commit()
                st.success("✅ Employee added successfully")
    elif menu=='View Employee':
        st.subheader("👁️ View Employes")
        cursor.execute('''
                       select emp_serial_number,name,phone,address,salary,join_date from employee
                       where user_id=%s
                       ''',(st.session_state.user_id,))
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=[
            "ID","Employee Name","Phone Number","Salary","Address","Joining Date"
        ])
        st.dataframe(df,use_container_width=True,hide_index=True)
    elif menu=="Delete Employee":
        st.header("❎ Delete Employee")
        id=st.number_input("Enter Employee id",placeholder='Id',step=1)
        if st.button("Delete Employee",type='primary'):
            if id<=0:
                st.error("Please fill required field!")
            else:
                cursor.execute('''
                                       delete from employee
                                       where emp_serial_number=%s and user_id=%s
                                       ''',(id,st.session_state.user_id,))
                if cursor.rowcount > 0:
                        st.success("✅ Employee deleted successfully.")
                else:
                        st.warning("⚠️ Employee ID not found.")
    elif menu=="Update Employee":
        st.header("🔃Update Employee")
        serial_number=st.text_input("Enter Employee id",placeholder="Id")
        name=st.text_input("Enter Employee Name",placeholder="Name")
        phone=st.text_input("Enter Employee Phone Number",placeholder="Number")
        salary=st.number_input("Enter Employee Salary",placeholder="Salary",step=1)
        address=st.text_area("Enter Employee address",placeholder="Address")
        join_date=st.date_input("Enter Employee Join date",
                                        min_value=date(1970,1,1),max_value=date.today())
        if st.button("Update Employee",type='primary'):
            if name.strip()=="" and serial_number.strip()=="" and phone.strip()=="" and address.strip()=="" and salary<=0:
                            st.error("Please fill the required fields!")
            else:
                cursor.execute('''
                               update employee set
                               name=%s,phone=%s,
                               salary=%s,address=%s,join_date=%s
                               where emp_serial_number=%s and user_id=%s
                               ''',(name,phone,salary,address,join_date,serial_number,st.session_state.user_id,))
                conn.commit()
                st.success("✅Successfully Updated")