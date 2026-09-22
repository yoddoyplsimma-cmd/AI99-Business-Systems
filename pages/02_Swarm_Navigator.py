import streamlit as st

# 1. ตั้งค่าหน้าจอแบบกว้าง (Wide Mode)
st.set_page_config(
    page_title="AI99 Swarm Navigator | Bespoke Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. ปรับแต่งดีไซน์หรูหรา Kingsman Luxury (Glassmorphism & Gold Accents)
st.markdown("""
<style>
    /* ธีมพื้นหลังโทนดาร์กหรูหรา */
    .stApp {
        background-color: #0b0f19;
        color: #e2e8f0;
    }
    
    /* กล่องคอนโซลฝั่งขวา (Glass Card) */
    .glass-panel {
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(212, 175, 55, 0.35);
        border-radius: 12px;
        padding: 26px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.45);
        margin-bottom: 20px;
    }
    
    /* หัวเรื่องสีทอง */
    .gold-title {
        color: #d4af37;
        font-family: 'Cinzel', 'Trajan Pro', serif;
        letter-spacing: 1.5px;
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 4px;
    }
    
    .badge-legal {
        background: rgba(212, 175, 55, 0.12);
        border: 1px solid #d4af37;
        color: #f1f5f9;
        padding: 6px 12px;
        border-radius: 6px;
        font-size: 11px;
        letter-spacing: 0.5px;
        display: inline-block;
        margin-bottom: 16px;
    }
</style>
""", unsafe_allow_html=True)

# 3. จัดสัดส่วนหน้าจอ 2 คอลัมน์ (ซ้ายเว้นโปร่ง / ขวาวางแผงคอนโซล)
col_left, col_right = st.columns([1, 1.2])

with col_left:
    st.markdown("### 🌐 AI99 Swarm Global Node")
    st.caption("Autonomous Deep Research & Public Domain Verification")
    st.info("ระบบปฏิบัติการ Swarm Autonomous Intelligence พร้อมรับโจทย์ภารกิจเจาะลึกภาคธุรกิจข้ามพรมแดน")

with col_right:
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    
    st.markdown('<div class="gold-title">AI99 SWARM NAVIGATOR</div>', unsafe_allow_html=True)
    st.caption("Autonomous Deep Research Agent | Bespoke Intelligence")
    st.markdown('<div class="badge-legal">🛡️ 100% Legal Public Domain Intelligence (OSINT Compliant)</div>', unsafe_allow_html=True)
    
    # 1. ระบบเลือกภาษา
    lang = st.selectbox(
        "Select Language / เลือกภาษาหน้าบ้าน:",
        ["🇬🇧 English (UK)", "🇩🇪 Deutsch", "🇹🇭 ภาษาไทย", "🇮🇹 Italiano", "🇪🇸 Español", "🇫🇷 Français"]
    )
    
    # 2. อีเมลทางการของผู้สั่งซื้อ
    buyer_email = st.text_input(
        "Official Buyer Email (ช่องทางรับไฟล์ Excel และหนังสือนำส่ง):",
        placeholder="executive@company.com"
    )
    
    # 3. พื้นที่เป้าหมาย
    country = st.selectbox(
        "Target Jurisdiction / ประเทศหรือภูมิภาคเป้าหมาย:",
        ["Vietnam (เวียดนาม)", "Thailand (ไทย)", "Singapore (สิงคโปร์)", "Indonesia (อินโดนีเซีย)", "Malaysia (มาเลเซีย)", "United Kingdom (สหราชอาณาจักร)", "United States (สหรัฐฯ)", "Other (ระบุในโจทย์)"]
    )
    
    # 4. กล่องป้อนโจทย์อิสระ
    directive = st.text_area(
        "Bespoke Directive (พิมพ์โจทย์ความต้องการธุรกิจของท่านอย่างอิสระ):",
        placeholder="เช่น: ต้องการหาโกดังห้องเย็น ขอเบอร์โทรตรงฝ่ายขาย และประมาณการราคาค่าเช่าต่อตารางเมตร ไม่เอาบริษัทนายหน้า",
        height=100
    )
    
    # 5. เลือกระดับแพ็กเกจ
    st.markdown("---")
    st.markdown("**Select Mission Tier / เลือกขนาดแพ็กเกจ:**")
    tier_choice = st.radio(
        "ขนาดโควตาข้อมูลที่ต้องการ:",
        [
            "Tier 1: สูงสุด 300 กิจการ — £249.95 (ส่งมอบภายใน 24 ชม.)",
            "Tier 2: 301 – 500 กิจการ — £349.95 (ส่งมอบภายใน 24 ชม.) [แนะนำ]",
            "Tier 3: 501 – 1,000 กิจการ — £499.95 (ส่งมอบ 24–48 ชม.)",
            "⚡ Express Fast-Track (งานด่วน 2–3 ชม.) — £399.95+"
        ],
        index=0
    )
    
    # 6. คัดกรองบุริมสิทธิ์กรณีข้อมูลเกินเพดาน
    st.markdown("**กรณีข้อมูลในพื้นที่เป้าหมายมีมากกว่าโควตา จัดลำดับคัดเลือกแบบใด?**")
    priority_filter = st.selectbox(
        "Priority Selection Criteria:",
        [
            "เกรด A / ชั้นนำระดับอุตสาหกรรม (Top Enterprise, ISO / Standard Certified)",
            "ใกล้จุดยุทธศาสตร์หลัก (Near Deep Sea Ports, Cargo Airports, Industrial Hubs)",
            "ช่องทางติดต่อสมบูรณ์สูงสุด (Active Direct Phone, Executive Email, Verified Web)",
            "กระจายสัดส่วนเท่ากันทั่วประเทศ (National Geographic Spread)",
            "อื่นๆ (ระบุเพิ่มในกล่องโจทย์ด้านบน)"
        ]
    )
    
    st.markdown("---")
    
    # 7. 2 ปุ่มมหัศจรรย์ทางกฎหมาย
    st.markdown("**Legal Agreements & Mandatory Consent:**")
    legal_agree_1 = st.checkbox(
        "I agree to the Terms of Service, OSINT Public Domain Compliance, and Privacy Policy."
    )
    legal_agree_2 = st.checkbox(
        "To the fullest extent permitted by applicable law, all fees are strictly non-refundable once custom intelligence execution has commenced."
    )
    
    # 8. กลไกปลดล็อกปุ่มชำระเงิน
    is_ready = legal_agree_1 and legal_agree_2 and (len(buyer_email.strip()) > 5) and (len(directive.strip()) > 5)
    
    if is_ready:
        st.success("✅ ระบบตรวจสอบความพร้อมสมบูรณ์: ปลดล็อกช่องทางชำระเงินและปล่อย Swarm แล้ว")
        if st.button("🚀 Authorize Swarm & Pay (ชำระเงินและเริ่มปฏิบัติการ)", use_container_width=True):
            st.info(f"เริ่มการเชื่อมต่อ Secure Checkout สำหรับ: {buyer_email} | กำลังจัดเตรียมคิวขุนศึก...")
    else:
        st.warning("⚠️ กรุณากรอกอีเมล, ระบุโจทย์ และติ๊กยอมรับข้อตกลงทางกฎหมายครบทั้ง 2 ข้อ เพื่อปลดล็อกปุ่มชำระเงิน")
        st.button("🔒 Authorize Swarm & Pay (ระบบถูกล็อก)", disabled=True, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

