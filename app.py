import streamlit as st
import stripe

st.set_page_config(page_title="AI99 Checkout System", page_icon="💳", layout="centered")

# ปิดระบบเช็กของเดิม แล้วสั่งกำหนดคีย์ตรงๆ ลงไปในโค้ดเลยเพื่อทดสอบ
stripe.api_key = "sk_test_ใส่รหัสลับStripeของพี่ตรงนี้ลงไปเลย"

st.title("💳 AI99 Checkout System")
st.write("---")
