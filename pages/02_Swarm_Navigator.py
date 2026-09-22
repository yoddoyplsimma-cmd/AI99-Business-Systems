import streamlit as st
import base64
import os
import json
import uuid
import hashlib
from datetime import datetime

# 1. ตั้งค่าหน้าจอแบบกว้าง
st.set_page_config(
    page_title="AI99 Intelligence Navigator | Bespoke B2B Research",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Server-Side Master Catalog (ล็อกราคาและเงื่อนไขเวลาอย่างเป็นทางการ)
TIER_CATALOG = {
    "TIER_1": {
        "code": "TIER_1",
        "price_gbp": 249.95,
        "currency": "GBP",
        "quota": "Up to 300 verified entities",
        "window_rule": "Within 24 hours after payment confirmation and acceptance of a complete, actionable mission brief.",
        "label_en": "Tier 1: Up to 300 verified entities — £249.95",
        "label_de": "Tier 1: Bis zu 300 verifizierte Einheiten — £249.95",
        "label_th": "Tier 1: สูงสุด 300 กิจการที่ผ่านการยืนยัน — £249.95"
    },
    "TIER_2": {
        "code": "TIER_2",
        "price_gbp": 349.95,
        "currency": "GBP",
        "quota": "301 – 500 verified entities",
        "window_rule": "Within 24 hours after payment confirmation and acceptance of a complete, actionable mission brief.",
        "label_en": "Tier 2: 301 – 500 verified entities — £349.95 [Recommended]",
        "label_de": "Tier 2: 301 – 500 verifizierte Einheiten — £349.95 [Empfohlen]",
        "label_th": "Tier 2: 301 – 500 กิจการที่ผ่านการยืนยัน — £349.95 [แนะนำ]"
    },
    "TIER_3": {
        "code": "TIER_3",
        "price_gbp": 499.95,
        "currency": "GBP",
        "quota": "501 – 1,000 verified entities",
        "window_rule": "Within 24–48 hours after payment confirmation and acceptance of a complete, actionable mission brief.",
        "label_en": "Tier 3: 501 – 1,000 verified entities — £499.95",
        "label_de": "Tier 3: 501 – 1.000 verifizierte Einheiten — £499.95",
        "label_th": "Tier 3: 501 – 1,000 กิจการที่ผ่านการยืนยัน — £499.95"
    },
    "EXPRESS": {
        "code": "EXPRESS",
        "price_gbp": 399.95,
        "currency": "GBP",
        "quota": "Express priority execution quota",
        "window_rule": "Within 2–3 hours after payment confirmation and acceptance of a complete, actionable mission brief.",
        "label_en": "⚡ Express Fast-Track (Sprint) — £399.95+",
        "label_de": "⚡ Express Fast-Track (Eilsprint) — £399.95+",
        "label_th": "⚡ Express Fast-Track (ภารกิจด่วนพิเศษ) — £399.95+"
    }
}

LEGAL_VERSIONS = {
    "terms_version": "Terms of Service v1.0",
    "privacy_version": "Privacy Policy v1.0",
    "osint_policy_version": "OSINT Compliance Policy v1.0",
    "effective_date": "23 September 2026"
}

# 3. จัดการรูปภาพพื้นหลัง
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

img_base64 = get_base64_image("pages/bg_agent.jpg")
bg_style = f"""
    background: linear-gradient(rgba(11, 15, 25, 0.45), rgba(11, 15, 25, 0.78)), url("data:image/jpeg;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
""" if img_base64 else "background-color: #0b0f19;"

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
        background: rgba(15, 23, 42, 0.86);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        border: 1px solid rgba(212, 175, 55, 0.4);
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.6);
        margin-bottom: 20px;
    }}
    
    .order-summary-box {{
        background: rgba(10, 16, 30, 0.92);
        border: 1px solid rgba(212, 175, 55, 0.65);
        border-radius: 8px;
        padding: 16px;
        margin-top: 14px;
        margin-bottom: 14px;
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
        margin-top: -8px;
        margin-bottom: 14px;
    }}
</style>
""", unsafe_allow_html=True)

# 4. Multilingual Dictionary
LANG_DATA = {
    "🇬🇧 English": {
        "title": "AI99 INTELLIGENCE NAVIGATOR",
        "subtitle": "Bespoke Business Research & Verified Data Services",
        "badge": "🛡️ Lawful Open-Source Intelligence (OSINT) & Public-Source Research",
        "company_label": "Company / Entity Name:",
        "email_label": "Official Business Email:",
        "target_label": "Target Jurisdiction / Country:",
        "target_options": ["Vietnam", "Thailand", "Singapore", "Indonesia", "Malaysia", "United Kingdom", "United States", "Other (Specify in directive)"],
        "directive_label": "Bespoke Intelligence Directive:",
        "directive_ph": "E.g., Cold storage logistics facilities, verified direct sales phone numbers, estimated rental rate per sqm. Exclude third-party brokers.",
        "compliance_warn": "⚠️ Compliance Notice: Do not submit passwords, credentials, confidential third-party information, or unlawfully obtained personal data.",
        "tier_title": "Select Mission Tier / Data Quota:",
        "priority_title": "Priority Allocation (If target landscape exceeds quota):",
        "priority_options": [
            "Grade A / Industry Standard (ISO Certified, Top Tier Market Share)",
            "Strategic Logistics Hubs (Near Deep Sea Ports, Cargo Airports)",
            "Maximum Contact Completeness (Verified Direct Phone & Executive Email)",
            "National Geographic Dispersion Across All Regions"
        ],
        "summary_title": "📋 Order Summary Snapshot (Pre-Execution)",
        "legal_header": "Legal Agreements & Mandatory Consent:",
        "legal_1": "I confirm that I am acting on behalf of a business or professional entity, that I am authorized to place this order, and that I have read and agree to the Terms of Service (v1.0), Privacy Policy (v1.0), and applicable data-use requirements.",
        "legal_2": "I expressly authorize AI99 to commence the customized service following payment and acknowledge that, once execution has commenced, fees are non-refundable to the fullest extent permitted by applicable law.",
        "warn_msg": "Please complete all entity fields, actionable directive, and authorize both mandatory declarations.",
        "btn_ready": "🚀 Authorize Intelligence Mission & Pay",
        "btn_locked": "🔒 Authorize Mission & Pay (System Locked)"
    },
    "🇩🇪 Deutsch": {
        "title": "AI99 INTELLIGENCE NAVIGATOR",
        "subtitle": "Maßgeschneiderte Unternehmensanalyse & Geprüfte Datendienste",
        "badge": "🛡️ Rechtmäßige Open-Source-Intelligence (OSINT) & Öffentlich zugängliche Recherche",
        "company_label": "Unternehmen / Organisationsname:",
        "email_label": "Offizielle geschäftliche E-Mail-Adresse:",
        "target_label": "Zielregion / Land:",
        "target_options": ["Vietnam", "Thailand", "Singapur", "Indonesien", "Malaysia", "Vereinigtes Königreich", "Vereinigte Staaten", "Andere (In Direktive angeben)"],
        "directive_label": "Maßgeschneiderte Aufklärungsdirektive:",
        "directive_ph": "Z.B.: Kühlhaus-Logistik, Direktnummern der Vertriebsleitung, Mietpreise pro m². Keine Makler.",
        "compliance_warn": "⚠️ Compliance-Hinweis: Übermitteln Sie keine Passwörter, Zugangsdaten oder unrechtmäßig erlangte personenbezogene Daten.",
        "tier_title": "Missionsstufe / Datenquote auswählen:",
        "priority_title": "Priorisierung (Falls Treffermenge Quote übersteigt):",
        "priority_options": [
            "Klasse A / Industriestandard (ISO-zertifiziert, Marktführer)",
            "Strategische Logistik-Hubs (Nähe Tiefseehäfen, Frachtflughäfen)",
            "Höchste Kontaktdichte (Geprüfte Durchwahlen & Geschäftsleitungs-Mail)",
            "Gleichmäßige geografische Verteilung"
        ],
        "summary_title": "📋 Bestellübersichts-Snapshot (Vor Ausführung)",
        "legal_header": "Rechtliche Vereinbarungen & Pflichtzustimmung:",
        "legal_1": "Ich bestätige, dass ich im Namen eines Unternehmens handle, zur Auftragserteilung berechtigt bin und die Nutzungsbedingungen (v1.0), Datenschutzrichtlinie (v1.0) sowie Datenanforderungen akzeptiere.",
        "legal_2": "Ich autorisiere AI99 ausdrücklich, den Dienst nach Zahlungseingang zu beginnen, und erkenne an, dass Gebühren nach Beginn der Ausführung nicht erstattungsfähig sind.",
        "warn_msg": "Bitte Firmenangaben, ausführbare Direktive ausfüllen und beide Erklärungen bestätigen.",
        "btn_ready": "🚀 Mission autorisieren & zahlen",
        "btn_locked": "🔒 Mission autorisieren & zahlen (Gesperrt)"
    },
    "🇹🇭 ภาษาไทย": {
        "title": "AI99 INTELLIGENCE NAVIGATOR",
        "subtitle": "บริการสืบค้นและตรวจสอบข้อมูลธุรกิจเชิงลึกเฉพาะกิจ (B2B)",
        "badge": "🛡️ การสืบค้นข้อมูลสาธารณะและข่าวกรองเปิดอย่างถูกต้องตามกฎหมาย (OSINT Compliant)",
        "company_label": "ชื่อบริษัท / นิติบุคคล / องค์กร:",
        "email_label": "อีเมลทางการระดับองค์กร (Official Business Email):",
        "target_label": "ประเทศหรือภูมิภาคเป้าหมาย:",
        "target_options": ["เวียดนาม", "ไทย", "สิงคโปร์", "อินโดนีเซีย", "มาเลเซีย", "สหราชอาณาจักร", "สหรัฐอเมริกา", "อื่นๆ (ระบุในโจทย์)"],
        "directive_label": "พิมพ์โจทย์ความต้องการทางธุรกิจอย่างอิสระ:",
        "directive_ph": "เช่น: ต้องการหาโกดังห้องเย็น ขอเบอร์โทรตรงฝ่ายขาย และประมาณการราคาค่าเช่าต่อตารางเมตร ไม่เอาบริษัทนายหน้า",
        "compliance_warn": "⚠️ ข้อกำหนดด้านความถูกต้อง: ห้ามส่งรหัสผ่าน ข้อมูลลับทางการค้าของบุคคลที่สาม หรือข้อมูลส่วนบุคคลที่ได้มาโดยมิชอบด้วยกฎหมาย",
        "tier_title": "เลือกขนาดแพ็กเกจข้อมูลที่ต้องการ:",
        "priority_title": "กรณีข้อมูลในพื้นที่เป้าหมายมีมากกว่าโควตา จัดลำดับคัดเลือกแบบใด?",
        "priority_options": [
            "เกรด A / ชั้นนำระดับอุตสาหกรรม (Top Enterprise, ได้รับการรับรอง ISO)",
            "ใกล้จุดยุทธศาสตร์หลัก (ใกล้ท่าเรือน้ำลึก, สนามบินขนส่งสินค้า, นิคมอุตสาหกรรม)",
            "ช่องทางติดต่อสมบูรณ์สูงสุด (เบอร์โทรตรงฝ่ายขาย/บริหาร, อีเมลทางการ)",
            "กระจายสัดส่วนเท่ากันครอบคลุมทั่วประเทศ"
        ],
        "summary_title": "📋 ภาพรวมคำสั่งซื้อก่อนดำเนินการ (Order Summary Snapshot)",
        "legal_header": "ข้อตกลงและเงื่อนไขการอนุมัติทางกฎหมาย:",
        "legal_1": "ข้าพเจ้ายืนยันว่าดำเนินการในนามนิติบุคคลหรือองค์กรธุรกิจ มีอำนาจสั่งซื้อถูกต้อง ได้อ่านและยอมรับข้อกำหนดการให้บริการ (v1.0) นโยบายความเป็นส่วนตัว (v1.0) และมาตรฐานข้อมูล",
        "legal_2": "ข้าพเจ้าอนุมัติให้ AI99 เริ่มต้นปฏิบัติการทันทีหลังชำระเงิน และรับทราบว่าค่าบริการไม่สามารถขอคืนได้ทุกกรณีตามที่กฎหมายอนุญาตเมื่อเริ่มรันระบบ",
        "warn_msg": "กรุณาระบุชื่อบริษัท อีเมล โจทย์ที่ชัดเจน และยินยอมรับเงื่อนไขทั้ง 2 ข้อเพื่อปลดล็อกปุ่มชำระเงิน",
        "btn_ready": "🚀 อนุมัติภารกิจและชำระเงิน",
        "btn_locked": "🔒 อนุมัติภารกิจและชำระเงิน (ระบบถูกล็อก)"
    }
}

# 5. Session State Order ID
if "order_id" not in st.session_state:
    now_str = datetime.utcnow().strftime("%Y%m%d")
    short_hash = str(uuid.uuid4())[:4].upper()
    st.session_state.order_id = f"AI99-ORD-{now_str}-{short_hash}"

col_left, col_right = st.columns([1.1, 1.1])

with col_left:
    st.write("") 

with col_right:
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    
    # เลือกระบบภาษา
    selected_lang = st.selectbox("Select Language / เลือกภาษา:", list(LANG_DATA.keys()), index=0)
    txt = LANG_DATA[selected_lang]
    lang_code = "en" if "English" in selected_lang else ("de" if "Deutsch" in selected_lang else "th")
    
    st.markdown(f'<div class="gold-title">{txt["title"]}</div>', unsafe_allow_html=True)
    st.caption(txt["subtitle"])
    st.markdown(f'<div class="badge-legal">{txt["badge"]}</div>', unsafe_allow_html=True)
    
    # หมวดตัวตน B2B
    company_name = st.text_input(txt["company_label"], placeholder="Acme Logistics Ltd. / Enterprise Corp")
    buyer_email = st.text_input(txt["email_label"], placeholder="director@acme.com")
    country = st.selectbox(txt["target_label"], txt["target_options"])
    
    # หมวดความต้องการ & Data Compliance Warning
    directive = st.text_area(txt["directive_label"], placeholder=txt["directive_ph"], height=85)
    st.markdown(f'<div class="compliance-note">{txt["compliance_warn"]}</div>', unsafe_allow_html=True)
    
    # Server-Side Tier Selection
    st.markdown(f"**{txt['tier_title']}**")
    tier_display_options = {k: v[f"label_{lang_code}"] for k, v in TIER_CATALOG.items()}
    selected_tier_code = st.radio(
        "Tier:",
        options=list(tier_display_options.keys()),
        format_func=lambda x: tier_display_options[x],
        index=0,
        label_visibility="collapsed"
    )
    selected_tier = TIER_CATALOG[selected_tier_code]
    
    # Priority Filter
    st.markdown(f"**{txt['priority_title']}**")
    priority_filter = st.selectbox("Priority:", txt["priority_options"], label_visibility="collapsed")
    
    # คำนวณ Directive SHA-256 Digest
    directive_clean = directive.strip()
    directive_hash = hashlib.sha256(directive_clean.encode("utf-8")).hexdigest()[:12] if directive_clean else "NONE"
    
    # กรอบ Order Summary Snapshot ครบถ้วนตามมาตรฐานพี่ยอด
    st.markdown('<div class="order-summary-box">', unsafe_allow_html=True)
    st.markdown(f"**{txt['summary_title']}**")
    c1, c2 = st.columns(2)
    with c1:
        st.write(f"**Order ID:** `{st.session_state.order_id}`")
        st.write(f"**Entity:** {company_name if company_name else '—'}")
        st.write(f"**Target:** {country}")
        st.write(f"**Tier Code:** `{selected_tier['code']}` ({selected_tier['quota']})")
    with c2:
        st.write(f"**Total Quoted:** £{selected_tier['price_gbp']:,.2f} {selected_tier['currency']}")
        st.write(f"**Priority:** {priority_filter[:25]}...")
        st.write(f"**Directive Hash:** `{directive_hash}`")
        st.write(f"**Policies Ref:** `{LEGAL_VERSIONS['terms_version']} | {LEGAL_VERSIONS['effective_date']}`")
        
    st.markdown(f"**Mission Summary (Scope):** *\"{directive_clean if directive_clean else 'Pending client brief...'}\"*")
    st.caption(f"⏱️ **Delivery Baseline:** {selected_tier['window_rule']}")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Policy Review Hub
    st.markdown(f"**{txt['legal_header']}**")
    with st.expander("🔍 Click to review Terms of Service, Privacy Policy & OSINT Guidelines"):
        st.markdown(f"### {LEGAL_VERSIONS['terms_version']} (Effective: {LEGAL_VERSIONS['effective_date']})")
        st.write("""
        **1. B2B Commercial Engagement:** All services provided by AI99 are intended strictly for professional and corporate entities. The client warrants full legal authority to place this directive.
        **2. Lawful OSINT Scope:** Research is conducted solely using lawfully accessible public sources. AI99 strictly refuses assignments requiring unauthorized intrusion, compromised credentials, or illicit data acquisition.
        **3. Delivery Window Baseline:** Delivery timelines commence only upon successful payment confirmation and acceptance of an actionable, unambiguous brief. Assignments requiring client clarification will pause the timeline until confirmed.
        **4. Immediate Execution & Non-Refundable Nature:** To the fullest extent permitted by applicable law, all fees are non-refundable once customized computation and execution have commenced.
        """)
        st.markdown(f"### {LEGAL_VERSIONS['privacy_version']} & {LEGAL_VERSIONS['osint_policy_version']}")
        st.write("We process business contact data in accordance with international data governance standards and strict confidentiality.")
        
    legal_agree_1 = st.checkbox(txt["legal_1"])
    legal_agree_2 = st.checkbox(txt["legal_2"])
    
    # Server-Side Complete Validation Gate
    is_ready = (
        len(company_name.strip()) >= 2 and
        len(buyer_email.strip()) > 5 and "@" in buyer_email and
        len(directive_clean) >= 10 and
        legal_agree_1 and
        legal_agree_2
    )
    
    if is_ready:
        st.success("✅ Order parameters verified. Authorization gate unlocked.")
        if st.button(txt["btn_ready"], use_container_width=True):
            # Immutable Order Record
            immutable_order_record = {
                "order_id": st.session_state.order_id,
                "created_at_utc": datetime.utcnow().isoformat(),
                "execution_commenced_at": None,
                "company_name": company_name.strip(),
                "buyer_email": buyer_email.strip(),
                "target_jurisdiction": country,
                "mission_directive_raw": directive_clean,
                "mission_directive_sha256": hashlib.sha256(directive_clean.encode("utf-8")).hexdigest(),
                "tier_code": selected_tier["code"],
                "quoted_price": selected_tier["price_gbp"],
                "currency": selected_tier["currency"],
                "priority_filter": priority_filter,
                "delivery_window_rule": selected_tier["window_rule"],
                "legal_governance": LEGAL_VERSIONS,
                "consent_b2b_authority": legal_agree_1,
                "consent_immediate_execution_nonrefundable": legal_agree_2,
                "payment_status": "PENDING_CHECKOUT"
            }
            
            os.makedirs("audit_orders", exist_ok=True)
            with open(f"audit_orders/{st.session_state.order_id}.json", "w", encoding="utf-8") as f:
                json.dump(immutable_order_record, f, indent=2, ensure_ascii=False)
                
            st.info(f"Order Snapshot locked: `{st.session_state.order_id}`. Redirecting to Secure Checkout...")
    else:
        st.warning(f"⚠️ {txt['warn_msg']}")
        st.button(txt["btn_locked"], disabled=True, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)
