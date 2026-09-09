import accounting_sandbox
import retail_sandbox
import banking_sandbox
import streamlit as st
import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="YBCAI99 System - Enterprise Sandbox Portal",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Styling (Glassmorphism & High-Tech Dark Theme)
st.markdown("""
<style>
    .main { background-color: #0B0F17; }
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #F8FAFC;
        letter-spacing: -0.5px;
        line-height: 1.15;
    }
    .hero-slogan {
        font-size: 1.25rem;
        color: #38BDF8;
        font-weight: 600;
        margin-top: 0.5rem;
        margin-bottom: 1.2rem;
    }
    .hero-desc {
        color: #94A3B8;
        font-size: 1.05rem;
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }
    .product-card {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .card-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #F1F5F9;
        margin-bottom: 8px;
    }
    .card-desc {
        color: #94A3B8;
        font-size: 0.95rem;
        line-height: 1.5;
        margin-bottom: 15px;
    }
    .badge {
        background-color: #0369A1;
        color: #E0F2FE;
        padding: 3px 8px;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 10px;
    }
    .legal-box {
        background: #0F172A;
        border: 1px solid #1E293B;
        border-radius: 8px;
        padding: 15px;
        margin-top: 10px;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# 3. Session State Initialization
if "selected_product" not in st.session_state:
    st.session_state["selected_product"] = None
if "checkout_step" not in st.session_state:
    st.session_state["checkout_step"] = False

# 4. Hero Section
col_hero_text, col_hero_img = st.columns([1.1, 1.1], gap="large")

with col_hero_text:
    st.markdown('<div class="hero-title">YBCAI99 System</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-slogan">ก้าวล้ำคู่แข่งด้วยขุมพลัง AI Navigator Infinity</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="hero-desc">
    ศูนย์ประเมินสถาปัตยกรรมปัญญาประดิษฐ์ระดับองค์กร (B2B Evaluation Sandbox Hub) 
    ทดสอบระบบเสมือนจริงก่อนติดตั้ง พร้อมระบบ <b>AI Navigator</b> คอยนำทางและแนะนำการใช้งานแบบจับมือทำด้วยภาษาธรรมชาติ
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    * ⚡ **Zero-Token Overhead:** ไม่มีบิลค่า Token ส่วนเกิน
    * 🛡️ **Singapore Legal Standard:** สัญญาระดับสากล รองรับ B2B Evaluation
    * 💳 **100% Deployment Credit:** ค่าประเมิน S$149 นำไปหักลดหย่อนค่าติดตั้งจริงได้เต็มจำนวน
    """)

with col_hero_img:
    try:
        st.image("assets/hero_ai_navigator.jpg", caption="YBCAI99 System Architecture Lab", use_container_width=True)
    except:
        st.image("hero_ai_navigator.jpg", caption="YBCAI99 System Architecture Lab", use_container_width=True)

st.divider()

# 5. Product Catalog & Selection
st.subheader("📦 เลือกโซลูชันเพื่อเข้าสู่ระบบประเมิน Sandbox")

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="product-card">
        <div>
            <span class="badge">FINANCIAL CORE</span>
            <div class="card-title">AI บัญชีและระบบภาษี</div>
            <div class="card-desc">
                ระบบอ่านบิลอัตโนมัติ กระทบยอด 3-Way Matching คำนวณภาษี GST 9% / VAT พร้อมส่งออกไฟล์ตรวจสอบ IRAS IAF
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("เลือกประเมิน AI บัญชี", key="btn_acc", use_container_width=True, type="primary"):
        st.session_state["selected_product"] = "Autonomous Accounting & Tax Engine"
        st.session_state["checkout_step"] = True

with col2:
    st.markdown("""
    <div class="product-card">
        <div>
            <span class="badge">RETAIL FLEET</span>
            <div class="card-title">SME Retail & Node Automation</div>
            <div class="card-desc">
                ระบบจัดการร้านค้าและจุดขาย POS เชื่อมโยง 3–5 เครื่องลูกข่าย ตัดรอบสต็อกและประมวลผลอัจฉริยะแบบเรียลไทม์
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("เลือกประเมิน SME Retail", key="btn_sme", use_container_width=True):
        st.session_state["selected_product"] = "SME Retail & Node Automation"
        st.session_state["checkout_step"] = True

with col3:
    st.markdown("""
    <div class="product-card">
        <div>
            <span class="badge">SECURE AIR-GAP</span>
            <div class="card-title">Banking & Enterprise Ledger</div>
            <div class="card-desc">
                ระบบบัญชีแยกประเภทวงปิด ป้องกันข้อมูลรั่วไหล 100% ตรวจสอบเส้นทางธุรกรรม Forensic Audit ย้อนหลัง
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("เลือกประเมิน Banking Ledger", key="btn_bank", use_container_width=True):
        st.session_state["selected_product"] = "Banking & Enterprise Ledger"
        st.session_state["checkout_step"] = True

# 6. Legal Checkout Gate (ปรากฏเมื่อเลือกระบบ)
if st.session_state["checkout_step"] and st.session_state["selected_product"]:
    st.write("")
    st.markdown("---")
    st.subheader(f"🔒 ประตูปรับสิทธิ์และชำระค่าแรกเข้า: {st.session_state['selected_product']}")
    
    col_form, col_summary = st.columns([1.2, 0.8], gap="large")
    
    with col_form:
        company_name = st.text_input("ชื่อนิติบุคคล / องค์กร (Company Name)*")
        business_email = st.text_input("อีเมลติดต่อธุรกิจ (Business Email)*")
        tax_id = st.text_input("เลขประจำตัวผู้เสียภาษี / UEN (ถ้ามี)")
        
        st.markdown('<div class="legal-box">', unsafe_allow_html=True)
        check_b2b = st.checkbox(
            "ข้าพเจ้ายืนยันว่าเข้าใช้งานในนามนิติบุคคล/ธุรกิจ (B2B Only) และยอมรับข้อตกลง YBCAI99 Master Sandbox Evaluation Agreement และ Singapore PDPA Privacy Terms (Version 1.0)",
            key="cb1"
        )
        check_fee = st.checkbox(
            "ข้าพเจ้ารับทราบว่าค่าประเมินสิทธิ์ 149.00 SGD ถือว่าส่งมอบทันทีเมื่อเปิดระบบ และนำไปเป็นเครดิตหักลดหย่อนค่าติดตั้งจริงได้ 100% ภายใน 90 วัน",
            key="cb2"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        can_pay = company_name and business_email and check_b2b and check_fee
        
        if st.button("ชำระเงิน 149.00 SGD & เปิดสิทธิ์ Sandbox ทันที", disabled=not can_pay, type="primary", use_container_width=True):
            st.success(f"ระบบบันทึก Audit Log สัญญา Singapore Legal Pack v1.0 สำเร็จ! กำลังนำทางเข้าสู่ห้องทดลอง {st.session_state['selected_product']}...")
            # ส่งต่อไปยัง Sandbox Engine ที่เลือก
                if st.session_state['selected_product'] == "Autonomous Accounting & Tax Engine":
                    accounting_sandbox.render_accounting_sandbox()
                elif st.session_state['selected_product'] == "SME Retail & Node Automation":
                    retail_sandbox.render_retail_sandbox()
                elif st.session_state['selected_product'] == "Banking & Financial-Grade Ledger":
                    banking_sandbox.render_banking_sandbox()    
            
    with col_summary:
        st.markdown("### สรุปคำสั่งซื้อสิทธิ์ประเมิน")
        st.write(f"**โซลูชัน:** {st.session_state['selected_product']}")
        st.write("**สัญญากำกับ:** YBCAI99-SG-LEGAL-v1.0")
        st.write("**สถานะผู้ให้บริการ:** YBCAI99 System (Independent AI Lab)")
        st.write("**ค่าแรกเข้าฐาน:** 149.00 SGD")
        st.write("**ภาษี GST:** 0.00 SGD (Non-GST Registered / Reverse Charge)")
        st.markdown("---")
        st.markdown("### ยอดชำระสุทธิ: **149.00 SGD**")
        st.caption("💡 ค่าธรรมเนียมนี้สามารถนำไปหักลดหย่อนค่าสัญญาระบบจริง (Production License) ได้เต็มจำนวน 100%")
