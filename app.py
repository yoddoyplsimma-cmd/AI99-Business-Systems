import streamlit as st
import stripe

st.set_page_config(page_title="AI99 Checkout System", page_icon="💳", layout="centered")

# ใส่รหัสลับโหมดทดสอบ sk_test_... ของพี่ตรงนี้เหมือนเดิมนะคะ
stripe.api_key = "sk_test_51TUw0KD0F0jpQtDWsxh6txwmyMFrgLo2tjBE8sDQsXyKpqCBHqEt4MBing4oW5dfvbsTobtFJ31yXo6WH7S53P1z001Z8oqVvf"

st.title("💳 AI99 Checkout System")
st.write("---")

# กำหนดตัวเลือกสกุลเงินและราคาสรุปย่อย (หน่วยเซนต์/เพนนี)
currency_options = {
    "GBP (£) ปอนด์อังกฤษ": {"code": "gbp", "amount": 16500, "label": "165.00 GBP"},
    "USD ($) ดอลลาร์สหรัฐ": {"code": "usd", "amount": 21000, "label": "210.00 USD"},
    "EUR (€) ยูโร": {"code": "eur", "amount": 19500, "label": "195.00 EUR"},
    "SGD ($) ดอลลาร์สิงคโปร์": {"code": "sgd", "amount": 28000, "label": "280.00 SGD"}
}

# 🛠️ ตรวจสอบการเปลี่ยนสกุลเงิน: หากมีการเปลี่ยนช้อยส์ ให้ล้างลิงก์เก่าทันทีอัตโนมัติ
if "previous_currency" not in st.session_state:
    st.session_state.previous_currency = "GBP (£) ปอนด์อังกฤษ"
if "checkout_url" not in st.session_state:
    st.session_state.checkout_url = None

selected_label = st.selectbox("🌐 เลือกสกุลเงินที่ต้องการชำระเงิน:", list(currency_options.keys()))

# ถ้ายูสเซอร์สลับคอยน์สกุลเงิน ให้สั่งล้าง URL เก่าทิ้งทันที ระบบจะได้ไม่จำค่าเก่า 9.99 ดอลลาร์ค่ะ
if selected_label != st.session_state.previous_currency:
    st.session_state.checkout_url = None
    st.session_state.previous_currency = selected_label
    st.rerun()

selected_currency = currency_options[selected_label]

col1, col2 = st.columns(2)

with col1:
    st.info(f"💰 ยอดเงินที่จะเรียกเก็บ: **{selected_currency['label']}**")
    
    # แสดงปุ่มกดสร้างลิงก์ชำระเงินใหม่
    if st.session_state.checkout_url is None:
        if st.button("Pay Now (Test Mode)", type="primary", use_container_width=True):
            with st.spinner("กำลังเชื่อมต่อช่องทางชำระเงินที่ปลอดภัย..."):
                try:
                    session = stripe.checkout.Session.create(
                        payment_method_types=["card"],
                        line_items=[{
                            "price_data": {
                                "currency": selected_currency["code"],
                                "product_data": {
                                    "name": "AI99 Digital Product",
                                    "description": f"Premium access - Paid in {selected_currency['code'].upper()}",
                                },
                                "unit_amount": selected_currency["amount"],
                            },
                            "quantity": 1,
                        }],
                        mode="payment",
                        success_url="https://example.com",
                        cancel_url="https://example.com",
                    )
                    st.session_state.checkout_url = session.url
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ เกิดข้อผิดพลาดจาก Stripe: {str(e)}")
    else:
        # ลิงก์ที่อัปเดตราคาใหม่แล้วจะขึ้นให้คลิกตรงนี้
        st.success("🎉 ระบบลงทะเบียนยอดเงินใหม่สำเร็จแล้วค่ะ")
        st.link_button("👉 คลิกที่นี่เพื่อไปหน้าจ่ายเงิน (Stripe)", st.session_state.checkout_url, use_container_width=True)

with col2:
    if st.session_state.checkout_url:
        if st.button("🔄 ล้างรายการเก่า เพื่อคำนวณใหม่", use_container_width=True):
            st.session_state.checkout_url = None
            st.rerun()
