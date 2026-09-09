import streamlit as st
import pandas as pd
import datetime

def render_accounting_sandbox():
    st.markdown("## 📊 Autonomous Accounting & Tax Engine (Sandbox)")
    st.caption("ระบบอ่านบิล กระทบยอด 3-Way Matching และคำนวณภาษีอัตโนมัติ (IRAS IAF / Revenue Dept Compliant)")
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("### 1. นำเข้าเอกสารทางบัญชี")
        uploaded_file = st.file_uploader("อัปโหลดใบเสร็จ / ใบแจ้งหนี้ (PDF, PNG, JPG)", type=["pdf", "png", "jpg", "jpeg"])
        
        doc_type = st.selectbox("ประเภทเอกสาร", ["Commercial Invoice", "Tax Invoice / Receipt", "Purchase Order (PO)"])
        tax_regime = st.radio("ระบบภาษีที่ใช้คำนวณ", ["Singapore GST (9%)", "Thailand VAT (7%)", "Zero-Rated / Exempt"])
        
        simulate_scan = st.button("⚡ เริ่มประมวลผล OCR & Data Extraction", type="primary", use_container_width=True)
        
    with col2:
        st.markdown("### 2. ผลการตรวจสอบ 3-Way Matching & Tax")
        if simulate_scan or uploaded_file:
            st.success("ตรวจพบความถูกต้อง: ข้อมูลบิลตรงกับใบสั่งซื้อ (Matched 100%)")
            
            summary_data = {
                "รายการ": ["Subtotal (ก่อนภาษี)", "Tax Assessment", "Total Amount (ยอดสุทธิ)", "Audit Trail Status"],
                "มูลค่า / ผลการประเมิน": [
                    "1,500.00 SGD", 
                    "135.00 SGD (GST 9%)" if "9%" in tax_regime else "105.00 THB (VAT 7%)", 
                    "1,635.00 SGD" if "9%" in tax_regime else "1,605.00 THB", 
                    "Verified & Immutable"
                ]
            }
            st.table(pd.DataFrame(summary_data))
            
            st.download_button(
                label="📥 ส่งออก Audit File (IRAS IAF Standard)",
                data="Sample IAF Content - Audit Ready",
                file_name=f"audit_export_{datetime.date.today()}.txt",
                mime="text/plain",
                use_container_width=True
            )
        else:
            st.info("กรุณากดประมวลผลเพื่อดูตัวอย่างการกระทบยอดและโครงสร้างข้อมูลตรวจสอบ")

if __name__ == "__main__":
    render_accounting_sandbox()
