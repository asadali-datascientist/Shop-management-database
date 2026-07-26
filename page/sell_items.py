import streamlit as st
import pandas as pd
from db import conn, cursor
from datetime import date

def sell():

    st.title("🛒 Sell Products")
    st.divider()

    menu = st.selectbox(
        "Select an option",
        ["Sell Product", "View Sales"]
    )

    st.divider()

    # ===========================
    # SELL PRODUCT
    # ===========================

    if menu == "Sell Product":
        st.header("Sell Product")
        cursor.execute("""
        SELECT product_id, name, sell_price
        FROM product
        WHERE user_id=%s
        """, (st.session_state.user_id,))

        products = cursor.fetchall()

        if not products:
            st.warning("No products available.")
            return

        selected = st.selectbox(
            "Select Product",
            products,
            format_func=lambda x: x[1]
        )

        product_id = selected[0]
        product_name = selected[1]
        price = selected[2]

        customer_name = st.text_input(
            "Customer Name",
            placeholder="Customer Name",key="customer_name"
        )

        quantity = st.number_input(
            "Quantity",
            min_value=1,
            step=1,key="quantity"
        )
        sale_date=st.date_input("Enter Sale Date",min_value=date(1970,1,1),
                                max_value=date.today(),key="sale_date")

        if st.button("Sell Product", type="primary"):

            if customer_name.strip() == "":
                st.error("Please enter customer name.")

            else:

                cursor.execute("""
                SELECT available_stock
                FROM stock
                WHERE product_id=%s
                AND user_id=%s
                """, (
                    product_id,
                    st.session_state.user_id
                ))

                stock = cursor.fetchone()

                if stock is None:

                    st.error("Stock not found.")

                elif quantity > stock[0]:

                    st.error("Not enough stock available.")

                else:

                    total_amount = price * quantity

                    # Save sale
                    cursor.execute("""
                    INSERT INTO sell_items
                    (
                        product_id,
                        product_name,
                        price,
                        quantity,
                        customer_name,
                        total_amount,
                        sale_date,
                        user_id
                    )
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
                    """, (
                        product_id,
                        product_name,
                        price,
                        quantity,
                        customer_name,
                        total_amount,
                        sale_date,
                        st.session_state.user_id
                    ))

                    # Update stock
                    cursor.execute("""
                    UPDATE stock
                    SET
                        sold_stock = sold_stock + %s,
                        available_stock = available_stock - %s
                    WHERE product_id=%s
                    AND user_id=%s
                    """, (
                        quantity,
                        quantity,
                        product_id,
                        st.session_state.user_id
                    ))

                    conn.commit()

                    st.success("✅ Product sold successfully.")
                    st.stop()
                    

    # ===========================
    # VIEW SALES
    # ===========================

    elif menu == "View Sales":

        st.subheader("👁️ View Sales")

        cursor.execute("""
        SELECT
            product_name,
            price,
            quantity,
            customer_name,
            total_amount,
            sale_date
        FROM sell_items
        WHERE user_id=%s
        ORDER BY id DESC
        """, (st.session_state.user_id,))

        data = cursor.fetchall()

        if data:

            df = pd.DataFrame(
                data,
                columns=[
                    "Product",
                    "Price",
                    "Quantity",
                    "Customer",
                    "Total Amount",
                    "Sale Date"
                ]
            )

            st.dataframe(
                df,
                use_container_width="stretch",
                hide_index=True
            )

        else:
            st.info("No sales available.")