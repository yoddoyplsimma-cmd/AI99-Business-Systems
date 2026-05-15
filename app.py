import streamlit as st
import os

st.set_page_config(page_title="AI99 Business Systems", layout="centered")

st.title("🚀 AI99 Business Systems")
st.subheader("ระบบทดสอบธุรกิจ AI99")

st.write("ระบบกำลังอยู่ในโหมด Deployment Test")

# Stripe (safe mode)
stripe_key = st.secrets.get("SKEY", os.getenv("SKEY"))

if stripe_key:
    st.success("Stripe พร้อมใช้งาน")
else:
    st.warning("Stripe ยังไม่ตั้งค่า (Test Mode)")

st.divider()
st.markdown("### 💎 Test Product")

if st.button("Test Checkout"):
    st.info("ระบบกำลังจำลองการชำระเงิน (ยังไม่เชื่อม Stripe จริง)")
