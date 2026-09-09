import streamlit as st
import pandas as pd
import time

def render_retail_sandbox():
    st.markdown("## 🏬 SME Retail & Node Automation (Sandbox)")
    st.caption("ระบบจำลองเครือข่ายจุดขาย POS เชื่อมโยง 3–5 เครื่องลูกข่าย และตัดสต็อกอัตโนมัติ")

    st.markdown("### 1. สถานะการเชื่อมต่อเครือข่าย POS (Edge Nodes)")
    nodes_data = {
        "Node ID": ["POS-01 (หน้าร้านหลัก)", "POS-02 (เคาน์เตอร์บาร์)", "POS-03 (จุดบริการด่วน)"],
        "IP Address": ["192.168.1.101", "192.168.1.102", "192.168.1.103"],
        "สถานะการเชื่อมต่อ": ["🟢 ออนไลน์ (เสถียร)", "🟢 ออนไลน์ (เสถียร)", "🟡 กำลังซิงค์แคช"],
        "Latency": ["4 ms", "6 ms", "12 ms"]
    }
    st.table(pd.DataFrame(nodes_data))

    st.markdown("### 2. จำลองการขายหน้าร้านและตัดสต็อกส่วนกลาง")
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        selected_node = st.selectbox("เลือกเครื่อง POS ที่ทำรายการ", ["POS-01 (หน้าร้านหลัก)", "POS-02 (เคาน์เตอร์บาร์)", "POS-03 (จุดบริการด่วน)"])
        item = st.selectbox("เลือกสินค้า", ["สินค้า A - Premium Coffee (ถุง)", "สินค้า B - Organic Tea Box", "สินค้า C - Ceramic Mug"])
        qty = st.number_input("จำนวนที่ขาย", min_value=1, max_value=50, value=1)
        submit_sale = st.button("🚀 จำลองการยิงบาร์โค้ดขาย & ตัดสต็อก", type="primary", use_container_width=True)

    with col2:
        if submit_sale:
            st.success(f"บันทึกรายการสำเร็จจาก {selected_node}!")
            st.info(f"ตัดสต็อก: {item} จำนวน {qty} ชิ้น เรียบร้อยแล้ว")
            st.metric(label="เวลาประมวลผลคำสั่งข้ามโหนด", value="0.04 วินาที", delta="-0.01 วินาที (Fast Sync)")
        else:
            st.info("กรุณากดจำลองการยิงบาร์โค้ดเพื่อดูการซิงค์ข้อมูลสต็อกแบบเรียลไทม์")

if __name__ == "__main__":
    render_retail_sandbox()
