import streamlit as st
import os

st.set_page_config(page_title="AI99 Business Systems", layout="centered")

# state จำลองหน้า
if "page" not in st.session_state:
    st.session_state.page = "home"

# ----------------------
# หน้า HOME
# ----------------------
if st.session_state.page == "home":

    st.title("🚀 AI99 Business Systems")
    st.subheader("ระบบทดสอบธุรกิจ AI99")

    st.markdown("### 💎 Test Product")

    if st.button("Test Checkout"):
        st.session_state.page = "checkout"
        st.rerun()

# ----------------------
# หน้า CHECKOUT (จำลอง)
# ----------------------
elif st.session_state.page == "checkout":

    st.title("💳 Checkout Page (Mock)")

    st.info("นี่คือหน้าจำลองการชำระเงิน")

    st.write("ระบบกำลังเตรียมเชื่อม Stripe จริง...")

    if st.button("ย้อนกลับ"):
        st.session_state.page = "home"
        st.rerun()
