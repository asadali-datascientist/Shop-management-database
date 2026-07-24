import streamlit as st
import pandas as pd
from db import conn, cursor

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
            placeholder="Customer Name"
        )

        quantity = st.number_input(
            "Quantity",
            min_value=1,
            step=1
        )

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
                        user_id
                    )
                    VALUES(%s,%s,%s,%s,%s,%s,%s)
                    """, (
                        product_id,
                        product_name,
                        price,
                        quantity,
                        customer_name,
                        total_amount,
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

    # ===========================
    # VIEW SALES
    # ===========================

    elif menu == "View Sales":

        st.subheader("👁️ View Sales")

        cursor.execute("""
        SELECT
            id,
            product_name,
            price,
            quantity,
            customer_name,
            total_amount
        FROM sell_items
        WHERE user_id=%s
        ORDER BY id DESC
        """, (st.session_state.user_id,))

        data = cursor.fetchall()

        if data:

            df = pd.DataFrame(
                data,
                columns=[
                    "Sale ID",
                    "Product",
                    "Price",
                    "Quantity",
                    "Customer",
                    "Total Amount"
                ]
            )

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

        else:
            st.info("No sales available.")