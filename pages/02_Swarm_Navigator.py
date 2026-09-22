import streamlit as st
import base64
import os
import json
import uuid
from datetime import datetime

# 1. ตั้งค่าหน้าจอแบบกว้าง (Wide Mode)
st.set_page_config(
    page_title="AI99 Intelligence Navigator | Bespoke B2B Research",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. ฟังก์ชันแปลงภาพเป็น Base64
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

img_base64 = get_base64_image("pages/bg_agent.jpg")
bg_style = f"""
    background: linear-gradient(rgba(11, 15, 25, 0.45), rgba(11, 15, 25, 0.75)), url("data:image/jpeg;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
""" if img_base64 else "background-color: #0b0f19;"

# 3. สไตล์ Kingsman Luxury Glassmorphism
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
        background: rgba(15, 23, 42, 0.84);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        border: 1px solid rgba(212, 175, 55, 0.4);
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.6);
        margin-bottom: 20px;
    }}
    
    .order-summary-box {{
        background: rgba(10, 16, 30, 0.9);
        border: 1px dashed rgba(212, 175, 55, 0.6);
        border-radius: 8px;
        padding: 16px;
        margin-top: 15px;
        margin-bottom: 15px;
        font-size: 13px;
    }}
    
    .gold-title {{
        color: #d4af37;
        font-family: 'Cinzel', 'Trajan Pro', serif;
        letter-spacing: 1.5px;
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 4px;
    }}
    
    .badge-legal {{
        background: rgba(212, 175, 55, 0.12);
        border: 1px solid #d4af37;
        color: #f1f5f9;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 11px;
        letter-spacing: 0.5px;
        display: inline-block;
        margin-bottom: 14px;
    }}
    
    .compliance-note {{
        color: #94a3b8;
        font-size: 11px;
        margin-top: -10px;
        margin-bottom: 14px;
    }}
</style>
""", unsafe_allow_html=True)

# 4. คลังคำศัพท์ Dynamic Multilingual พร้อม B2B Authority Gate
LANG_DATA = {
    "🇬🇧 English": {
        "title": "AI99 INTELLIGENCE NAVIGATOR",
        "subtitle": "Bespoke Business Research & Verified Data Services",
        "badge": "🛡️ 100% OSINT Compliant | Public Domain Intelligence",
        "company_label": "Company / Entity Name:",
        "email_label": "Official Business Email:",
        "target_label": "Target Jurisdiction / Country:",
        "target_options": ["Vietnam", "Thailand", "Singapore", "Indonesia", "Malaysia", "United Kingdom", "United States", "Other (Specify in directive)"],
        "directive_label": "Bespoke Intelligence Directive:",
        "directive_ph": "E.g., Cold storage logistics facilities, verified direct sales phone numbers, estimated rental rate per sqm. Exclude third-party brokers.",
        "compliance_warn": "⚠️ Do not submit passwords, credentials, confidential third-party information, or unlawfully obtained personal data.",
        "tier_title": "Select Mission Tier / Data Quota:",
        "tier_data": {
            "Tier 1 (£249.95)": {"price": 249.95, "desc": "Up to 300 verified entities (24h delivery)", "window": "Within 24 Hours"},
            "Tier 2 (£349.95) [Recommended]": {"price": 349.95, "desc": "301 – 500 verified entities (24h delivery)", "window": "Within 24 Hours"},
            "Tier 3 (£499.95)": {"price": 499.95, "desc": "501 – 1,000 verified entities (24–48h delivery)", "window": "24–48 Hours"},
            "⚡ Express Fast-Track (£399.95+)": {"price": 399.95, "desc": "Priority execution (2–3h critical delivery)", "window": "2–3 Hours"}
        },
        "priority_title": "Priority Allocation (If target landscape exceeds quota):",
        "priority_options": [
            "Grade A / Industry Standard (ISO Certified, Top Tier)",
            "Strategic Logistics Hubs (Near Deep Sea Ports, Cargo Airports)",
            "Maximum Contact Completeness (Verified Direct Phone & Executive Email)",
            "National Geographic Spread Across All Regions"
        ],
        "summary_title": "📋 Order Summary Snapshot (Pre-Execution)",
        "legal_header": "Legal Agreements & Mandatory Consent:",
        "terms_ver": "Terms v1.0 — Effective 23 September 2026",
        "legal_1": "I confirm that I am acting on behalf of a business or professional entity, that I am authorized to place this order, and that I have read and agree to the Terms of Service (v1.0), Privacy Policy, and applicable data-use requirements.",
        "legal_2": "I expressly authorize AI99 to commence the customized service following payment and acknowledge that, once execution has commenced, fees are non-refundable to the fullest extent permitted by applicable law.",
        "warn_msg": "Please complete all entity fields, directive, and authorize both mandatory declarations.",
        "btn_ready": "🚀 Authorize Intelligence Mission & Pay",
        "btn_locked": "🔒 Authorize Mission & Pay (Locked)"
    },
    "🇩🇪 Deutsch": {
        "title": "AI99 INTELLIGENCE NAVIGATOR",
        "subtitle": "Maßgeschneiderte Unternehmensanalyse & Geprüfte Datendienste",
        "badge": "🛡️ 100% OSINT-konform | Öffentliche Domänenaufklärung",
        "company_label": "Unternehmen / Organisationsname:",
        "email_label": "Offizielle geschäftliche E-Mail-Adresse:",
        "target_label": "Zielregion / Land:",
        "target_options": ["Vietnam", "Thailand", "Singapur", "Indonesien", "Malaysia", "Vereinigtes Königreich", "Vereinigte Staaten", "Andere (In Direktive angeben)"],
        "directive_label": "Maßgeschneiderte Aufklärungsdirektive:",
        "directive_ph": "Z.B.: Kühlhaus-Logistik, Direktnummern der Vertriebsleitung, Mietpreise pro m². Keine Makler.",
        "compliance_warn": "⚠️ Übermitteln Sie keine Passwörter, Zugangsdaten oder unrechtmäßig erlangte personenbezogene Daten.",
        "tier_title": "Missionsstufe / Datenquote auswählen:",
        "tier_data": {
            "Tier 1 (£249.95)": {"price": 249.95, "desc": "Bis zu 300 geprüfte Einheiten (Lieferung in 24 Std.)", "window": "Innerhalb von 24 Stunden"},
            "Tier 2 (£349.95) [Empfohlen]": {"price": 349.95, "desc": "301 – 500 geprüfte Einheiten (Lieferung in 24 Std.)", "window": "Innerhalb von 24 Stunden"},
            "Tier 3 (£499.95)": {"price": 499.95, "desc": "501 – 1.000 geprüfte Einheiten (24–48 Std.)", "window": "24–48 Stunden"},
            "⚡ Express Fast-Track (£399.95+)": {"price": 399.95, "desc": "Express-Abwicklung (2–3 Std. Eilsprint)", "window": "2–3 Stunden"}
        },
        "priority_title": "Priorisierung (Falls Treffermenge Quote übersteigt):",
        "priority_options": [
            "Klasse A / Industriestandard (ISO-zertifiziert, Marktführer)",
            "Strategische Logistik-Hubs (Nähe Tiefseehäfen, Frachtflughäfen)",
            "Höchste Kontaktdichte (Geprüfte Durchwahlen & Geschäftsleitungs-Mail)",
            "Gleichmäßige geografische Verteilung"
        ],
        "summary_title": "📋 Bestellübersichts-Snapshot (Vor Ausführung)",
        "legal_header": "Rechtliche Vereinbarungen & Pflichtzustimmung:",
        "terms_ver": "Nutzungsbedingungen v1.0 — Gültig ab 23. September 2026",
        "legal_1": "Ich bestätige, dass ich im Namen eines Unternehmens handel, zur Auftragserteilung berechtigt bin und die Nutzungsbedingungen (v1.0) sowie Datenschutzbestimmungen akzeptiere.",
        "legal_2": "Ich autorisiere AI99 ausdrücklich, den Dienst nach Zahlungseingang zu beginnen, und erkenne an, dass Gebühren nach Ausführungsbeginn nicht erstattungsfähig sind.",
        "warn_msg": "Bitte Firmenangaben, Direktive ausfüllen und beide Erklärungen bestätigen.",
        "btn_ready": "🚀 Mission autorisieren & zahlen",
        "btn_locked": "🔒 Mission autorisieren & zahlen (Gesperrt)"
    },
    "🇹🇭 ภาษาไทย": {
        "title": "AI99 INTELLIGENCE NAVIGATOR",
        "subtitle": "บริการสืบค้นและตรวจสอบข้อมูลธุรกิจเชิงลึกเฉพาะกิจ (B2B)",
        "badge": "🛡️ ข้อมูลสาธารณะถูกต้องตามกฎหมาย 100% (OSINT Compliant)",
        "company_label": "ชื่อบริษัท / นิติบุคคล / องค์กร:",
        "email_label": "อีเมลทางการระดับองค์กร (Official Business Email):",
        "target_label": "ประเทศหรือภูมิภาคเป้าหมาย:",
        "target_options": ["เวียดนาม", "ไทย", "สิงคโปร์", "อินโดนีเซีย", "มาเลเซีย", "สหราชอาณาจักร", "สหรัฐอเมริกา", "อื่นๆ (ระบุในโจทย์)"],
        "directive_label": "พิมพ์โจทย์ความต้องการทางธุรกิจอย่างอิสระ:",
        "directive_ph": "เช่น: ต้องการหาโกดังห้องเย็น ขอเบอร์โทรตรงฝ่ายขาย และประมาณการราคาค่าเช่าต่อตารางเมตร ไม่เอาบริษัทนายหน้า",
        "compliance_warn": "⚠️ ห้ามส่งรหัสผ่าน ข้อมูลลับทางการค้าของบุคคลที่สาม หรือข้อมูลส่วนบุคคลที่ได้มาโดยมิชอบด้วยกฎหมาย",
        "tier_title": "เลือกขนาดแพ็กเกจข้อมูลที่ต้องการ:",
        "tier_data": {
            "Tier 1 (£249.95)": {"price": 249.95, "desc": "สูงสุด 300 กิจการที่ผ่านการยืนยัน (ส่งมอบใน 24 ชม.)", "window": "ภายใน 24 ชั่วโมง"},
            "Tier 2 (£349.95) [แนะนำ]": {"price": 349.95, "desc": "301 – 500 กิจการที่ผ่านการยืนยัน (ส่งมอบใน 24 ชม.)", "window": "ภายใน 24 ชั่วโมง"},
            "Tier 3 (£499.95)": {"price": 499.95, "desc": "501 – 1,000 กิจการที่ผ่านการยืนยัน (ส่งมอบ 24–48 ชม.)", "window": "24–48 ชั่วโมง"},
            "⚡ Express Fast-Track (£399.95+)": {"price": 399.95, "desc": "ภารกิจด่วนพิเศษ (ส่งมอบภายใน 2–3 ชม.)", "window": "2–3 ชั่วโมง"}
        },
        "priority_title": "กรณีข้อมูลในพื้นที่เป้าหมายมีมากกว่าโควตา จัดลำดับคัดเลือกแบบใด?",
        "priority_options": [
            "เกรด A / ชั้นนำระดับอุตสาหกรรม (Top Enterprise, ได้รับการรับรอง ISO)",
            "ใกล้จุดยุทธศาสตร์หลัก (ใกล้ท่าเรือน้ำลึก, สนามบินขนส่งสินค้า, นิคมอุตสาหกรรม)",
            "ช่องทางติดต่อสมบูรณ์สูงสุด (เบอร์โทรตรงฝ่ายขาย/บริหาร, อีเมลทางการ)",
            "กระจายสัดส่วนเท่ากันครอบคลุมทั่วประเทศ"
        ],
        "summary_title": "📋 ภาพรวมคำสั่งซื้อก่อนดำเนินการ (Order Summary Snapshot)",
        "legal_header": "ข้อตกลงและเงื่อนไขการอนุมัติทางกฎหมาย:",
        "terms_ver": "ข้อกำหนดการให้บริการ v1.0 — มีผลบังคับใช้ 23 กันยายน 2026",
        "legal_1": "ข้าพเจ้ายืนยันว่าดำเนินการในนามนิติบุคคลหรือองค์กรธุรกิจ มีอำนาจสั่งซื้อถูกต้อง ได้อ่านและยอมรับข้อกำหนดการให้บริการ (v1.0) นโยบายความเป็นส่วนตัว และมาตรฐานข้อมูล",
        "legal_2": "ข้าพเจ้าอนุมัติให้ AI99 เริ่มต้นปฏิบัติการทันทีหลังชำระเงิน และรับทราบว่าค่าบริการไม่สามารถขอคืนได้ทุกกรณีตามที่กฎหมายอนุญาตเมื่อเริ่มรันระบบ",
        "warn_msg": "กรุณาระบุชื่อบริษัท อีเมล โจทย์ และยินยอมรับเงื่อนไขทั้ง 2 ข้อเพื่อปลดล็อกปุ่มชำระเงิน",
        "btn_ready": "🚀 อนุมัติภารกิจและชำระเงิน",
        "btn_locked": "🔒 อนุมัติภารกิจและชำระเงิน (ระบบถูกล็อก)"
    }
}

# 5. Session State สำหรับ Order ID คงที่
if "order_id" not in st.session_state:
    now_str = datetime.utcnow().strftime("%Y%m%d")
    short_hash = str(uuid.uuid4())[:4].upper()
    st.session_state.order_id = f"AI99-ORD-{now_str}-{short_hash}"

col_left, col_right = st.columns([1.1, 1.1])

with col_left:
    st.write("") # ปล่อยพื้นที่โล่งสำหรับ Negative Space และตัวแบบ

with col_right:
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    
    # เลือกระบบภาษา
    selected_lang = st.selectbox(
        "Select Interface Language / เลือกภาษา:",
        list(LANG_DATA.keys()),
        index=0
    )
    txt = LANG_DATA[selected_lang]
    
    st.markdown(f'<div class="gold-title">{txt["title"]}</div>', unsafe_allow_html=True)
    st.caption(txt["subtitle"])
    st.markdown(f'<div class="badge-legal">{txt["badge"]}</div>', unsafe_allow_html=True)
    
    # หมวดตัวตน B2B (อยู่ติดกันตามคำสั่งพี่ยอด)
    company_name = st.text_input(txt["company_label"], placeholder="Acme Logistics Ltd. / Enterprise Corp")
    buyer_email = st.text_input(txt["email_label"], placeholder="director@acme.com")
    country = st.selectbox(txt["target_label"], txt["target_options"])
    
    # หมวดความต้องการ & Data Compliance Warning
    directive = st.text_area(txt["directive_label"], placeholder=txt["directive_ph"], height=85)
    st.markdown(f'<div class="compliance-note">{txt["compliance_warn"]}</div>', unsafe_allow_html=True)
    
    # เลือกระดับ Tier
    st.markdown(f"**{txt['tier_title']}**")
    tier_keys = list(txt["tier_data"].keys())
    tier_selected = st.radio("Tier Selection:", tier_keys, index=0, label_visibility="collapsed")
    current_tier_info = txt["tier_data"][tier_selected]
    
    # Priority Filter
    st.markdown(f"**{txt['priority_title']}**")
    priority_filter = st.selectbox("Priority:", txt["priority_options"], label_visibility="collapsed")
    
    # กรอบ Order Summary Snapshot ก่อนกดจ่ายเงิน
    st.markdown('<div class="order-summary-box">', unsafe_allow_html=True)
    st.markdown(f"**{txt['summary_title']}**")
    c1, c2 = st.columns(2)
    with c1:
        st.write(f"**Order ID:** `{st.session_state.order_id}`")
        st.write(f"**Entity:** {company_name if company_name else '—'}")
        st.write(f"**Target:** {country}")
    with c2:
        st.write(f"**Tier Price:** £{current_tier_info['price']:,.2f} GBP")
        st.write(f"**Window:** {current_tier_info['window']}")
        st.write(f"**Terms Ref:** `v1.0-20260923`")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2 ปุ่มมหัศจรรย์ฉบับ B2B
    st.markdown(f"**{txt['legal_header']}**")
    st.caption(f"📑 {txt['terms_ver']}")
    
    with st.expander("🔍 Click to review Terms of Service & OSINT Compliance Policy"):
        st.write("""
        **1. Scope of Engagement:** AI99 provides automated research services exclusively compiled from publicly available online sources (OSINT).
        **2. B2B Warranties:** Client warrants that requests are for lawful commercial purposes.
        **3. Non-Refundable Nature:** Due to the instant allocation of computational resources, all fees are strictly non-refundable upon commencement.
        """)
        
    legal_agree_1 = st.checkbox(txt["legal_1"])
    legal_agree_2 = st.checkbox(txt["legal_2"])
    
    # เงื่อนไขปลดล็อกปุ่ม (ครบทั้งชื่อบริษัท, อีเมล, โจทย์ และติ๊ก 2 ช่อง)
    is_ready = (
        len(company_name.strip()) >= 2 and
        len(buyer_email.strip()) > 5 and "@" in buyer_email and
        len(directive.strip()) >= 5 and
        legal_agree_1 and
        legal_agree_2
    )
    
    if is_ready:
        st.success("✅ Order parameters verified. Authorization gate unlocked.")
        if st.button(txt["btn_ready"], use_container_width=True):
            # บันทึก Audit Trail Snapshot ลงไฟล์ระบบหลังบ้านทันที
            audit_record = {
                "order_id": st.session_state.order_id,
                "timestamp_utc": datetime.utcnow().isoformat(),
                "company_name": company_name,
                "buyer_email": buyer_email,
                "target_country": country,
                "directive": directive,
                "tier": tier_selected,
                "price": current_tier_info["price"],
                "currency": "GBP",
                "priority_filter": priority_filter,
                "terms_version": "v1.0-20260923",
                "b2b_authority_consent": legal_agree_1,
                "non_refundable_consent": legal_agree_2
            }
            # บันทึกจำลองหลังบ้าน
            os.makedirs("audit_logs", exist_ok=True)
            with open(f"audit_logs/{st.session_state.order_id}.json", "w", encoding="utf-8") as f:
                json.dump(audit_record, f, indent=2, ensure_ascii=False)
                
            st.info(f"Connecting to Secure Stripe Checkout for Order: {st.session_state.order_id}...")
    else:
        st.warning(f"⚠️ {txt['warn_msg']}")
        st.button(txt["btn_locked"], disabled=True, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)
