import streamlit as st
import stripe
import base64
import time
from datetime import datetime, timedelta

# 1. Page Configuration
st.set_page_config(page_title="AI99 Global Sandbox Simulator", page_icon="🧪", layout="centered")

# Stripe Sandbox Secret Key (Using sk_test for Simulator)
stripe.api_key = "sk_test_51TUw0KD0F0jpQtDWsxh6txwmyMFrgLo2tjBE8sDQsXyKpqCBHqEt4MBing4oW5dfvbsTobtFJ31yXo6WH7S53P1z001Z8oqVvf"

# 2. Multi-Language Dictionary Setup
lang_options = {
    "🇬🇧 English (UK)": "en_uk",
    "🇺🇸 English (US)": "en_us",
    "🇩🇪 Deutsch": "de",
    "🇪🇸 Español": "es"
}

ui_translations = {
    "en_uk": {
        "title": "🧪 AI99 Checkout & Legal Contract Sandbox Simulator",
        "caption": "Comprehensive Virtual Simulation System (Frontend + Payment Check + Cloud Vault + Email Delivery)",
        "sub1": "🌐 1. Select Contract Package & Enter Buyer Information",
        "email_lbl": "📧 Enter Buyer Email (For Simulation Delivery):",
        "country_lbl": "📌 Select Jurisdiction / Country:",
        "pkg_lbl": "💼 Select SME Package Options:",
        "sub2": "⚖️ 2. Legal Agreements & Terms Acceptance",
        "warn_email": "⚠️ *Please enter buyer email to enable simulator.*",
        "sub3": "💳 3. System Processing Status",
        "license_lbl": "📋 Contract License:",
        "charge_lbl": "💰 Total Amount Charged:",
        "btn_pay": "🚀 Pay & Enable Virtual Simulator",
        "spinner": "System logic is simulating connection to Stripe server...",
        "vault_title": "🔓 [Vault Simulation] Simulating Cloud Vault File Retrieval",
        "vault_found": "📁 Asset File Found in Vault:",
        "vault_expiry": "⏳ Secure Link Expiry: 24-Hour Expiration Link",
        "btn_dl": "📥 Test Download Actual Contract File (Secure UI Link)",
        "mail_title": "📨 [Email Simulation] Simulating Mail Server Operations",
        "mail_box": "📬 Click to Open Simulation Inbox (Preview Customer Email)",
        "btn_reset": "🔄 Reset Sandbox Simulator"
    },
    "en_us": {
        "title": "🧪 AI99 Checkout & Legal Contract Sandbox Simulator",
        "caption": "Comprehensive Virtual Simulation System (Frontend + Payment Check + Cloud Vault + Email Delivery)",
        "sub1": "🌐 1. Select Contract Package & Enter Buyer Info",
        "email_lbl": "📧 Enter Buyer Email (For Simulation Delivery):",
        "country_lbl": "📌 Select Jurisdiction / Country:",
        "pkg_lbl": "💼 Select SME Package Options:",
        "sub2": "⚖️ 2. Legal Agreements & Terms Acceptance",
        "warn_email": "⚠️ *Please enter buyer email to enable simulator.*",
        "sub3": "💳 3. System Processing Status",
        "license_lbl": "📋 Contract License:",
        "charge_lbl": "💰 Total Amount Charged:",
        "btn_pay": "🚀 Pay & Enable Virtual Simulator",
        "spinner": "System logic is simulating connection to Stripe server...",
        "vault_title": "🔓 [Vault Simulation] Simulating Cloud Vault File Retrieval",
        "vault_found": "📁 Asset File Found in Vault:",
        "vault_expiry": "⏳ Secure Link Expiry: 24-Hour Expiration Link",
        "btn_dl": "📥 Test Download Actual Contract File (Secure UI Link)",
        "mail_title": "📨 [Email Simulation] Simulating Mail Server Operations",
        "mail_box": "📬 Click to Open Simulation Inbox (Preview Customer Email)",
        "btn_reset": "🔄 Reset Sandbox Simulator"
    },
    "de": {
        "title": "🧪 AI99 Checkout & Rechtสัญญา Sandbox-Simulator",
        "caption": "Umfassendes virtuelles Simulationssystem (Frontend + Zahlungsprüfung + Cloud Vault + E-Mail-Zustellung)",
        "sub1": "🌐 1. Vertrags-Paket auswählen & Käuferdaten eingeben",
        "email_lbl": "📧 Käufer-E-Mail eingeben (Für Zustellungssimulation):",
        "country_lbl": "📌 Gerichtsstand / Land auswählen:",
        "pkg_lbl": "💼 SME-Paketoptionen auswählen:",
        "sub2": "⚖️ 2. Rechtliche Vereinbarungen & Anerkennung der Bedingungen",
        "warn_email": "⚠️ *Bitte Käufer-E-Mail eingeben, um den Simulator zu aktivieren.*",
        "sub3": "💳 3. Status der Systemverarbeitung",
        "license_lbl": "📋 Vertragslizenz:",
        "charge_lbl": "💰 Geladener Gesamtbetrag:",
        "btn_pay": "🚀 Bezahlen & Virtuellen Simulator aktivieren",
        "spinner": "Systemlogik simuliert Verbindung zum Stripe-Server...",
        "vault_title": "🔓 [Vault-Simulation] Simuliere Abruf von Cloud-Vault-Dateien",
        "vault_found": "📁 Asset-Datei im Vault gefunden:",
        "vault_expiry": "⏳ Sicherer Link läuft ab: 24-Stunden-Ablauflink",
        "btn_dl": "📥 Tatsächliche Vertragsdatei herunterladen (Sicherer UI-Link)",
        "mail_title": "📨 [E-Mail-Simulation] Simuliere Mail-Server-Operationen",
        "mail_box": "📬 Klicken, um den Simulations-Posteingang zu öffnen (Vorschau Kunden-E-Mail)",
        "btn_reset": "🔄 Sandbox-Simulator zurücksetzen"
    },
    "es": {
        "title": "🧪 AI99 Simulador de Sandbox de Pago y Contrato Legal",
        "caption": "Sistema de simulación virtual integral (Frontend + Verificación de pago + Cloud Vault + Entrega de correo)",
        "sub1": "🌐 1. Seleccione el paquete de contrato e ingrese la información del comprador",
        "email_lbl": "📧 Ingrese el correo electrónico del comprador (Para simulación de entrega):",
        "country_lbl": "📌 Seleccione Jurisdicción / País:",
        "pkg_lbl": "💼 Seleccione Opciones de Paquete SME:",
        "sub2": "⚖️ 2. Acuerdos legales y aceptación de términos",
        "warn_email": "⚠️ *Por favor ingrese el correo electrónico del comprador para activar el simulador.*",
        "sub3": "💳 3. Estado de procesamiento del sistema",
        "license_lbl": "📋 Licencia de contrato:",
        "charge_lbl": "💰 Monto total cobrado:",
        "btn_pay": "🚀 Pagar y activar simulador virtual",
        "spinner": "La lógica del sistema está simulando la conexión al servidor de Stripe...",
        "vault_title": "🔓 [Simulación de Vault] Simulando recuperación de archivos de Cloud Vault",
        "vault_found": "📁 Archivo de activos encontrado en Vault:",
        "vault_expiry": "⏳ Vencimiento del enlace seguro: enlace de vencimiento de 24 horas",
        "btn_dl": "📥 Descargar archivo de contrato real (Enlace seguro de UI)",
        "mail_title": "📨 [Simulación de correo electrónico] Simulación de operaciones del servidor de correo",
        "mail_box": "📬 Haga clic para abrir la bandeja de entrada de simulación (Vista previa del correo del cliente)",
        "btn_reset": "🔄 Restablecer simulador de Sandbox"
    }
}

# 3. Language Selector Placement (Top of Page)
selected_lang_name = st.selectbox("🌐 Select Interface Language / ภาษาหลังบ้าน:", list(lang_options.keys()))
lang = lang_options[selected_lang_name]
t = ui_translations[lang]

# Render Titles based on Translation
st.title(t["title"])
st.caption(t["caption"])
st.write("---")

# 4. Global Target Jurisdictions & SME Packages
countries = ["Latvia", "USA", "UK", "Singapore", "Australia", "Germany", "Netherlands", "Switzerland"]
packages = [
    "SME Standard Auto-Responder",
    "SME Golden Lead Finder",
    "SME Diamond Integrated Agent",
    "SME Full-Option Enterprise Vault"
]

# Virtual Contract Repository Mapping
contracts_db = {
    country: {
        pkg: f"legal_contract_{country.lower()}_{pkg.lower().replace(' ', '_').replace('-', '_')}.pdf" 
        for pkg in packages
    } for country in countries
}

# 5. Dynamic Currency Pricing System
euro_zone = ["Latvia", "Germany", "Netherlands", "Switzerland"]
currency_pricing = {
    "EUR": {
        "SME Standard Auto-Responder": {"code": "eur", "amount": 4900, "label": "49.00 EUR"},
        "SME Golden Lead Finder": {"code": "eur", "amount": 9900, "label": "99.00 EUR"},
        "SME Diamond Integrated Agent": {"code": "eur", "amount": 19900, "label": "199.00 EUR"},
        "SME Full-Option Enterprise Vault": {"code": "eur", "amount": 39900, "label": "399.00 EUR"}
    },
    "USD": {
        "SME Standard Auto-Responder": {"code": "usd", "amount": 5900, "label": "59.00 USD"},
        "SME Golden Lead Finder": {"code": "usd", "amount": 11900, "label": "119.00 USD"},
        "SME Diamond Integrated Agent": {"code": "usd", "amount": 23900, "label": "239.00 USD"},
        "SME Full-Option Enterprise Vault": {"code": "usd", "amount": 47900, "label": "479.00 USD"}
    }
}

# 6. Session State Management
if "previous_selection" not in st.session_state: st.session_state.previous_selection = ""
if "checkout_url" not in st.session_state: st.session_state.checkout_url = None
if "payment_success" not in st.session_state: st.session_state.payment_success = False
if "selected_contract" not in st.session_state: st.session_state.selected_contract = ""
if "customer_email" not in st.session_state: st.session_state.customer_email = ""

# 7. Main Interface Layout
st.subheader(t["sub1"])
customer_email_input = st.text_input(t["email_lbl"], placeholder="example@customer.com")

col_a, col_b = st.columns(2)
with col_a:
    selected_country = st.selectbox(t["country_lbl"], countries)
with col_b:
    selected_package = st.selectbox(t["pkg_lbl"], packages)

# Currency logic activation
currency_group = "EUR" if selected_country in euro_zone else "USD"
selected_currency = currency_pricing[currency_group][selected_package]
target_file = contracts_db[selected_country][selected_package]

current_selection_key = f"{selected_country}_{selected_package}"
if current_selection_key != st.session_state.previous_selection:
    st.session_state.checkout_url = None
    st.session_state.payment_success = False
    st.session_state.previous_selection = current_selection_key

st.write("---")

# 8. Legal Right Protection System
st.subheader(t["sub2"])
agree_terms = st.checkbox("I agree to the Terms of Service and Privacy Policy.")
agree_refund = st.checkbox("To the fullest extent permitted by applicable law, all fees are non-refundable once the digital assets, services, or materials have been accessed, delivered, or made available.")
is_compliant = agree_terms and agree_refund and (customer_email_input != "")

if customer_email_input == "":
    st.caption(t["warn_email"])

st.write("---")

# 9. Processing Unit & Payment Simulation
st.subheader(t["sub3"])
col1, col2 = st.columns(2)

with col1:
    st.info(f"{t['license_lbl']} **[{selected_country}] {selected_package}**")
    st.warning(f"{t['charge_lbl']} **{selected_currency['label']}**")
    
    if st.session_state.checkout_url is None and not st.session_state.payment_success:
        if st.button(t["btn_pay"], type="primary", use_container_width=True, disabled=not is_compliant):
            with st.spinner(t["spinner"]):
                try:
                    session = stripe.checkout.Session.create(
                        payment_method_types=["card"],
                        line_items=[{
                            "price_data": {
                                "currency": selected_currency["code"],
                                "product_data": {
                                    "name": f"AI99 Legal Core Contract: {selected_country}",
                                    "description": f"Professional Automation Bundle - {selected_package}",
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
                    st.session_state.payment_success = True 
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Stripe Error: {str(e)}")

# 10. Post-Payment Success Loop Simulation
if st.session_state.payment_success:
    st.success("🎉 [STRIPE WEBHOOK: SUCCESS] Payment successful! Signal sent back to backend successfully.")
    
    expiry_time = datetime.now() + timedelta(hours=24)
    secure_payload = f"{st.session_state.selected_contract}||{expiry_time.timestamp()}"
    secure_token = base64.b64encode(secure_payload.encode()).decode()
    
    # ─── Vault Simulation ───
    st.markdown(f"### {t['vault_title']}")
    st.write(f"{t['vault_found']} `{st.session_state.selected_contract}`")
    st.write(f"⏳ Secure Link Expiry: `{expiry_time.strftime('%Y-%m-%d %H:%M:%S')}`")
    
    st.download_button(
        label=t["btn_dl"],
        data=f"--- AI99 SECURE LEGAL CONTRACT PRODUCTION ---\nTarget Asset File: {st.session_state.selected_contract}\nVerification Security Token: {secure_token}\nJurisdiction Governing Law Enforced: {selected_country}\nProfessional Module Attached: {selected_package}",
        file_name=st.session_state.selected_contract,
        mime="application/pdf",
        use_container_width=True
    )
    
    # ─── Mail Server Simulation ───
    st.write("---")
    st.markdown(f"### {t['mail_title']}")
    with st.expander(t["mail_box"], expanded=True):
        st.markdown(f"""
        **From:** no-reply@ai99.com  
        **To:** `{st.session_state.customer_email}`  
        **Subject:** Receipt and Contract Download Link Completed - AI99  
        
        Dear Member,  
        The system has successfully completed the payment process for **{selected_currency['label']}**.  
        
        The contract type **[{selected_country}] - {selected_package}** has now been authorized for commercial access. You can download the actual file via our secure fallback system below:  
        
        🔗 [Click to Download Encrypted Secure Contract (Temporary Link)]({st.session_state.checkout_url if st.session_state.checkout_url else 'https://example.com'})  
        *(This temporary link will automatically expire within 24 hours for maximum security).* Thank you for participating in our research and choosing the AI99 Global Contract System.  
        """)

with col2:
    if st.session_state.checkout_url or st.session_state.payment_success:
        if st.button(t["btn_reset"], use_container_width=True):
            st.session_state.checkout_url = None
            st.session_state.payment_success = False
            st.session_state.selected_contract = ""
            st.session_state.customer_email = ""
            st.rerun()
