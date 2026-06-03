import streamlit as st
import stripe

# ตั้งค่าหน้าเว็บให้ปลอดภัยและเป็นระเบียบ
st.set_page_config(
    page_title="AI99 Checkout System", 
    page_icon="💳",
    layout="centered"
)

# 🔒 ระบบรักษาความปลอดภัย: ตรวจสอบการตั้งค่า API Key ก่อนเริ่มทำงาน
if "SKEY" not in st.secrets or not st.secrets["SKEY"]:
    st.error("🔒 [Security Error]: ไม่พบรหัสลับ 'SKEY' ในระบบความปลอดภัย")
    st.info("💡 วิธีแก้บน Streamlit Cloud: ไปที่ Settings -> Secrets แล้วใส่ SKEY = 'sk_test_...' ค่ะ")
    st.stop()

# กำหนดคีย์ความลับให้กับระบบ Stripe อย่างปลอดภัย
stripe.api_key = st.secrets["SKEY"]

st.title("💳 AI99 Checkout System")
st.write("---")

# จัดการสถานะแอปพลิเคชัน (State Handling)
if "checkout_url" not in st.session_state:
    st.session_state.checkout_url = None

col1, col2 = st.columns()

with col1:
    # หากยังไม่มีการสร้างลิงก์ ให้แสดงปุ่มชำระเงิน
    if st.session_state.checkout_url is None:
        if st.button("Pay Now (Test Mode)", type="primary", use_container_width=True):
            with st.spinner("กำลังเชื่อมต่อช่องทางชำระเงินที่ปลอดภัย..."):
                try:
                    # สร้าง Session บน Server ของ Stripe โดยตรง ปลอดภัยจากการดักจับข้อมูลบัตร
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
                    
                    # บันทึก URL ชำระเงินอย่างปลอดภัยลงใน Session State
                    st.session_state.checkout_url = session.url
                    st.rerun()

                except stripe.error.StripeError as e:
                    st.error(f"❌ ระบบจ่ายเงินขัดข้อง: {e.user_message if hasattr(e, 'user_message') else str(e)}")
                except Exception:
                    st.error("❌ เกิดข้อผิดพลาดภายในระบบความปลอดภัย กรุณาลองใหม่อีกครั้ง")
    else:
        st.success("🎉 ระบบเตรียมช่องทางชำระเงินสำเร็จเรียบร้อยแล้วค่ะ")
        st.link_button("👉 คลิกที่นี่เพื่อไปหน้าจ่ายเงิน (Stripe)", st.session_state.checkout_url, use_container_width=True)

with col2:
    if st.session_state.checkout_url is not None:
        if st.button("🔄 ล้างรายการนี้", use_container_width=True):
            st.session_state.checkout_url = None
            st.rerun()
