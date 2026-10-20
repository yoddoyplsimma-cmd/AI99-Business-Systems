import streamlit as st
import urllib.parse
from datetime import datetime

# ==========================================================
# 1. การตั้งค่าระบบหลัก และท่อรับเงิน (CONFIG & GATEWAYS)
# ==========================================================
AMAZON_AFFILIATE_TAG = "ybcai99garden-20"
# หยอดลิงก์ Stripe หรือ Gumroad ของพี่ยอดลงในช่องนี้
DIRECT_PAYMENT_URL = "https://buy.stripe.com/test_your_link_here" 

st.set_page_config(
    page_title="AI99 Garden Spatial System",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling ให้หน้าตาดูโมเดิร์น เรียบหรู
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; font-weight: 800; color: #1b4d3e; margin-bottom: 0px; }
    .sub-title { font-size: 1.05rem; color: #555; margin-bottom: 25px; }
    .card-box { background-color: #f8faf8; border: 1px solid #dcdfdc; border-radius: 12px; padding: 18px; margin-bottom: 15px; }
    .spec-tag { background-color: #e8f5e9; color: #2e7d32; font-weight: bold; padding: 4px 10px; border-radius: 6px; font-size: 0.85rem; }
    .legal-box { background-color: #fff8e1; border-left: 5px solid #ffa000; padding: 15px; border-radius: 6px; margin: 15px 0px; }
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
# 3. แถบควบคุมด้านข้าง (SIDEBAR & SETTINGS)
# ==========================================================
with st.sidebar:
    st.markdown("### ⚙️ การตั้งค่าระบบ")
    lang = st.radio("เลือกภาษา / Language", ["ไทย (TH)", "English (EN)"])
    is_th = lang.startswith("ไทย")
    
    st.markdown("---")
    st.markdown("### 🏢 YBC AI99 System")
    st.caption(f"Affiliate Tracking: `{AMAZON_AFFILIATE_TAG}`")
    st.caption("Core Logic: Zero-Hallucination NotebookLM")

# ==========================================================
# 4. ส่วนหัวของเว็บ (HEADER)
# ==========================================================
title_text = "🌿 ระบบคำนวณและออกแบบจัดสวนอัจฉริยะ AI99" if is_th else "🌿 AI99 Intelligent Garden Spatial System"
sub_text = "คำนวณขนาด ออกแบบสัดส่วนตรงรุ่น พร้อมจัดสเปกชุดอุปกรณ์เสร็จสรรพในคลิกเดียว" if is_th else "Instant micro-space optimization, dimension extraction, and verified hardware BOM."

st.markdown(f"<div class='main-title'>{title_text}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='sub-title'>{sub_text}</div>", unsafe_allow_html=True)

# ==========================================================
# 5. สเต็ปที่ 1: เลือกสไตล์และหมวดหมู่ (STYLE SELECTION)
# ==========================================================
st.markdown("### 1. เลือกสไตล์สวนที่ต้องการ" if is_th else "### 1. Select Preferred Style")

style_keys = list(CATALOG.keys())
selected_key = st.selectbox(
    "รูปแบบสไตล์ที่ผ่านการวิจัยและถอดรหัสแล้ว:" if is_th else "Verified Master Architectural Styles:",
    style_keys,
    format_func=lambda x: f"{CATALOG[x]['category']} - {CATALOG[x]['title_th'] if is_th else CATALOG[x]['title_en']}"
)

current_style = CATALOG[selected_key]
dim = current_style["dimensions"]

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(f"""
    <div class='card-box'>
        <h4>📌 สเปกมิติมาตรฐาน (Standard Spatial Dimension)</h4>
        <span class='spec-tag'>กว้าง (Width): {dim['width']} ม.</span>
        <span class='spec-tag'>สูง (Height): {dim['height']} ม.</span>
        <span class='spec-tag'>ลึก (Depth): {dim['depth']} ม.</span>
        <p style='margin-top: 10px; color: #666; font-size: 0.9rem;'>
            หมวดหมู่: <b>{current_style['category']}</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("#### 📷 สแกนพื้นที่จริงของท่าน" if is_th else "#### 📷 Scan Your Real Space")
    input_method = st.radio("ช่องทางถ่ายภาพ:", ["เปิดกล้องสด (Camera)", "อัปโหลดรูปภาพ (Upload)"], horizontal=True)
    if input_method.startswith("เปิดกล้อง"):
        camera_img = st.camera_input("กดถ่ายภาพมุมระเบียงหรือห้องของท่าน")
    else:
        uploaded_img = st.file_uploader("เลือกไฟล์รูปภาพพื้นที่บ้าน", type=["jpg", "png", "jpeg"])

st.markdown("---")

# ==========================================================
# 6. สเต็ปที่ 2: หน้าปรับแต่งสเปก (INTERACTIVE BOM CUSTOMIZER)
# ==========================================================
st.markdown("### 2. ปรับแต่งอุปกรณ์ตามต้องการ (Interactive BOM Customizer)" if is_th else "### 2. Interactive BOM & Style Customizer")

col_custom1, col_custom2 = st.columns(2)

with col_custom1:
    pot_shape = st.selectbox(
        "รูปทรงกระถาง / รางปลูก (Planter Style):" if is_th else "Planter Form Factor:",
        ["รางยาวมินิมอล (Rectangular Trough)", "ทรงกระบอกโมเดิร์น (Cylinder)", "สี่เหลี่ยมลูกบาศก์ (Square Cube)", "ทรงกลมคลาสสิก (Round Pot)"]
    )

with col_custom2:
    pot_color = st.selectbox(
        "โทนสีวัสดุ (Color & Texture):" if is_th else "Color Finish:",
        ["ดำด้านลอฟท์ (Matte Black)", "ขาวคลีนมินิมอล (Matte White)", "เทาคอนกรีตโมเดิร์น (Concrete Grey)", "ดินเผาธรรมชาติ (Terracotta)"]
    )

st.markdown("#### 📦 รายการวัสดุอุปกรณ์และปรับจำนวน (Item List & Quantities)" if is_th else "#### 📦 Bill of Materials (BOM Table)")

# จัดการ State เก็บจำนวนของแต่ละชิ้น
if "item_quantities" not in st.session_state:
    st.session_state.item_quantities = {}

total_estimated_price = 0.0

for item in current_style["default_items"]:
    item_key = f"{selected_key}_{item['id']}"
    if item_key not in st.session_state.item_quantities:
        st.session_state.item_quantities[item_key] = item["qty"]

    c1, c2, c3, c4 = st.columns([4, 2, 2, 3])
    
    with c1:
        # ปรับชื่อตามทรงและสีที่ลูกค้าเลือก
        display_name = item["name"]
        if item["id"] in ["planter", "pots", "hook_pots"]:
            display_name = f"{item['name']} [{pot_shape.split(' ')[0]} - {pot_color.split(' ')[0]}]"
        st.write(f"**{display_name}**")
        st.caption(f"ประมาณการ: ${item['price']:.2f} / หน่วย")
        
    with c2:
        qty = st.number_input(
            f"จำนวน ({item['id']})", 
            min_value=0, 
            max_value=50, 
            value=st.session_state.item_quantities[item_key], 
            key=f"num_{item_key}",
            label_visibility="collapsed"
        )
        st.session_state.item_quantities[item_key] = qty
        
    with c3:
        subtotal = qty * item["price"]
        total_estimated_price += subtotal
        st.write(f"**${subtotal:.2f}**")
        
    with c4:
        # ปุ่มแฝงคลิกรายชิ้น ดัก Cookie Amazon 24 ชม.
        search_query = f"{item['search']} {pot_color.split(' ')[0]}"
        aff_url = get_amazon_link(search_query)
        st.link_button("ดูบน Amazon ↗", aff_url)

st.markdown("---")

# ==========================================================
# 7. สเต็ปที่ 3: สรุปยอด และท่อรับเงิน (CHECKOUT & LEGAL GATE)
# ==========================================================
col_total, col_action = st.columns([1, 1])

with col_total:
    st.markdown(f"### ราคารวมอุปกรณ์โดยประมาณ: `${total_estimated_price:.2f}`")
    st.caption("ราคาสินค้าจริงขึ้นอยู่กับโปรโมชั่นบน Amazon ณ เวลาที่สั่งซื้อ")

with col_action:
    # ปุ่มซื้อทั้งหมดผ่าน Amazon Tag
    all_keywords = current_style['category'] + " " + pot_color.split(' ')[0]
    st.link_button("🛒 สั่งซื้ออุปกรณ์ชุดนี้ทั้งหมดบน Amazon (One-Click)", get_amazon_link(all_keywords), use_container_width=True)

# ----------------------------------------------------------
# ส่วนข้อตกลง 2 ปุ่มมหัศจรรย์ และ ท่อรับเงินค่าบริการ $99
# ----------------------------------------------------------
st.markdown("""
<div class='legal-box'>
    <b>⚖️ ข้อตกลงการปลดล็อกพิมพ์เขียวสถาปัตยกรรม (AI99 Mandatory Terms):</b><br>
    การเข้าถึงไฟล์พิมพ์เขียว แผนผังระบบ และการคำนวณสัดส่วนสถาปัตยกรรม เป็นการส่งมอบสินทรัพย์ดิจิทัลเสร็จสมบูรณ์ทันที มีผลผูกพันทางอิเล็กทรอนิกส์สากล
</div>
""", unsafe_allow_html=True)

chk_terms = st.checkbox("1. ข้าพเจ้ายอมรับข้อตกลงการให้บริการ และนโยบายทรัพย์สินทางปัญญาของ AI99 (Terms & IP Acceptance)")
chk_refund = st.checkbox("2. ข้าพเจ้ายืนยันสละสิทธิ์การขอคืนเงินทุกกรณี 100% หลังเข้าถึงระบบ (Strict Non-Refundable Clause)")

if chk_terms and chk_refund:
    st.success("✅ เงื่อนไขถูกต้องครบถ้วน ปลดล็อกท่อชำระเงินเรียบร้อย")
    st.link_button("💳 ปลดล็อกพิมพ์เขียวเต็มฉบับ ($99.95 Checkout)", DIRECT_PAYMENT_URL, use_container_width=True)
else:
    st.info("กรุณากดยอมรับเงื่อนไข 2 ปุ่มด้านบนให้ครบถ้วนเพื่อปลดล็อกปุ่มชำระเงินและดาวน์โหลดพิมพ์เขียว")
