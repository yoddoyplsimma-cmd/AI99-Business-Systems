import streamlit as st
import urllib.parse
import time
from datetime import datetime

# ==========================================================
# 1. การตั้งค่าระบบหลัก, ราคา $140 / 4 เดือน และท่อรับเงิน
# ==========================================================
AMAZON_AFFILIATE_TAG = "ybcai99garden-20"

# ท่อรับเงินจริง (รองรับแก้ไขลิงก์และเบอร์พร้อมเพย์ได้ตลอด)
STRIPE_CHECKOUT_URL = "https://buy.stripe.com/your_actual_stripe_link" 
PROMPTPAY_ID = "0812345678"  # เบอร์โทร หรือ PromptPay ID ของพี่ยอด
PRICE_USD = 140.00
PRICE_THB = 4900.00
ACCESS_PERIOD_DAYS = 120  # สิทธิ์เข้าถึง 4 เดือนเต็ม (1 ไตรมาส)

st.set_page_config(
    page_title="AI99 Garden Spatial System",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling สไตล์คลีนโมเดิร์น
st.markdown("""
    <style>
    .main-title { font-size: 2.1rem; font-weight: 800; color: #1b4d3e; margin-bottom: 0px; }
    .sub-title { font-size: 1.0rem; color: #555; margin-bottom: 20px; }
    .card-box { background-color: #f8faf8; border: 1px solid #dcdfdc; border-radius: 12px; padding: 18px; margin-bottom: 15px; }
    .spec-tag { background-color: #e8f5e9; color: #2e7d32; font-weight: bold; padding: 4px 10px; border-radius: 6px; font-size: 0.85rem; margin-right: 5px; }
    .legal-box { background-color: #fff8e1; border-left: 5px solid #ffa000; padding: 15px; border-radius: 6px; margin: 15px 0px; font-size: 0.95rem; }
    .guide-bubble { background-color: #e8f0fe; border-left: 4px solid #1a73e8; padding: 12px; border-radius: 6px; margin-bottom: 10px; font-size: 0.9rem; }
    </style>
""", unsafe_allow_html=True)

# ==========================================================
# 2. ฐานข้อมูลสเปกสำเร็จรูป (MASTER BOM DATASET)
# ==========================================================
CATALOG = {
    "STYLE-BAL-01": {
        "title_th": "สวนผักสลัดแนวตั้งระเบียงคอนโด (Verdant Balcony Kit)",
        "title_en": "Minimalist Vertical Balcony Salad Kit",
        "category": "Balcony Micro-Space",
        "dimensions": {"width": 1.20, "height": 2.00, "depth": 0.45},
        "default_items": [
            {"id": "rack", "name": "โครงชั้นวางกัลวาไนซ์ 4-5 ชั้น ทรง Slim", "qty": 1, "price": 45.0, "search": "vertical garden wall planter rack outdoor"},
            {"id": "planter", "name": "รางปลูกผักสลัด Food-grade ทน UV", "qty": 4, "price": 8.0, "search": "rectangular planter box UV resistant"},
            {"id": "drip", "name": "ชุดระบบน้ำหยดอัตโนมัติ Micro-drip", "qty": 1, "price": 18.5, "search": "automatic micro drip irrigation kit balcony"},
            {"id": "soil", "name": "ดินปลูกสูตรมินิมอลระบายน้ำไว (50L)", "qty": 2, "price": 12.0, "search": "organic potting mix perlite lightweight"}
        ]
    },
    "STYLE-MSH-01": {
        "title_th": "สมาร์ทฟังกิพอด ตู้เห็ดในร่มกินได้ (Smart Fungi Pod)",
        "title_en": "Indoor Micro Mushroom Chamber",
        "category": "Mushroom Chamber",
        "dimensions": {"width": 0.50, "height": 0.70, "depth": 0.40},
        "default_items": [
            {"id": "chamber", "name": "ตู้โหลแก้ว/อะคริลิก คุมความชื้นมินิมอล", "qty": 1, "price": 55.0, "search": "mushroom fruiting chamber grow tent"},
            {"id": "humidifier", "name": "เครื่องพ่นหมอก Ultrasonic + เซนเซอร์", "qty": 1, "price": 28.0, "search": "ultrasonic mist maker with humidity controller"},
            {"id": "spores", "name": "ก้อนเชื้อเห็ดพรีเมียม (Oyster/Lion's Mane)", "qty": 4, "price": 6.5, "search": "organic mushroom grow kit lion mane oyster"},
            {"id": "light", "name": "ไฟ LED Bar 5W สเปกตรัมขาว", "qty": 1, "price": 14.0, "search": "small indoor led grow light bar for plants"}
        ]
    },
    "STYLE-IND-01": {
        "title_th": "ชั้นวางไม้และไฟปลูกในห้องรับแขก (Living Plant Shelf)",
        "title_en": "Living Room Aesthetic Greenery Stand",
        "category": "Indoor Greenery",
        "dimensions": {"width": 1.00, "height": 1.60, "depth": 0.35},
        "default_items": [
            {"id": "wood_rack", "name": "ชั้นวางไม้โครงเหล็กนอร์ดิก 4 ชั้น", "qty": 1, "price": 62.0, "search": "tiered plant stand indoor metal wood tall"},
            {"id": "grow_light", "name": "ไฟ Grow Light ซ่อนใต้ชั้น Full Spectrum", "qty": 3, "price": 15.0, "search": "under shelf grow lights full spectrum warm white"},
            {"id": "pots", "name": "กระถางเซรามิกมินิมอลพร้อมจานรอง", "qty": 6, "price": 7.0, "search": "ceramic plant pots with drainage hole saucer modern"}
        ]
    },
    "STYLE-FYD-01": {
        "title_th": "แผงสวนแนวตั้งระแนงหน้าบ้าน (Front Entrance Green Wall)",
        "title_en": "Front Yard Compact Trellis System",
        "category": "Front Yard",
        "dimensions": {"width": 1.80, "height": 1.80, "depth": 0.50},
        "default_items": [
            {"id": "trellis", "name": "แผงระแนงเหล็กโมดูลาร์ตั้งพื้น พ่นกันสนิม", "qty": 1, "price": 78.0, "search": "freestanding garden trellis wall panel metal"},
            {"id": "hook_pots", "name": "กระถางแขวนระบบ Hook Lock เก็บน้ำสำรอง", "qty": 12, "price": 4.5, "search": "hanging wall planter pots self watering hook"},
            {"id": "timer_drip", "name": "ระบบน้ำหยด PE พร้อมไทม์เมอร์ก๊อกน้ำ", "qty": 1, "price": 24.0, "search": "outdoor faucet hose timer with drip distribution tubing"}
        ]
    }
}

def get_amazon_link(keyword):
    encoded = urllib.parse.quote_plus(keyword)
    return f"https://www.amazon.com/s?k={encoded}&tag={AMAZON_AFFILIATE_TAG}"

# ==========================================================
# 3. ตัวคุมตรรกะ & ป้อมความปลอดภัย & AI ไกด์นำทัวร์
# ==========================================================
def secure_ai_guide(user_query, active_style_data):
    """
    ระบบคุมตรรกะ ป้องกัน Prompt Injection และสกัดกั้นการยิงแฮก
    ตอบเฉพาะบริบทการใช้งานในเว็บและสเปกจริงเท่านั้น (ต้นทุน $0.00)
    """
    now = time.time()
    # ดักการยิงรัว (Anti-Spam / Rate Limiting)
    if "last_request_time" not in st.session_state:
        st.session_state.last_request_time = 0
        st.session_state.req_count = 0

    if now - st.session_state.last_request_time < 2.0:
        st.session_state.req_count += 1
        if st.session_state.req_count > 4:
            return "⚠️ ระบบตรวจพบคำขอถี่เกินไป กรุณารอสักครู่เพื่อความปลอดภัยของระบบครับ"
    else:
        st.session_state.req_count = 0

    st.session_state.last_request_time = now

    # สกัดกั้นคำสั่งแฮก / Jailbreak
    blacklist = ["ignore previous", "hack", "api key", "password", "system prompt", "database", "token", "root"]
    if any(b in user_query.lower() for b in blacklist):
        return "🛡️ ขออภัยครับ ระบบอนุญาตให้สอบถามเฉพาะข้อมูลสถาปัตยกรรมจัดสวนและวิธีใช้งานในหน้าเว็บนี้เท่านั้น"

    q = user_query.lower()
    title = active_style_data["title_th"]
    dim = active_style_data["dimensions"]

    if "วิธีใช้" in q or "ทำยังไง" in q or "ทัวร์" in q or "start" in q:
        return "🚩 **ขั้นตอนง่ายๆ 3 สเต็ป:**\n1. เลือกสไตล์สวนที่ชอบด้านบน แล้วเปิดกล้องถ่ายมุมห้องจริง\n2. เลื่อนลงมาปรับแต่งทรงกระถาง สี และจำนวนชิ้นในตาราง\n3. กดสั่งซื้อของผ่าน Amazon หรือปลดล็อกพิมพ์เขียวเต็มฉบับ 4 เดือนที่ปุ่มด้านล่างได้เลยครับ"
    elif "ขนาด" in q or "พื้นที่" in q or "กว้าง" in q:
        return f"📐 สไตล์ **{title}** ใช้ขนาดมาตรฐาน กว้าง {dim['width']}ม. x สูง {dim['height']}ม. x ลึก {dim['depth']}ม. เหมาะสำหรับพื้นที่จำกัดครับ"
    elif "กระถาง" in q or "สลับ" in q or "เปลี่ยน" in q:
        return "💡 ท่านสามารถเลือกทรงกระถาง (กลม, เหลี่ยม, รางยาว) และเปลี่ยนโทนสีได้ที่แผงข้อ 2 รายการค้นหา Amazon จะปรับให้ตรงรุ่นอัตโนมัติครับ"
    elif "อายุ" in q or "4 เดือน" in q or "ราคา" in q:
        return f"💳 แพ็กเกจ Seasonal Pass ราคา ${PRICE_USD:.2f} (฿{PRICE_THB:,.0f}) ให้สิทธิ์เข้าถึงพิมพ์เขียวและสเปกระบบ 4 เดือนเต็ม (120 วัน) ตามรอบฤดูกาลปลูกครับ"
    else:
        return f"🌿 AI ไกด์พร้อมช่วยเหลือครับ สำหรับสไตล์ **{title}** ท่านสามารถปรับลดจำนวนอุปกรณ์ที่ไม่ต้องการออกได้ที่ตารางด้านล่างเลยครับ"

# ==========================================================
# 4. แถบข้าง: AI ไกด์แนะนำการใช้งาน
# ==========================================================
with st.sidebar:
    st.markdown("### 🤖 ผู้ช่วยแนะนำระบบ (AI Guide)")
    st.caption("ระบบคุมตรรกะความปลอดภัย: Zero-Hallucination Guard")
    
    # ปุ่มด่วนสำหรับลูกค้ากดถาม
    st.write("**คำถามยอดนิยม:**")
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        ask_how = st.button("🚩 วิธีใช้งานเว็บ", use_container_width=True)
    with col_b2:
        ask_dim = st.button("📐 เช็กขนาดพื้นที่", use_container_width=True)
        
    col_b3, col_b4 = st.columns(2)
    with col_b3:
        ask_pot = st.button("🪴 ปรับทรงกระถาง", use_container_width=True)
    with col_b4:
        ask_pass = st.button("⏳ สิทธิ์ 4 เดือน", use_container_width=True)

    if "guide_msg" not in st.session_state:
        st.session_state.guide_msg = "ยินดีต้อนรับครับ! เลือกสไตล์สวนที่ต้องการ แล้วกดปุ่มถามด้านบน หรือพิมพ์สอบถามได้ตลอดเวลาครับ"

    if ask_how:
        st.session_state.guide_msg = secure_ai_guide("วิธีใช้งาน", CATALOG["STYLE-BAL-01"])
    elif ask_dim:
        st.session_state.guide_msg = secure_ai_guide("ขนาดพื้นที่", CATALOG["STYLE-BAL-01"])
    elif ask_pot:
        st.session_state.guide_msg = secure_ai_guide("กระถาง", CATALOG["STYLE-BAL-01"])
    elif ask_pass:
        st.session_state.guide_msg = secure_ai_guide("4 เดือน", CATALOG["STYLE-BAL-01"])

    custom_ask = st.text_input("พิมพ์ถาม AI ไกด์:", placeholder="พิมพ์คำถามที่นี่...")
    if st.button("ส่งคำถาม", use_container_width=True):
        if custom_ask:
            st.session_state.guide_msg = secure_ai_guide(custom_ask, CATALOG["STYLE-BAL-01"])

    st.markdown(f"<div class='guide-bubble'>{st.session_state.guide_msg}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### ⚙️ ข้อมูลระบบ")
    st.caption(f"Affiliate Partner Tag: `{AMAZON_AFFILIATE_TAG}`")
    st.caption("Data Anchor: Master BOM NotebookLM Vault")

# ==========================================================
# 5. ส่วนหัวของเว็บ (HEADER)
# ==========================================================
st.markdown("<div class='main-title'>🌿 ระบบคำนวณและออกแบบจัดสวนอัจฉริยะ AI99</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>คำนวณสัดส่วนพื้นที่ตรงรุ่น • ปรับแต่งทรงและสีตามต้องการ • สั่งซื้อชุดอุปกรณ์ครบวงจร</div>", unsafe_allow_html=True)

# ==========================================================
# 6. สเต็ปที่ 1: เลือกสไตล์และสแกนพื้นที่ (STYLE & SCAN)
# ==========================================================
st.markdown("### 1. เลือกสไตล์สวนที่ต้องการ")

style_keys = list(CATALOG.keys())
selected_key = st.selectbox(
    "รูปแบบสไตล์มาตรฐานที่ผ่านการคำนวณแล้ว:",
    style_keys,
    format_func=lambda x: f"{CATALOG[x]['category']} - {CATALOG[x]['title_th']}"
)

current_style = CATALOG[selected_key]
dim = current_style["dimensions"]

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(f"""
    <div class='card-box'>
        <h4>📌 สเปกมิติมาตรฐาน (Standard Dimension)</h4>
        <span class='spec-tag'>กว้าง: {dim['width']} เมตร</span>
        <span class='spec-tag'>สูง: {dim['height']} เมตร</span>
        <span class='spec-tag'>ลึก: {dim['depth']} เมตร</span>
        <p style='margin-top: 12px; color: #555; font-size: 0.9rem;'>
            หมวดหมู่: <b>{current_style['category']}</b><br>
            ชื่อสถาปัตยกรรม: {current_style['title_th']}
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("#### 📷 ถ่ายภาพหรือสแกนพื้นที่จริงของท่าน")
    cam_mode = st.radio("เลือกช่องทางถ่ายภาพ:", ["เปิดกล้องสด (Camera)", "อัปโหลดรูปภาพ (Upload)"], horizontal=True)
    if cam_mode.startswith("เปิดกล้อง"):
        st.camera_input("สแกนมุมระเบียงหรือห้องที่ต้องการจัด")
    else:
        st.file_uploader("เลือกไฟล์รูปภาพพื้นที่บ้าน", type=["jpg", "png", "jpeg"])

st.markdown("---")

# ==========================================================
# 7. สเต็ปที่ 2: แผงปรับแต่งสินค้า (INTERACTIVE BOM CUSTOMIZER)
# ==========================================================
st.markdown("### 2. ปรับแต่งรูปทรง สี และจำนวนอุปกรณ์ (Interactive Customizer)")

col_opt1, col_opt2 = st.columns(2)

with col_opt1:
    pot_shape = st.selectbox(
        "เลือกรูปทรงกระถาง / รางปลูก (Planter Style):",
        ["รางยาวมินิมอล (Rectangular Trough)", "ทรงกระบอกโมเดิร์น (Cylinder)", "สี่เหลี่ยมลูกบาศก์ (Square Cube)", "ทรงกลมคลาสสิก (Round Pot)"]
    )

with col_opt2:
    pot_color = st.selectbox(
        "เลือกโทนสีวัสดุ (Color & Texture):",
        ["ดำด้านลอฟท์ (Matte Black)", "ขาวคลีนมินิมอล (Matte White)", "เทาคอนกรีตโมเดิร์น (Concrete Grey)", "ดินเผาธรรมชาติ (Terracotta)"]
    )

st.markdown("#### 📦 ตารางรายการอุปกรณ์ในเซ็ต (Bill of Materials)")

if "quantities" not in st.session_state:
    st.session_state.quantities = {}

total_estimated = 0.0

for item in current_style["default_items"]:
    item_id = f"{selected_key}_{item['id']}"
    if item_id not in st.session_state.quantities:
        st.session_state.quantities[item_id] = item["qty"]

    c_name, c_qty, c_price, c_aff = st.columns([4, 2, 2, 3])
    
    with c_name:
        display_name = item["name"]
        if item["id"] in ["planter", "pots", "hook_pots"]:
            display_name = f"{item['name']} [{pot_shape.split(' ')[0]} - {pot_color.split(' ')[0]}]"
        st.write(f"**{display_name}**")
        st.caption(f"ประมาณการ: ${item['price']:.2f} / ชิ้น")
        
    with c_qty:
        qty = st.number_input(
            f"จำนวน ({item['id']})", 
            min_value=0, 
            max_value=50, 
            value=st.session_state.quantities[item_id], 
            key=f"input_{item_id}",
            label_visibility="collapsed"
        )
        st.session_state.quantities[item_id] = qty
        
    with c_price:
        subtotal = qty * item["price"]
        total_estimated += subtotal
        st.write(f"**${subtotal:.2f}**")
        
    with c_aff:
        # ลิงก์ตรงไป Amazon พร้อมผูก Tag เพื่อดักคุกกี้ 24 ชั่วโมง
        query = f"{item['search']} {pot_color.split(' ')[0]}"
        st.link_button("ดูบน Amazon ↗", get_amazon_link(query))

st.markdown("---")

# ==========================================================
# 8. สเต็ปที่ 3: สรุปยอด และท่อรับเงินจริง ($140 / 4 เดือน)
# ==========================================================
col_sum, col_buy = st.columns([1, 1])

with col_sum:
    st.markdown(f"### ราคารวมอุปกรณ์โดยประมาณ: `${total_estimated:.2f}`")
    st.caption("ราคาสินค้าจริงขึ้นอยู่กับราคาผู้ขายบน Amazon ณ วันที่สั่งซื้อ")

with col_buy:
    search_all = f"{current_style['category']} {pot_color.split(' ')[0]}"
    st.link_button("🛒 สั่งซื้ออุปกรณ์ชุดนี้ทั้งหมดบน Amazon (One-Click)", get_amazon_link(search_all), use_container_width=True)

# ----------------------------------------------------------
# ส่วนสัญญา 2 ปุ่มมหัศจรรย์ และ ท่อชำระเงินจริง
# ----------------------------------------------------------
st.markdown(f"""
<div class='legal-box'>
    <b>⚖️ ข้อตกลงสิทธิ์การใช้งาน Seasonal Access Pass (${PRICE_USD:.2f} / 1 ไตรมาส 4 เดือน):</b><br>
    - สิทธิ์นี้ครอบคลุมการเข้าถึงไฟล์พิมพ์เขียว แผนผังระบบ และการคำนวณสเปกสถาปัตยกรรมเป็นเวลา <b>{ACCESS_PERIOD_DAYS} วัน (4 เดือนเต็ม)</b><br>
    - เมื่อครบกำหนด 4 เดือน สิทธิ์จะสิ้นสุดลงโดยอัตโนมัติ หากต้องการใช้งานต่อในฤดูกาลถัดไปสามารถลงทะเบียนใหม่ได้<br>
    - การเข้าถึงระบบถือเป็นการส่งมอบสินทรัพย์ดิจิทัลเสร็จสมบูรณ์ทันที มีผลผูกพันตามกฎหมายธุรกรรมอิเล็กทรอนิกส์
</div>
""", unsafe_allow_html=True)

chk1 = st.checkbox("1. ข้าพเจ้ายอมรับข้อตกลงการให้บริการ และนโยบายทรัพย์สินทางปัญญาของ AI99 (Terms of Service)")
chk2 = st.checkbox("2. ข้าพเจ้ายืนยันสละสิทธิ์การขอคืนเงินทุกกรณี 100% หลังเข้าถึงระบบ (Strict Non-Refundable Clause)")

if chk1 and chk2:
    st.success("✅ ยืนยันข้อกำหนดเรียบร้อย ปลดล็อกท่อชำระเงินสิทธิ์ 4 เดือน")
    tab_global, tab_local = st.tabs([f"💳 บัตรเครดิต/เดบิต สากล (Stripe ${PRICE_USD:.2f})", f"📱 สแกนจ่ายพร้อมเพย์ไทย (PromptPay ฿{PRICE_THB:,.0f})"])
    
    with tab_global:
        st.write(f"ชำระค่าบริการ Seasonal Pass 4 เดือน ผ่าน Stripe ระบบความปลอดภัยมาตรฐานสากล")
        st.link_button(f"🚀 ชำระเงิน Stripe (${PRICE_USD:.2f} / 4 เดือน)", STRIPE_CHECKOUT_URL, use_container_width=True)
        
    with tab_local:
        st.write(f"ชำระเงินตรงเข้าบัญชีผ่าน PromptPay ยอดชำระ: **฿{PRICE_THB:,.0f}** (สิทธิ์ 4 เดือน)")
        qr_code_url = f"https://promptpay.io/{PROMPTPAY_ID}/{PRICE_THB}.png"
        col_q, col_s = st.columns([1, 1])
        with col_q:
            st.image(qr_code_url, caption=f"PromptPay ID: {PROMPTPAY_ID}", width=220)
        with col_s:
            st.file_uploader("แนบสลิปโอนเงินเพื่อปลดล็อกสิทธิ์:", type=["jpg", "png", "pdf"])
            if st.button("ยืนยันการส่งสลิป"):
                st.info("ระบบได้รับข้อมูลสลิปแล้ว กำลังตรวจสอบเพื่อเปิดสิทธิ์การใช้งาน 4 เดือนครับ")
else:
    st.info("กรุณาทำเครื่องหมายติ๊กถูก 2 ปุ่มด้านบนให้ครบถ้วน เพื่อปลดล็อกท่อชำระเงิน")
