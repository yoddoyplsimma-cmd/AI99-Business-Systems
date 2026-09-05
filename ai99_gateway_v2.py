import streamlit as st
import json
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="AI99 Multi-Engine Sandbox & Commercial Gateway",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- STYLING ---
st.markdown("""
<style>
    .reportview-container { background: #0e1117; }
    .stButton>button { width: 100%; border-radius: 6px; height: 3em; font-weight: bold; }
    .metric-card { background-color: #1e222b; border: 1px solid #30363d; border-radius: 8px; padding: 16px; margin-bottom: 12px; }
    .status-badge { display: inline-block; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; font-weight: bold; }
    .badge-active { background-color: #238636; color: white; }
    .badge-standby { background-color: #d29922; color: black; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("⚡ AI99 Multi-Engine Sandbox & Commercial Gateway")
st.caption("Cross-Platform B2B Architecture, Logic Simulator & Commercial Deployment Portal")

st.info("⚠️ **MANDATORY LEGAL ARCHITECTURE NOTICE:** AI99 is a Software and Technology Licensor. All physical installations, wiring, relays, alarms, and suppression actuation must be performed and approved by licensed local contractors.")

st.markdown("---")

# --- ENGINE SELECTOR (MULTI-PROJECT DROPDOWN) ---
col_proj, col_cur = st.columns([2, 1])

with col_proj:
    selected_project = st.selectbox(
        "📦 เลือกโปรเจกต์ที่ต้องการทดสอบและเปิดดีล (Select AI99 Engine):",
        [
            "AI99 EDGE-GUARD 3-in-1 (Boutique Garage & Asset Defense)",
            "AI99 Smart Vision (AI Garden Design & Spatial Scanning)"
        ]
    )

with col_cur:
    currency = st.selectbox(
        "💱 เลือกสกุลเงินในการชำระมัดจำ (Currency):",
        ["USD ($)", "EUR (€)", "GBP (£)", "SGD (S$)", "THB (฿)"]
    )

# --- CURRENCY CONVERTER LOGIC ---
currency_code = currency.split(" ")[0]
rates_from_usd = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "SGD": 1.34,
    "THB": 35.50
}
currency_symbols = {
    "USD": "$",
    "EUR": "€",
    "GBP": "£",
    "SGD": "S$",
    "THB": "฿"
}

st.markdown("---")

# ==============================================================================
# ENGINE 1: EDGE-GUARD 3-IN-1
# ==============================================================================
if "EDGE-GUARD" in selected_project:
    st.markdown("### 🛡️ AI99 EDGE-GUARD: 3-in-1 Threat Neutralization Engine")
    st.markdown('<span class="status-badge badge-active">ACTIVE COMMERCIAL ENGINE (U.S. DEPLOYMENT)</span>', unsafe_allow_html=True)
    st.write("")

    # Video Player Section
    st.subheader("1. สาธิตการทำงานจริง (Visual Proof & Video Stream)")
    video_source_type = st.radio(
        "เลือกช่องทางการเล่นคลิปเดโม:",
        ["วิดีโอตัวอย่างผ่าน URL / Direct Link", "อัปโหลดไฟล์วิดีโอ MP4"],
        horizontal=True
    )
    
    if video_source_type == "วิดีโอตัวอย่างผ่าน URL / Direct Link":
        video_url = st.text_input("ระบุลิงก์วิดีโอ (YouTube / MP4 Cloud Storage):", value="https://www.w3schools.com/html/mov_bbb.mp4")
        if video_url:
            st.video(video_url)
    else:
        uploaded_video = st.file_uploader("เลือกไฟล์วิดีโอ MP4 ของพี่ยอด:", type=["mp4", "mov"])
        if uploaded_video:
            st.video(uploaded_video)
        else:
            st.info("ยังไม่มีการอัปโหลดไฟล์วิดีโอ กรุณาเลือกไฟล์ MP4 เพื่อแสดงผลบนหน้า Sandbox")

    st.markdown("---")

    # Interactive Logic Simulator
    st.subheader("2. ทดสอบจำลองสัญญาณตรรกะระบบ (Interactive Logic Simulator)")
    
    sim_col1, sim_col2, sim_col3 = st.columns(3)

    with sim_col1:
        st.markdown("**🔥 เหตุการณ์ที่ 1: ตรวจจับเพลิงไหม้ EV**")
        st.write("CCTV จับกลุ่มความร้อนสูงผิดปกติเหนือจุดชาร์จ")
        if st.button("🚨 จำลองเปลวไฟ / ความร้อนสูง"):
            st.error("MATCH: Thermal Anomaly Detected (98.4%)")
            st.code("OUTPUT: Relay 01 Triggered [ACTIVE]\nSTATUS: Solenoid Signal Fired (Millisecond)", language="text")
            st.caption("หมายเหตุ: สารดับเพลิงถูกติดตั้งและออกแบบโดยช่างท้องถิ่น")

    with sim_col2:
        st.markdown("**📡 เหตุการณ์ที่ 2: ตัดเน็ต / สัญญาณ Jammer**")
        st.write("ระบบโดนกวนสัญญาณยามวิกาลขณะพบการงัดแงะ")
        if st.button("📻 จำลอง Jammer / สลับยิงรหัสมอส"):
            st.warning("FAILOVER: Network Lost -> RF Failover Engaged")
            st.code("BURST: Morse Radio Signal Emitted\nLIMIT: Auto-cutoff within 5.0s (FCC §15.231)\nIMMOBILIZER: Starter Interrupted", language="text")
            st.caption("หมายเหตุ: สัญญาณวิทยุส่งสั้น ปลอดภัยตามกรอบ FCC")

    with sim_col3:
        st.markdown("**🎙️ เหตุการณ์ที่ 3: สั่งสตาร์ท / วาร์ปรถด้วยเสียง**")
        st.write("ไมโครโฟนปิดตลอดเวลา ฟังเฉพาะเสียงผู้มีสิทธิ์")
        if st.button("🔑 จำลองคำสั่งเสียง Dual-Key"):
            st.success("AUTHENTICATED: Voice Command Verified")
            st.code("BUFFER: Audio Processed in RAM & Wiped\nACTION: Gateway Warmup / Start Authorized", language="text")
            st.caption("หมายเหตุ: ไม่มีการบันทึกเสียงสนทนา ปลอดภัยต่อกฎหมายดักฟัง")

    st.markdown("---")

    # Legal Clickwrap Gatekeeper
    st.subheader("3. ข้อตกลงทางกฎหมายและการยอมรับเงื่อนไข (Legal Clickwrap Gatekeeper)")
    st.write("กรุณาตรวจสอบและทำเครื่องหมายยอมรับข้อตกลงเพื่อปลดล็อกระบบชำระเงินมัดจำ:")

    c1 = st.checkbox("1. ข้าพเจ้าเป็นตัวแทนผู้มีอำนาจลงนามผูกพันในนามบริษัทหรือผู้ซื้อ (Authorized Representative)")
    c2 = st.checkbox("2. ข้าพเจ้ามีสิทธิ์ในกรรมสิทธิ์หรือได้รับอนุญาตเป็นลายลักษณ์อักษรในการต่อระบบเข้าตัวรถและสถานที่ (Vehicle & Property Authorization)")
    c3 = st.checkbox("3. ข้าพเจ้ารับทราบว่า AI99 ขายเฉพาะสิทธิ์การใช้ซอฟต์แวร์และวงจรตรรกะ (Software Licensor) มิใช่ผู้รับเหมาติดตั้งทางกายภาพ")
    c4 = st.checkbox("4. งานติดตั้ง เดินสายไฟ วาล์วดับเพลิง และอุปกรณ์ภายนอกทั้งหมดต้องดำเนินการโดยช่างผู้มีใบอนุญาตในรัฐนั้นๆ (Licensed Local Integrator)")
    c5 = st.checkbox("5. ข้าพเจ้ารับทราบว่าการตรวจจับของ AI เป็นเชิงความน่าจะเป็น (Probabilistic) อาจมี False Positives หรือ False Negatives ได้")
    c6 = st.checkbox("6. ข้าพเจ้ายอมรับว่าฟังก์ชันคลื่นวิทยุสำรอง (Radio Failover) ต้องใช้อุปกรณ์ที่ผ่านเกณฑ์อนุญาตของ FCC")
    c7 = st.checkbox("7. ระบบเสียงถูกตั้งค่าปิดการบันทึกถาวรเป็นค่าเริ่มต้น (Audio Recording OFF by default) เพื่อความถูกต้องตามกฎหมายความเป็นส่วนตัว")
    c8 = st.checkbox("8. ข้าพเจ้ายอมรับข้อกำหนดใน Master Software License Agreement และ State Addenda (AZ / TX / CA / FL) ทุกประการ")

    all_agreed = c1 and c2 and c3 and c4 and c5 and c6 and c7 and c8

    st.markdown("---")

    # Deposit & Pricing Calculation
    st.subheader("4. เปิดดีลและชำระเงินมัดจำสิทธิ์พื้นที่ (Commercial Checkout)")
    
    base_usd_deposit = 1000.0
    converted_deposit = base_usd_deposit * rates_from_usd[currency_code]
    symbol = currency_symbols[currency_code]

    checkout_col1, checkout_col2 = st.columns([1, 1])

    with checkout_col1:
        st.markdown(f"""
        <div class="metric-card">
            <h4>ยอดชำระมัดจำเปิดสิทธิ์พื้นที่ (Territory Deposit)</h4>
            <h2 style="color: #2ea043;">{symbol}{converted_deposit:,.2f} {currency_code}</h2>
            <p style="font-size: 0.85em; color: #8b949e;">(เทียบเท่ามาตรฐาน $1,000.00 USD - เป็นไปตามข้อกำหนด Schedule B)</p>
        </div>
        """, unsafe_allow_html=True)
        
        customer_email = st.text_input("ระบุอีเมลผู้ติดต่อเพื่อรับเอกสารยืนยันสิทธิ์:", placeholder="ceo@company.com")

    with checkout_col2:
        st.write("**สิทธิ์ที่จะได้รับทันทีหลังเปิดดีล:**")
        st.markdown("""
        * สิทธิ์จองโควตาพื้นที่แบบ Exclusive Territory ตามเงื่อนไข Schedule 5
        * เอกสารพิมพ์เขียว I/O Reference Wiring Blueprint สำหรับช่าง
        * สิทธิ์การปรึกษาด้านสถาปัตยกรรมระบบ 1-on-1 โดยตรงกับ CEO
        * รหัสทดสอบระบบและเอกสาร Deployment Certificate ครบชุด
        """)

    if all_agreed and customer_email:
        if st.button(f"🚀 ยืนยันการเปิดดีลและชำระมัดจำ ({symbol}{converted_deposit:,.2f} {currency_code})"):
            st.success("✅ ระบบได้รับข้อมูลเรียบร้อย! ออกใบรับรองสิทธิ์และรหัสตรวจสอบระบบอัตโนมัติ")
            audit_log = {
                "Timestamp": str(datetime.utcnow()),
                "Project": "AI99 EDGE-GUARD 3-in-1",
                "Customer_Email": customer_email,
                "Amount_Paid": f"{converted_deposit:,.2f} {currency_code}",
                "Agreed_Terms": "8/8 Clickwrap Verified",
                "Deployment_ID": "DEP-US-" + datetime.utcnow().strftime("%Y%m%d%H%M%S")
            }
            st.json(audit_log)
    else:
        st.warning("🔒 กรุณาติ๊กยอมรับเงื่อนไขทางกฎหมายครบทั้ง 8 ข้อ และระบุอีเมลเพื่อปลดล็อกปุ่มชำระเงิน")

# ==============================================================================
# ENGINE 2: SMART VISION (GARDEN DESIGN) - COMING SOON / PIPELINE
# ==============================================================================
else:
    st.markdown("### 🌿 AI99 Smart Vision: AI Garden Design & Spatial Scanning")
    st.markdown('<span class="status-badge badge-standby">R&D PIPELINE / DIRECT AFFILIATE INTEGRATION</span>', unsafe_allow_html=True)
    st.write("")

    st.subheader("1. คลิปเดโมระบบสแกนพื้นที่จัดสวน (Demonstration Preview)")
    st.info("ระบบกล้อง AI สแกนวิเคราะห์ภูมิทัศน์และคำนวณพื้นที่สำหรับออกแบบสวนเฉพาะจุด")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")

    st.markdown("---")

    st.subheader("2. สถานะการพัฒนาระบบ (System Pipeline)")
    st.write("""
    โปรเจกต์นี้อยู่ในระหว่างกระบวนการพัฒนาตรรกะ AI ร่วมกับพันธมิตร:
    * **Spatial Scanning Engine:** ระบบประมวลผลพิกัดพื้นที่จัดสวน
    * **Amazon Direct Affiliate Integration:** เชื่อมระบบดึงรายการวัสดุและอุปกรณ์จัดสวนอัตโนมัติ
    * **Generative Landscape Engine:** ระบบจำลองภาพผลลัพธ์หลังจัดสวนเสร็จ
    """)
    
    st.warning("⚠️ ส่วนการจำลองโต้ตอบ (Interactive Simulator) และการเปิดดีลเชิงพาณิชย์ของโปรเจกต์นี้ จะเปิดใช้งานอย่างเป็นทางการหลังเสร็จสิ้นขั้นตอนเชื่อมต่อ API")
