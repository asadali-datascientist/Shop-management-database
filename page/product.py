import streamlit as st
from datetime import date
import pandas as pd  
from db import conn,cursor

def product():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
    st.set_page_config(page_title="Product",
                       page_icon="🛒",
                   layout='wide')
    
    st.title("🧾 Product Management")
    st.divider()
    menu=st.selectbox("Select an option",['Add Product','Update Product',
                                     'Delete Product','View Product'])
    st.divider()
    if menu=='Add Product':
        st.subheader("➕Add Product")
        serial_number=st.text_input("Enter  product Serial Number",
                                    placeholder='Serial Number',key="serial_number")
        name=st.text_input("Enter product name",placeholder="Name",key='product_name')
        category=st.text_input("Category",placeholder='Category',key="category")
        purchase_price=st.number_input("Enter Purchase  Price",
                                       placeholder='Price',step=1,key="purchase_price")
        sell_price=st.number_input('Enter Selling Price',placeholder='Price',step=1,
                                   key="sell_price")
        quantity=st.number_input("Enter Total Quantity",placeholder="Quantity",
                                 key="quantity",step=1)
        product_date=st.date_input("Enter Date",min_value=date(1970,1,1),
                                   key="product_date",max_value=date.today())
        if st.button("Add Product",type='primary'):
            if name.strip()=="" and quantity<=0 and category.strip()=="" and purchase_price<=0 and sell_price<=0:
                st.error("Please fill required fields!")
            else:
                cursor.execute('''
                               insert into product(name,category,purchase_price,
                               sell_price,serial_number,quantity,user_id,product_date)
                               values(%s,%s,%s,%s,%s,%s,%s,%s)
                               ''',(name,category,purchase_price,sell_price,
                                    serial_number,quantity,
                                    st.session_state.user_id,product_date,))
                conn.commit()
                product_id = cursor.lastrowid
                cursor.execute("""
                            INSERT INTO stock
                            (product_id,total_stock,sold_stock,available_stock,user_id)
                            VALUES(%s,%s,%s,%s,%s)
                            """,(
                             product_id,
                            quantity,
                            0,
                            quantity,
                            st.session_state.user_id))
                
                conn.commit()
                st.success(" ✅ Product added successfully")
                
    elif menu=="Delete Product":
        st.subheader("❎Delete Product")
        id=st.number_input("Enter product serial Number",
                           placeholder='Serial Number',
                           key='delete_serial',step=1)
        if st.button("Delete",type='primary'):
            if id<=0:
                st.error("Please fill required field")
            else:
                cursor.execute('''
                               delete from product where serial_number=%s and user_id=%s
                               ''',(id,st.session_state.user_id,))
                if cursor.rowcount > 0:
                    st.success("✅ Product deleted successfully.")
                else:
                        st.warning("⚠️ Product ID not found.")
                        
    elif menu=="View Product":
        st.subheader("👁️View Product")
        cursor.execute('''
                       select serial_number,name,category,purchase_price,sell_price
                       ,quantity,product_date FROM product where user_id=%s
                       ''',(st.session_state.user_id,))
        data=cursor.fetchall()
        df = pd.DataFrame(
        data,
        columns=[
            "Serial Number",
            "Product Name",
            "Category",
            "Purchase Price",
            "Sell Price",
            "Total Quantity",
            "Product Added Date"
        ]
    )

        st.dataframe(df,use_container_width=True,hide_index=True)
        
    elif menu=='Update Product':
        st.subheader("🔃Update Product")
        serial_number=st.text_input("Enter Product Serail  Number",
                                      placeholder="Serial Number",
                                      key="update_serial")
        name=st.text_input("Enter product name",placeholder="Name",
                           key='product_name')
        category=st.text_input("Category",placeholder='Category',
                               key="update_category")
        purchase_price=st.number_input("Enter Purchase  Price",
                                        key="update_purchase",placeholder='Price',step=1)
        sell_price=st.number_input('Enter Selling Price',placeholder='Price',
                                   key="update_sell",step=1)
        quantity=st.number_input("Enter Total Quantity",placeholder="Quantity",
                                 key="update_quantity",step=1)
        product_date=st.date_input("Enter Date",min_value=date(1970,1,1),
                                   key="update_date",max_value=date.today())
        if st.button("Update",type='primary'):
            if name.strip()=="" and serial_number.strip()=="" and category.strip()=="" and purchase_price<=0 and sell_price<=0:
                        st.error("Product id missing!")
            else:
                cursor.execute('''
                               update product set
                               name=%s,category=%s,
                               purchase_price=%s,sell_price=%s,
                               quantity=%s,product_date=%s
                               where serial_number=%s and user_id=%s
                               ''',(name,category,purchase_price,
                                    sell_price,quantity,
                                    product_date,serial_number,st.session_state.user_id,))
                conn.commit()
            