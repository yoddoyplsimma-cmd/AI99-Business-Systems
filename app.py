import streamlit as st
import stripe
import base64
import time
from datetime import datetime, timedelta

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="AI99 Sandbox Simulator", page_icon="🧪", layout="centered")

# ใส่รหัสลับโหมดทดสอบ Stripe (ใช้ sk_test สำหรับ Sandbox)
stripe.api_key = "sk_test_51TUw0KD0F0jpQtDWsxh6txwmyMFrgLo2tjBE8sDQsXyKpqCBHqEt4MBing4oW5dfvbsTobtFJ31yXo6WH7S53P1z001Z8oqVvf"

st.title("🧪 AI99 Checkout & Legal Contract Sandbox Simulator")
st.caption("ระบบจำลองสถานะเสมือนจริงครบวงจร (Frontend + Payment Check + Cloud Vault + Email Delivery)")
st.write("---")

# 2. ฐานข้อมูลคลังไฟล์สัญญาเสมือนจริง (เชื่อมโยงพิกัดสัญญาระดับ 9.8/10)
countries = ["USA", "UK", "Singapore", "Australia", "Germany", "Netherlands", "Switzerland"]
professions = ["Freelance Creators", "Online Sellers", "Virtual Assistants", "Online Coaches", "Independent Contractors"]

contracts_db = {
    country: {
        prof: f"legal_contract_{country.lower()}_{prof.lower().replace(' ', '_')}.pdf" 
        for prof in professions
    } for country in countries
}

currency_options = {
    "GBP (£) ปอนด์อังกฤษ": {"code": "gbp", "amount": 16500, "label": "165.00 GBP"},
    "USD ($) ดอลลาร์สหรัฐ": {"code": "usd", "amount": 21000, "label": "210.00 USD"},
    "EUR (€) ยูโร": {"code": "eur", "amount": 19500, "label": "195.00 EUR"},
    "SGD ($) ดอลลาร์สิงคโปร์": {"code": "sgd", "amount": 28000, "label": "280.00 SGD"}
}

# 3. บริหารสถานะระบบ (Session State)
if "previous_currency" not in st.session_state: st.session_state.previous_currency = "GBP (£) ปอนด์อังกฤษ"
if "checkout_url" not in st.session_state: st.session_state.checkout_url = None
if "payment_success" not in st.session_state: st.session_state.payment_success = False
if "selected_contract" not in st.session_state: st.session_state.selected_contract = ""
if "customer_email" not in st.session_state: st.session_state.customer_email = ""

# 4. หน้าจอหลัก: รับข้อมูลและเลือกตัวเลือก (Frontend Input)
st.subheader("🌐 1. เลือกแพ็กเกจสัญญาและระบุข้อมูลผู้ซื้อ")
customer_email_input = st.text_input("📧 ระบุอีเมลของผู้ซื้อ (สำหรับจำลองการจัดส่ง):", placeholder="example@customer.com")

col_a, col_b = st.columns(2)
with col_a:
    selected_country = st.selectbox("📌 เลือกประเทศ (Jurisdiction):", countries)
with col_b:
    selected_prof = st.selectbox("💼 เลือกสายอาชีพ (Profession):", professions)

target_file = contracts_db[selected_country][selected_prof]
selected_label = st.selectbox("💵 เลือกสกุลเงินที่ต้องการชำระเงิน:", list(currency_options.keys()))

# เคลียร์ระบบอัตโนมัติเมื่อมีการเปลี่ยนอินพุต ป้องกันข้อมูลข้ามลูป
if selected_label != st.session_state.previous_currency:
    st.session_state.checkout_url = None
    st.session_state.payment_success = False
    st.session_state.previous_currency = selected_label
    st.rerun()

selected_currency = currency_options[selected_label]
st.write("---")

# 5. ระบบคุ้มครองสิทธิ์ทางกฎหมาย (Double Checkbox Enforced)
st.subheader("⚖️ 2. ข้อตกลงทางกฎหมายและการยอมรับเงื่อนไข")
agree_terms = st.checkbox("I agree to the Terms of Service and Privacy Policy.")
agree_refund = st.checkbox("To the fullest extent permitted by applicable law, all fees are non-refundable once the digital assets, services, or materials have been accessed, delivered, or made available.")
is_compliant = agree_terms and agree_refund and (customer_email_input != "")

if customer_email_input == "":
    st.caption("⚠️ *กรุณากรอกอีเมลผู้ซื้อเพื่อเปิดระบบจำลอง*")

st.write("---")

# 6. ส่วนประมวลผลและการจำลองสเต็ปการชำระเงิน
st.subheader("💳 3. สถานะการประมวลผลระบบ")
col1, col2 = st.columns(2)

with col1:
    st.info(f"📋 สัญญาที่จะได้รับ: **[{selected_country}] {selected_prof}**")
    st.warning(f"💰 ยอดเงินเรียกเก็บ: **{selected_currency['label']}**")
    
    if st.session_state.checkout_url is None and not st.session_state.payment_success:
        if st.button("🚀 จ่ายเงินและเปิดระบบเสมือนจริง", type="primary", use_container_width=True, disabled=not is_compliant):
            with st.spinner("ตรรกะระบบกำลังจำลองการยิงหาเซิร์ฟเวอร์ Stripe..."):
                try:
                    # เรียกใช้สิทธิ์ Stripe Session ในโหมด Sandbox 
                    session = stripe.checkout.Session.create(
                        payment_method_types=["card"],
                        line_items=[{
                            "price_data": {
                                "currency": selected_currency["code"],
                                "product_data": {
                                    "name": f"AI99 Legal Core Contract: {selected_country}",
                                    "description": f"Professional Package for {selected_prof}",
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
                    st.session_state.selected_contract = target_file
                    st.session_state.customer_email = customer_email_input
                    
                    # บังคับระบบเปลี่ยนสถานะเป็นชำระเงินสำเร็จ (Simulated Success)
                    st.session_state.payment_success = True 
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Stripe Error: {str(e)}")

# 7. ลูปเสมือนจริงของตัวเลือกที่ 1 + ตัวเลือกที่ 2 (ลูปหลังจ่ายเงินสำเร็จ)
if st.session_state.payment_success:
    st.success("🎉 [STRIPE WEBHOOK: SUCCESS] ระบบตัดเงินสำเร็จและส่งสัญญาณกลับหลังบ้านเรียบร้อย!")
    
    expiry_time = datetime.now() + timedelta(hours=24)
    secure_payload = f"{st.session_state.selected_contract}||{expiry_time.timestamp()}"
    secure_token = base64.b64encode(secure_payload.encode()).decode()
    
    # ─── SIMULATION ตัวเลือกที่ 2: เชื่อมคลังไฟล์จริงและทำ Secure Link ───
    st.markdown("### 🔓 [Vault Simulation] ระบบจำลองการดึงไฟล์จากคลังคลาวด์")
    st.write(f"📁 ค้นพบไฟล์จริงในระบบ: `{st.session_state.selected_contract}`")
    st.write(f"⏳ Secure Link Expiry: `{expiry_time.strftime('%Y-%m-%d %H:%M:%S')}` (Link บล็อกความเสี่ยงแบบมีอายุ 24 ชม.)")
    
    st.download_button(
        label="📥 กดทดสอบดาวน์โหลดไฟล์สัญญาจริง (Secure UI Link)",
        data=f"--- AI99 SECURE LEGAL CONTRACT PRODUCTION ---\nTarget Asset File: {st.session_state.selected_contract}\nVerification Security Token: {secure_token}\nJurisdiction Governing Law Enforced: {selected_country}\nProfessional Module Attached: {selected_prof}",
        file_name=st.session_state.selected_contract,
        mime="application/pdf",
        use_container_width=True
    )
    
    # ─── SIMULATION ตัวเลือกที่ 1: ตรรกะจำลองการส่งอีเมล ───
    st.write("---")
    st.markdown("### 📨 [Email Simulation] ระบบจำลองการทำงานของ Mail Server")
    with st.expander("📬 คลิกเปิดกล่องข้อความจำลอง เพื่อดูหน้าตาอีเมลที่ลูกค้าจะได้รับ", expanded=True):
        st.markdown(f"""
        **From:** no-reply@ai99.com  
        **To:** `{st.session_state.customer_email}`  
        **Subject:** ใบเสร็จรับเงินและลิงก์ดาวน์โหลดสัญญาเสร็จสมบูรณ์จาก AI99  
        
        เรียน ท่านสมาชิกผู้ใช้งาน,  
        ระบบได้ทำการประมวลผลการชำระเงินจำนวน **{selected_currency['label']}** เสร็จสิ้นเรียบร้อยแล้ว  
        
        ขณะนี้ สัญญาประเภท **[{selected_country}] - {selected_prof}** ได้รับการอนุมัติสิทธิ์การเข้าถึงเชิงพาณิชย์แล้ว ท่านสามารถกดดาวน์โหลดไฟล์จริงได้ผ่านระบบสำรองด้านล่างนี้:  
        
        🔗 [คลิกดาวน์โหลดสัญญาแบบเข้ารหัสปลอดภัย (Temporary Link)]({st.session_state.checkout_url if st.session_state.checkout_url else 'https://example.com'})  
        *(ลิงก์นี้ระบบจะปิดการเข้าถึงอัตโนมัติภายใน 24 ชั่วโมง เพื่อรักษาความปลอดภัยสูงสุด)* ขอบคุณที่ร่วมงานวิจัยและใช้บริการระบบสัญญากลสากล AI99  
        """)

with col2:
    if st.session_state.checkout_url or st.session_state.payment_success:
        if st.button("🔄 รีเซ็ตสเต็ปเสมือนจริง (Reset Sandbox)", use_container_width=True):
            st.session_state.checkout_url = None
            st.session_state.payment_success = False
            st.session_state.selected_contract = ""
            st.session_state.customer_email = ""
            st.rerun()
