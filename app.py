import streamlit as st

# ตั้งค่าหน้าเว็บให้ดูเป็นมืออาชีพ
st.set_page_config(page_title="AI99 Business Systems", layout="centered")

# --- ส่วนหัวของอาณาจักร AI99 ---
st.title("🚀 AI99 Business Systems")
st.subheader("ระบบจัดการงานวิจัยและวิศวกรรมระดับโลก")
st.write("ยินดีต้อนรับท่าน CEO พี่ยอด เข้าสู่ระบบการจัดการข้อมูลเชิงลึก")
# --- ติดตั้งสายพานเชื่อมเงิน (บรรทัดนี้ต้องมีครับบอส!) ---
stripe.api_key = st.secrets["SKEY"]
# --- พิกัดการขาย (กระดาษแผ่นที่ 1) ---
st.divider()
st.markdown("### 💎 แพ็กเกจการลงทุน (AI99 Research)")
col1, col2, col3 = st.columns(3)
col1.metric("USD", "$96.99")
col2.metric("GBP", "£165")
col3.metric("EUR", "€165")

# --- พิกัดพวงมาลัย (USD, GBP, EUR) ---
currency = st.radio("เลือกสกุลเงิน:", ["USD", "GBP", "EUR"])

# --- ตั้งราคา (หน่วยเป็นสตางค์) ---
prices = {"USD": 9699, "GBP": 16500, "EUR": 16500}

# --- บรรทัดที่ 28 (ปุ่มชำระเงินที่ใช้งานได้จริง) ---
if st.button("ชำระเงินและดาวน์โหลดเอกสารทองคำ"):
    try:
        # สร้างพิกัดวาร์ปไปหน้า Stripe
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': currency.lower(),
                    'product_data': {'name': 'เอกสารทองคำ AI99'},
                    'unit_amount': prices[currency],
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://google.com',
            cancel_url='https://google.com',
        )
        # พอกดปุ่มปุ๊บ ให้ลิงก์ปรากฏขึ้นมาเพื่อไปหน้าจ่ายเงิน
        st.success("สร้างรายการสำเร็จ!")
        st.markdown(f'<a href="{checkout_session.url}" target="_self" style="background-color: #008CBA; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">จิ้มตรงนี้เพื่อไปหน้าชำระเงิน (Stripe)</a>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"เกิดข้อผิดพลาด: {e}")
