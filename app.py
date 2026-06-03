import streamlit as st
import stripe

st.set_page_config(page_title="AI99 Checkout System", page_icon="💳", layout="centered")

# 🛠️ ตรวจสอบจุดนี้: พี่ต้องเอาคีย์จริงที่ขึ้นต้นด้วย sk_test_... มาใส่แทนข้อความด้านล่างนี้นะคะ
# ห้ามระบุภาษาไทยลงในเครื่องหมายคำพูดนี้เด็ดขาดค่ะ
stripe.api_key = "sk_test_51TUw0KD0F0jpQtDWsxh6txwmyMFrgLo2tjBE8sDQsXyKpqCBHqEt4MBing4oW5dfvbsTobtFJ31yXo6WH7S53P1z001Z8oqVvf"

st.title("💳 AI99 Checkout System")
st.write("---")

if "checkout_url" not in st.session_state:
    st.session_state.checkout_url = None

col1, col2 = st.columns(2)

with col1:
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
                            "unit_amount": 999,
                        },
                        "quantity": 1,
                    }],
                    mode="payment",
                    success_url="https://example.com",
                    cancel_url="https://example.com",
                )
                st.session_state.checkout_url = session.url
                st.success("🎉 ระบบเตรียมช่องทางชำระเงินสำเร็จเรียบร้อยแล้วค่ะ")
                st.rerun()
                
            except Exception as e:
                st.error(f"❌ เกิดข้อผิดพลาดจาก Stripe: {str(e)}")

    if st.session_state.checkout_url:
        st.link_button("👉 คลิกที่นี่เพื่อไปหน้าจ่ายเงิน (Stripe)", st.session_state.checkout_url, use_container_width=True)

with col2:
    if st.session_state.checkout_url:
        if st.button("🔄 ล้างรายการเก่า", use_container_width=True):
            st.session_state.checkout_url = None
            st.rerun()
