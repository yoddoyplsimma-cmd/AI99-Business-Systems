import streamlit as st
import stripe

# ตั้งค่าหน้าเว็บปกติ
st.set_page_config(page_title="AI99 Checkout System", page_icon="💳", layout="centered")

# ใส่รหัสลับตรงๆ ลงไปในโค้ดเพื่อทดสอบระบบตามวิธีที่ทำสำเร็จ
stripe.api_key = "sk_test_เอาตัวเลขรหัสยาวๆของพี่มาใส่ในเครื่องหมายคำพูดนี้"

st.title("💳 AI99 Checkout System")
st.write("---")

# จัดการสถานะแอปพลิเคชัน (State Handling)
if "checkout_url" not in st.session_state:
    st.session_state.checkout_url = None

# 🛠️ แก้ไขจุดนี้: ใส่เลข 2 ลงไปในวงเล็บเพื่อให้ระบุจำนวนคอลัมน์อย่างถูกต้องตามเวอร์ชันใหม่
col1, col2 = st.columns(2)

with col1:
    # บังคับให้ปุ่มสร้างรายการชำระเงินโผล่ขึ้นมาเสมอเพื่อให้พี่กดทดสอบได้
    if st.button("Pay Now (Test Mode)", type="primary", use_container_width=True):
        with st.spinner("กำลังเชื่อมต่อช่องทางชำระเงินที่ปลอดภัย..."):
            try:
                session = stripe.checkout.Session.create(
                    payment_method_types=["card"],
                    line_items=[{
                        "price_data": {
                            "currency": "usd",
                            "product_data": {
                                "name": "AI99 Digital Product",
                                "description": "Premium access to AI99 digital services",
                            },
                            "unit_amount": 999,  # 9.99 USD
                        },
                        "quantity": 1,
                    }],
                    mode="payment",
                    success_url="https://example.com",
                    cancel_url="https://example.com",
                )
                # บันทึก URL ที่ได้จาก Stripe ลงในระบบ
                st.session_state.checkout_url = session.url
                st.success("🎉 ระบบเตรียมช่องทางชำระเงินสำเร็จเรียบร้อยแล้วค่ะ")
                
            except Exception as e:
                st.error(f"❌ เกิดข้อผิดพลาดจาก Stripe: {str(e)}")

    # เมื่อกดสร้างรายการสำเร็จแล้ว ให้ปุ่มทางไปหน้าชำระเงินแสดงขึ้นมาใต้ปุ่มหลัก
    if st.session_state.checkout_url:
        st.link_button("👉 คลิกที่นี่เพื่อไปหน้าจ่ายเงิน (Stripe)", st.session_state.checkout_url, use_container_width=True)

with col2:
    # ปุ่มสำหรับเคลียร์ล้างสถานะเพื่อทดสอบกดใหม่
    if st.session_state.checkout_url:
        if st.button("🔄 ล้างรายการเก่า", use_container_width=True):
            st.session_state.checkout_url = None
            st.rerun()
