import streamlit as st
import stripe

st.set_page_config(page_title="AI99 Checkout", layout="centered")

stripe.api_key = st.secrets["SKEY"]

st.title("💳 AI99 Checkout System")

if st.button("Pay Now (Test Mode)"):

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": "AI99 Digital Product",
                },
                "unit_amount": 999,  # $9.99
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url="https://example.com/success",
        cancel_url="https://example.com/cancel",
    )

    st.write("Redirecting to Stripe...")
    st.markdown(f"[Click here if not redirected]({session.url})")
