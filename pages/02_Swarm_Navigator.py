import streamlit as st
import base64
import os

# 1. ตั้งค่าหน้าจอแบบกว้าง
st.set_page_config(
    page_title="AI99 Swarm Navigator | Bespoke Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ดึงภาพพื้นหลัง
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

img_base64 = get_base64_image("pages/bg_agent.jpg")
bg_style = f"""
    background: linear-gradient(rgba(11, 15, 25, 0.4), rgba(11, 15, 25, 0.7)), url("data:image/jpeg;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
""" if img_base64 else "background-color: #0b0f19;"

# สไตล์ Kingsman Luxury
st.markdown(f"""
<style>
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    .stApp {{
        {bg_style}
        color: #e2e8f0;
    }}
    
    .glass-panel {{
        background: rgba(15, 23, 42, 0.82);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(212, 175, 55, 0.4);
        border-radius: 12px;
        padding: 26px;
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.6);
        margin-bottom: 20px;
    }}
    
    .gold-title {{
        color: #d4af37;
        font-family: 'Cinzel', 'Trajan Pro', serif;
        letter-spacing: 1.5px;
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 4px;
    }}
    
    .badge-legal {{
        background: rgba(212, 175, 55, 0.15);
        border: 1px solid #d4af37;
        color: #f1f5f9;
        padding: 6px 12px;
        border-radius: 6px;
        font-size: 11px;
        letter-spacing: 0.5px;
        display: inline-block;
        margin-bottom: 16px;
    }}
</style>
""", unsafe_allow_html=True)

# 2. คลังคำศัพท์ Dynamic Engine บริสุทธิ์ 100%
LANG_DATA = {
    "🇬🇧 English": {
        "title": "AI99 SWARM NAVIGATOR",
        "subtitle": "Autonomous Deep Research Agent | Bespoke Intelligence",
        "badge": "🛡️ 100% Legal Public Domain Intelligence (OSINT Compliant)",
        "email_label": "Official Buyer Email (For delivery of Excel dossier & dispatch brief):",
        "target_label": "Target Jurisdiction / Country:",
        "target_options": ["Vietnam", "Thailand", "Singapore", "Indonesia", "Malaysia", "United Kingdom", "United States", "Other (Specify below)"],
        "directive_label": "Bespoke Intelligence Directive:",
        "directive_ph": "E.g., Cold storage logistics facilities, verified direct sales phone numbers, estimated rental rate per sqm. Exclude third-party brokers.",
        "tier_title": "Select Mission Tier / Data Quota:",
        "tier_options": [
            "Tier 1: Up to 300 verified enterprises — £249.95 (24h delivery)",
            "Tier 2: 301 – 500 verified enterprises — £349.95 (24h delivery) [Recommended]",
            "Tier 3: 501 – 1,000 verified enterprises — £499.95 (24–48h delivery)",
            "⚡ Express Fast-Track (2–3h critical sprint) — £399.95+"
        ],
        "priority_title": "Priority Allocation (If target landscape exceeds tier quota):",
        "priority_options": [
            "Grade A / Industry Standard (ISO Certified, Top Tier Market Share)",
            "Strategic Logistics Hubs (Near Deep Sea Ports, Cargo Airports)",
            "Maximum Contact Completeness (Verified Direct Phone & Executive Email)",
            "Geographic Dispersion Across All Regions",
            "Other (Specify in directive)"
        ],
        "legal_header": "Legal Agreements & Mandatory Consent:",
        "legal_1": "I agree to the Terms of Service, OSINT Public Domain Compliance, and Privacy Policy.",
        "legal_2": "To the fullest extent permitted by applicable law, all fees are strictly non-refundable once custom intelligence execution has commenced.",
        "warn_msg": "Please provide buyer email, mission directive, and check both legal consents.",
        "btn_ready": "🚀 Authorize Swarm & Pay",
        "btn_locked": "🔒 Authorize Swarm & Pay (System Locked)",
        "status_running": "Initializing Secure Checkout for:"
    },
    "🇩🇪 Deutsch": {
        "title": "AI99 SWARM NAVIGATOR",
        "subtitle": "Autonomer Deep Research Agent | Maßgeschneiderte Aufklärung",
        "badge": "🛡️ 100% Konform mit öffentlichen OSINT-Vorschriften",
        "email_label": "Offizielle E-Mail-Adresse des Käufers (Für Excel-Dossier und Übergabeschreiben):",
        "target_label": "Zielregion / Land:",
        "target_options": ["Vietnam", "Thailand", "Singapur", "Indonesien", "Malaysia", "Vereinigtes Königreich", "Vereinigte Staaten", "Andere (Unten angeben)"],
        "directive_label": "Maßgeschneiderte Aufklärungsdirektive:",
        "directive_ph": "Z.B.: Kühlhaus-Logistik, Direktnummern der Vertriebsleitung, Mietpreise pro m². Keine Makler.",
        "tier_title": "Missionsstufe / Datenquote auswählen:",
        "tier_options": [
            "Tier 1: Bis zu 300 geprüfte Unternehmen — £249.95 (Lieferung in 24 Std.)",
            "Tier 2: 301 – 500 geprüfte Unternehmen — £349.95 (Lieferung in 24 Std.) [Empfohlen]",
            "Tier 3: 501 – 1.000 geprüfte Unternehmen — £499.95 (24–48 Std.)",
            "⚡ Express Fast-Track (2–3 Std. Express-Sprint) — £399.95+"
        ],
        "priority_title": "Priorisierung (Falls Treffermenge Quota übersteigt):",
        "priority_options": [
            "Klasse A / Industriestandard (ISO-zertifiziert, Marktführer)",
            "Strategische Logistik-Hubs (Nähe Tiefseehäfen, Frachtflughäfen)",
            "Höchste Kontaktdichte (Geprüfte Durchwahlen & Geschäftsführungs-Mail)",
            "Gleichmäßige geografische Verteilung",
            "Sonstiges (In Direktive angeben)"
        ],
        "legal_header": "Rechtliche Vereinbarungen & Pflichtzustimmung:",
        "legal_1": "Ich akzeptiere die AGB, OSINT-Konformität und die Datenschutzrichtlinie.",
        "legal_2": "Soweit gesetzlich zulässig, sind alle Gebühren nach Beginn der Datenanalyse absolut nicht erstattungsfähig.",
        "warn_msg": "Bitte E-Mail, Direktive eingeben und beide Zustimmungen erteilen.",
        "btn_ready": "🚀 Swarm autorisieren & zahlen",
        "btn_locked": "🔒 Swarm autorisieren & zahlen (Gesperrt)",
        "status_running": "Sicherer Checkout wird vorbereitet für:"
    },
    "🇹🇭 ภาษาไทย": {
        "title": "AI99 SWARM NAVIGATOR",
        "subtitle": "ระบบขุนศึกค้นหาข้อมูลเชิงลึกอัตโนมัติ | ปฏิบัติการเฉพาะกิจ",
        "badge": "🛡️ ข้อมูลสาธารณะถูกต้องตามกฎหมาย 100% (OSINT Compliant)",
        "email_label": "อีเมลทางการของผู้สั่งซื้อ (ช่องทางรับไฟล์ Excel และหนังสือนำส่ง):",
        "target_label": "ประเทศหรือภูมิภาคเป้าหมาย:",
        "target_options": ["เวียดนาม", "ไทย", "สิงคโปร์", "อินโดนีเซีย", "มาเลเซีย", "สหราชอาณาจักร", "สหรัฐอเมริกา", "อื่นๆ (ระบุในโจทย์)"],
        "directive_label": "พิมพ์โจทย์ความต้องการธุรกิจของท่านอย่างอิสระ:",
        "directive_ph": "เช่น: ต้องการหาโกดังห้องเย็น ขอเบอร์โทรตรงฝ่ายขาย และประมาณการราคาค่าเช่าต่อตารางเมตร ไม่เอาบริษัทนายหน้า",
        "tier_title": "เลือกขนาดแพ็กเกจข้อมูลที่ต้องการ:",
        "tier_options": [
            "Tier 1: สูงสุด 300 กิจการ — £249.95 (ส่งมอบภายใน 24 ชม.)",
            "Tier 2: 301 – 500 กิจการ — £349.95 (ส่งมอบภายใน 24 ชม.) [แนะนำ]",
            "Tier 3: 501 – 1,000 กิจการ — £499.95 (ส่งมอบ 24–48 ชม.)",
            "⚡ Express Fast-Track (งานด่วน 2–3 ชม.) — £399.95+"
        ],
        "priority_title": "กรณีข้อมูลในพื้นที่เป้าหมายมีมากกว่าโควตา จัดลำดับคัดเลือกแบบใด?",
        "priority_options": [
            "เกรด A / ชั้นนำระดับอุตสาหกรรม (Top Enterprise, ได้รับการรับรองมาตรฐาน ISO)",
            "ใกล้จุดยุทธศาสตร์หลัก (ใกล้ท่าเรือน้ำลึก, สนามบินขนส่งสินค้า, นิคมอุตสาหกรรม)",
            "ช่องทางติดต่อสมบูรณ์สูงสุด (มีเบอร์โทรตรงฝ่ายบริหาร, อีเมลทางการ, เว็บไซต์ชัดเจน)",
            "กระจายสัดส่วนครอบคลุมทั่วประเทศ",
            "อื่นๆ (ระบุเพิ่มเติมในกล่องโจทย์)"
        ],
        "legal_header": "ข้อตกลงและเงื่อนไขการอนุมัติทางกฎหมาย:",
        "legal_1": "ข้าพเจ้ายอมรับข้อกำหนดการให้บริการ, การปฏิบัติตามมาตรฐาน OSINT และนโยบายความเป็นส่วนตัว",
        "legal_2": "ภายใต้ขอบเขตสูงสุดที่กฎหมายอนุญาต ค่าธรรมเนียมทั้งหมดไม่สามารถขอคืนได้ทุกกรณีเมื่อเริ่มรันระบบ",
        "warn_msg": "กรุณากรอกอีเมล ระบุโจทย์ และติ๊กยอมรับข้อตกลงทั้ง 2 ข้อเพื่อปลดล็อกปุ่มชำระเงิน",
        "btn_ready": "🚀 ชำระเงินและเริ่มปฏิบัติการ Swarm",
        "btn_locked": "🔒 ชำระเงินและเริ่มปฏิบัติการ (ระบบถูกล็อก)",
        "status_running": "กำลังเตรียมเปิดช่องทางชำระเงินปลอดภัยสำหรับ:"
    }
}

# จัด Layout 2 ฝั่ง
col_left, col_right = st.columns([1.1, 1.1])

with col_left:
    st.write("") # ปล่อยโปร่งโชว์ตัวแบบและวิวมหานคร

with col_right:
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    
    # 1. ระบบเลือกภาษา (Default: English)
    selected_lang = st.selectbox(
        "Select Interface Language / เลือกภาษา:",
        list(LANG_DATA.keys()),
        index=0
    )
    
    txt = LANG_DATA[selected_lang]
    
    st.markdown(f'<div class="gold-title">{txt["title"]}</div>', unsafe_allow_html=True)
    st.caption(txt["subtitle"])
    st.markdown(f'<div class="badge-legal">{txt["badge"]}</div>', unsafe_allow_html=True)
    
    # 2. Email ผู้สั่งซื้อ
    buyer_email = st.text_input(txt["email_label"], placeholder="executive@company.com")
    
    # 3. พื้นที่เป้าหมาย
    country = st.selectbox(txt["target_label"], txt["target_options"])
    
    # 4. Directive โจทย์อิสระ
    directive = st.text_area(txt["directive_label"], placeholder=txt["directive_ph"], height=95)
    
    # 5. Mission Tier
    st.markdown("---")
    st.markdown(f"**{txt['tier_title']}**")
    tier_choice = st.radio("Tier:", txt["tier_options"], index=0, label_visibility="collapsed")
    
    # 6. Priority Filter
    st.markdown(f"**{txt['priority_title']}**")
    priority_filter = st.selectbox("Priority:", txt["priority_options"], label_visibility="collapsed")
    
    st.markdown("---")
    
    # 7. Dual Legal Consent Gate
    st.markdown(f"**{txt['legal_header']}**")
    legal_agree_1 = st.checkbox(txt["legal_1"])
    legal_agree_2 = st.checkbox(txt["legal_2"])
    
    # 8. กลไกปลดล็อกปุ่มชำระเงิน
    is_ready = legal_agree_1 and legal_agree_2 and (len(buyer_email.strip()) > 5) and (len(directive.strip()) > 5)
    
    if is_ready:
        st.success("✅ Protocol Ready")
        if st.button(txt["btn_ready"], use_container_width=True):
            st.info(f"{txt['status_running']} {buyer_email}")
    else:
        st.warning(f"⚠️ {txt['warn_msg']}")
        st.button(txt["btn_locked"], disabled=True, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)
