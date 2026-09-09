import streamlit as st
import pandas as pd
import hashlib
import datetime

def render_banking_sandbox():
    st.markdown("## 🔒 Banking & Financial-Grade Ledger (Sandbox)")
    st.caption("ระบบจำลองสถาปัตยกรรม Air-Gapped บัญชีแยกประเภทแบบเข้ารหัส ป้องกันการแก้ไขย้อนหลัง (Immutable Ledger)")

    st.markdown("### 1. รายการธุรกรรมใน Ledger (Cryptographically Hashed)")
    sample_ledger = {
        "Block ID": ["#00104", "#00105", "#00106"],
        "Timestamp": ["2026-09-09 07:30:12", "2026-09-09 07:35:45", "2026-09-09 07:40:02"],
        "รายละเอียดธุรกรรม": [
            "Internal Transfer (SGD 12,500.00)",
            "Cross-Border Settlement (USD 4,200.00)",
            "Escrow Release - Vendor Contract"
        ],
        "Hash (SHA-256)": [
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
            "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
        ],
        "สถานะความปลอดภัย": ["🔒 Validated", "🔒 Validated", "🔒 Validated"]
    }
    st.table(pd.DataFrame(sample_ledger))

    st.markdown("### 2. จำลองการส่งคำสั่งธุรกรรมผ่าน Air-Gapped Signature")
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        tx_party = st.text_input("คู่สัญญา / บัญชีปลายทาง", value="Enterprise Clearing Account SG-09")
        tx_amount = st.number_input("จำนวนเงิน (SGD)", min_value=100.0, value=5000.0, step=500.0)
        sign_btn = st.button("🔐 ลงนามด้วยกุญแจเข้ารหัส (Offline Sign)", type="primary", use_container_width=True)

    with col2:
        if sign_btn:
            raw_data = f"{tx_party}-{tx_amount}-{datetime.datetime.now()}"
            tx_hash = hashlib.sha256(raw_data.encode()).hexdigest()
            st.success("ลงนามธุรกรรมสำเร็จ (Zero-Trust Verified)")
            st.code(f"Transaction Hash: {tx_hash}\nAir-Gapped Status: OK\nVerification: Passed", language="text")
        else:
            st.info("กรุณากดลงนามเพื่อจำลองการเข้ารหัสระดับธนาคาร")

if __name__ == "__main__":
    render_banking_sandbox()
