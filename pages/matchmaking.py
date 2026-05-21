import streamlit as st
import random, time

ONLINE_PLAYERS = [
    {"name":"ProGamer_X",  "level":42,"wins":230,"cost":50, "game":"Ludo", "status":"🟢 Ready"},
    {"name":"BlazeFire",   "level":38,"wins":180,"cost":50, "game":"Ludo", "status":"🟢 Ready"},
    {"name":"NightOwl99",  "level":29,"wins":120,"cost":100,"game":"Chase","status":"🟢 Ready"},
    {"name":"QuantumKid",  "level":55,"wins":310,"cost":100,"game":"Chase","status":"🟡 In Game"},
    {"name":"ShadowByte",  "level":21,"wins":90, "cost":20, "game":"Ludo", "status":"🟢 Ready"},
    {"name":"CyberAshu",   "level":33,"wins":150,"cost":20, "game":"Ludo", "status":"🟢 Ready"},
    {"name":"StarPlayer",  "level":47,"wins":260,"cost":50, "game":"Chase","status":"🟢 Ready"},
    {"name":"RocketMan",   "level":18,"wins":60, "cost":10, "game":"Ludo", "status":"🟢 Ready"},
]

def show():
    st.markdown("""<h2 style='color:#fbbf24;font-family:Orbitron,sans-serif;'>
        🔍 Global Matchmaking</h2>""", unsafe_allow_html=True)

    st.markdown("""
    <div style='background:linear-gradient(135deg,#1a0a2e,#2d1b69);
                border-radius:14px;padding:1.2rem 1.5rem;margin-bottom:1.5rem;
                border:1px solid #7c3aed;'>
        <h4 style='color:#a78bfa;margin:0 0 0.5rem 0;'>🌍 How Matchmaking Works</h4>
        <p style='color:#94a3b8;margin:0;font-size:0.9rem;'>
            Set your <strong style="color:#fbbf24;">entry cost</strong> and
            <strong style="color:#fbbf24;">game type</strong>.
            The system finds players with the <strong style="color:#10b981;">same cost</strong>
            globally. Winner takes the prize pool!
        </p>
    </div>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""<h3 style='color:#fbbf24;'>⚙️ Find a Match</h3>""",
                    unsafe_allow_html=True)

        game_type = st.selectbox("🎮 Select Game",
                                 ["🎲 Ludo (4 Players)","🏃 Chase (2 Players)"])
        entry_cost = st.selectbox("💰 Entry Cost",
                                  ["₹10","₹20","₹50","₹100","₹200","₹500"])
        room_type = st.radio("🔒 Room Type", ["🌍 Public (Auto Match)","🔐 Private Room"])

        cost_val = int(entry_cost.replace("₹",""))
        players_needed = 4 if "Ludo" in game_type else 2
        prize = int(cost_val * players_needed * 0.9)

        st.markdown(f"""
        <div style='background:#0f0f1a;border-radius:12px;padding:1rem;
                    border:1px solid #fbbf2444;margin:1rem 0;'>
            <div style='display:flex;justify-content:space-between;margin:4px 0;'>
                <span style='color:#94a3b8;'>Entry Cost</span>
                <span style='color:#fbbf24;font-weight:700;'>{entry_cost}</span>
            </div>
            <div style='display:flex;justify-content:space-between;margin:4px 0;'>
                <span style='color:#94a3b8;'>Players Needed</span>
                <span style='color:#a78bfa;font-weight:700;'>{players_needed}</span>
            </div>
            <div style='display:flex;justify-content:space-between;margin:4px 0;'>
                <span style='color:#94a3b8;'>Prize Pool</span>
                <span style='color:#10b981;font-weight:700;'>₹{prize}</span>
            </div>
            <div style='display:flex;justify-content:space-between;margin:4px 0;'>
                <span style='color:#94a3b8;'>Your Balance</span>
                <span style='color:{"#10b981" if st.session_state.wallet_balance >= cost_val else "#ef4444"};font-weight:700;'>
                    ₹{st.session_state.wallet_balance}</span>
            </div>
        </div>""", unsafe_allow_html=True)

        if "Private" in room_type:
            room_code = st.text_input("🔑 Enter Room Code (6 digits)",
                                      placeholder="e.g. 452198")
            if st.button("🚪 Join Private Room"):
                if room_code and len(room_code) == 6:
                    st.success(f"✅ Joined room {room_code}! Waiting for players...")
                    st.balloons()
                else:
                    st.error("Enter a valid 6-digit room code!")
            if st.button("➕ Create Private Room"):
                code = str(random.randint(100000,999999))
                st.success(f"✅ Room created! Share code: **{code}**")
        else:
            if st.session_state.wallet_balance < cost_val:
                st.error(f"❌ Insufficient balance! Add ₹{cost_val - st.session_state.wallet_balance} more.")
            else:
                if st.button("🔍 Find Match Now", type="primary"):
                    with st.spinner("🔍 Searching for players with same cost..."):
                        time.sleep(2)
                    matched = [p for p in ONLINE_PLAYERS
                               if p["cost"] == cost_val and
                               ("Ludo" in game_type and p["game"]=="Ludo" or
                                "Chase" in game_type and p["game"]=="Chase")][:players_needed-1]
                    if matched:
                        st.success(f"✅ Match found! {len(matched)+1}/{players_needed} players ready!")
                        for p in matched:
                            st.markdown(f"""
                            <div style='background:#1a0a2e;border-radius:10px;padding:8px 12px;
                                        margin:4px 0;border-left:3px solid #10b981;'>
                                👾 <strong style='color:white;'>{p["name"]}</strong>
                                <span style='color:#94a3b8;font-size:0.8rem;'>
                                    Lv.{p["level"]} · {p["wins"]} wins</span>
                            </div>""", unsafe_allow_html=True)
                        st.session_state.wallet_balance -= cost_val
                        st.info(f"₹{cost_val} deducted. Game starting...")
                    else:
                        st.warning("⏳ No players found yet. Try a different cost or wait...")

    with col2:
        st.markdown("""<h3 style='color:#10b981;'>🌍 Online Players</h3>""",
                    unsafe_allow_html=True)

        filter_game = st.selectbox("Filter by game",
                                   ["All","Ludo","Chase"], key="filter_game")
        filter_cost = st.selectbox("Filter by cost",
                                   ["All","₹10","₹20","₹50","₹100","₹200"], key="filter_cost")

        filtered = ONLINE_PLAYERS
        if filter_game != "All":
            filtered = [p for p in filtered if p["game"] == filter_game]
        if filter_cost != "All":
            filtered = [p for p in filtered if p["cost"] == int(filter_cost.replace("₹",""))]

        st.markdown(f"**{len(filtered)} players online**")
        for p in filtered:
            status_color = "#10b981" if "Ready" in p["status"] else "#fbbf24"
            st.markdown(f"""
            <div style='background:linear-gradient(90deg,#1a0a2e,#0f0f1a);
                        border-radius:12px;padding:0.8rem 1.2rem;margin:6px 0;
                        border:1px solid #7c3aed33;'>
                <div style='display:flex;justify-content:space-between;align-items:center;'>
                    <div>
                        <strong style='color:white;'>👾 {p["name"]}</strong>
                        <span style='color:#94a3b8;font-size:0.78rem;margin-left:8px;'>
                            Lv.{p["level"]} · 🏆{p["wins"]} wins</span>
                    </div>
                    <span style='color:{status_color};font-size:0.78rem;'>{p["status"]}</span>
                </div>
                <div style='margin-top:4px;display:flex;gap:8px;'>
                    <span style='background:#fbbf2422;color:#fbbf24;padding:2px 8px;
                                 border-radius:10px;font-size:0.75rem;'>💰 ₹{p["cost"]}</span>
                    <span style='background:#7c3aed22;color:#a78bfa;padding:2px 8px;
                                 border-radius:10px;font-size:0.75rem;'>🎮 {p["game"]}</span>
                </div>
            </div>""", unsafe_allow_html=True)
