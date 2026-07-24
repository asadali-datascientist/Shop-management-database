import streamlit as st
import pandas as pd
from db import cursor

def stock():

    st.title("📦 Stock Management")

    cursor.execute("""
    SELECT
        p.serial_number,
        p.name,
        p.category,
        s.total_stock,
        s.sold_stock,
        s.available_stock
    FROM stock s
    JOIN product p
    ON s.product_id=p.product_id
    WHERE s.user_id=%s
    """,(st.session_state.user_id,))

    data=cursor.fetchall()

    df=pd.DataFrame(
        data,
        columns=[
            "Product Serial Number",
            "Product Name",
            "Category",
            "Total Stock",
            "Sold",
            "Available"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )