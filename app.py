import streamlit as st
import stripe

st.set_page_config(page_title="AI99 Checkout", layout="centered")

stripe.api_key = st.secrets["SKEY"]

st.title("💳 AI99 Checkout System")

if "checkout_url" not in st.session_state:
    st.session_state.checkout_url = None

if st.button("Pay Now (Test Mode)"):

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": "AI99 Digital Product",
                },
                "unit_amount": 999,
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url="https://example.com/success",
        cancel_url="https://example.com/cancel",
    )

    st.session_state.checkout_url = session.url

if st.session_state.checkout_url:
    st.markdown(f"[👉 ไปหน้าจ่ายเงิน]({st.session_state.checkout_url})")
