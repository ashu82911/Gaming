import streamlit as st
from datetime import datetime
import random

def show():
    st.markdown("""<h2 style='color:#fbbf24;font-family:Orbitron,sans-serif;'>
        💰 Wallet</h2>""", unsafe_allow_html=True)

    # Balance card
    st.markdown(f"""
    <div style='background:linear-gradient(135deg,#1a0a2e,#2d1b69);
                border-radius:20px;padding:2rem;text-align:center;
                border:2px solid #fbbf24;box-shadow:0 0 30px rgba(251,191,36,0.2);
                margin-bottom:1.5rem;'>
        <div style='color:#94a3b8;font-size:0.9rem;letter-spacing:2px;'>WALLET BALANCE</div>
        <div style='font-size:3.5rem;font-weight:900;color:#fbbf24;
                    font-family:Orbitron,sans-serif;'>
            ₹{st.session_state.wallet_balance}</div>
        <div style='color:#94a3b8;font-size:0.8rem;margin-top:4px;'>
            Available to play & withdraw</div>
    </div>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""<h3 style='color:#10b981;'>➕ Add Money</h3>""",
                    unsafe_allow_html=True)
        # Quick amounts
        st.markdown("**Quick Add:**")
        qa_cols = st.columns(4)
        for col, amt in zip(qa_cols, [100,200,500,1000]):
            with col:
                if st.button(f"₹{amt}", key=f"qa_{amt}"):
                    st.session_state.wallet_balance += amt
                    st.session_state.transactions.insert(0,{
                        "type":"Add Money","amount":amt,
                        "status":"✅ Success",
                        "time": datetime.now().strftime("%d %b, %I:%M %p")
                    })
                    st.success(f"₹{amt} added!")
                    st.rerun()

        custom = st.number_input("Custom Amount (₹)", min_value=10, max_value=10000, value=100)
        payment = st.selectbox("Payment Method", ["UPI","Net Banking","Credit Card","Debit Card"])
        if st.button("💳 Add Money", type="primary"):
            st.session_state.wallet_balance += custom
            st.session_state.transactions.insert(0,{
                "type":"Add Money","amount":custom,
                "status":"✅ Success",
                "time": datetime.now().strftime("%d %b, %I:%M %p")
            })
            st.success(f"✅ ₹{custom} added via {payment}!")
            st.rerun()

    with col2:
        st.markdown("""<h3 style='color:#ef4444;'>💸 Withdraw</h3>""",
                    unsafe_allow_html=True)
        w_amt = st.number_input("Withdraw Amount (₹)", min_value=100,
                                max_value=st.session_state.wallet_balance, value=100)
        w_method = st.selectbox("Withdraw To", ["Bank Account","UPI","Paytm"])
        upi_id = st.text_input("UPI ID / Account", placeholder="ashu@upi")
        if st.button("💸 Withdraw"):
            if w_amt <= st.session_state.wallet_balance:
                st.session_state.wallet_balance -= w_amt
                st.session_state.transactions.insert(0,{
                    "type":"Withdraw","amount":w_amt,
                    "status":"✅ Processed",
                    "time": datetime.now().strftime("%d %b, %I:%M %p")
                })
                st.success(f"✅ ₹{w_amt} withdrawn to {w_method}!")
                st.rerun()
            else:
                st.error("Insufficient balance!")

    st.markdown("---")
    st.markdown("""<h3 style='color:#a78bfa;'>📋 Transaction History</h3>""",
                unsafe_allow_html=True)
    for t in st.session_state.transactions:
        color = "#10b981" if "Add" in t["type"] or "Win" in t["type"] else "#ef4444"
        sign  = "+" if "Add" in t["type"] or "Win" in t["type"] else "-"
        st.markdown(f"""
        <div style='background:#1a0a2e;border-radius:12px;padding:0.8rem 1.2rem;
                    margin:6px 0;display:flex;justify-content:space-between;
                    border-left:4px solid {color};'>
            <div>
                <div style='color:white;font-weight:600;'>{t["type"]}</div>
                <div style='color:#94a3b8;font-size:0.78rem;'>{t["time"]}</div>
            </div>
            <div style='text-align:right;'>
                <div style='color:{color};font-weight:800;font-size:1.1rem;'>
                    {sign}₹{t["amount"]}</div>
                <div style='color:#94a3b8;font-size:0.75rem;'>{t["status"]}</div>
            </div>
        </div>""", unsafe_allow_html=True)
