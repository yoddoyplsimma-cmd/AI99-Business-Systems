import streamlit as st
import stripe

st.set_page_config(page_title="AI99 Checkout System", page_icon="💳", layout="centered")

# ใส่รหัสลับตรงๆ ลงไปในโค้ดเพื่อทดสอบระบบตามวิธีที่ทำสำเร็จ
stripe.api_key = "sk_test_YOUR_ACTUAL_SECRET_KEY_HERE"

st.title("💳 AI99 Checkout System")
st.write("---")

# จัดการสถานะแอปพลิเคชัน (State Handling)
if "checkout_url" not in st.session_state:
    st.session_state.checkout_url = None

# 🛠️ เพิ่มระบบให้ผู้ซื้อเลือกสกุลเงินที่ต้องการจ่ายได้เอง
currency_options = {
    "GBP (£) ปอนด์อังกฤษ": {"code": "gbp", "amount": 16500, "label": "165.00 GBP"},
    "USD ($) ดอลลาร์สหรัฐ": {"code": "usd", "amount": 21000, "label": "210.00 USD"}, # ราคาใกล้เคียงกันโดยประมาณ
    "EUR (€) ยูโร": {"code": "eur", "amount": 19500, "label": "195.00 EUR"},       # ราคาใกล้เคียงกันโดยประมาณ
    "SGD ($) ดอลลาร์สิงคโปร์": {"code": "sgd", "amount": 28000, "label": "280.00 SGD"} # ราคาใกล้เคียงกันโดยประมาณ
}

selected_label = st.selectbox("🌐 เลือกสกุลเงินที่ต้องการชำระเงิน:", list(currency_options.keys()))
selected_currency = currency_options[selected_label]

col1, col2 = st.columns(2)

with col1:
    st.info(f"💰 ยอดเงินที่จะเรียกเก็บ: **{selected_currency['label']}**")
    
    if st.button("Pay Now (Test Mode)", type="primary", use_container_width=True):
        with st.spinner("กำลังเชื่อมต่อช่องทางชำระเงินที่ปลอดภัย..."):
            try:
                session = stripe.checkout.Session.create(
                    payment_method_types=["card"],
                    line_items=[{
                        "price_data": {
                            "currency": selected_currency["code"], # ส่งโค้ดสกุลเงินที่เลือกไปให้ Stripe
                            "product_data": {
                                "name": "AI99 Digital Product",
                                "description": f"Premium access - Paid in {selected_currency['code'].upper()}",
                            },
                            "unit_amount": selected_currency["amount"], # ส่งจำนวนเงินในหน่วยย่อย (คูณ 100 แล้ว)
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
