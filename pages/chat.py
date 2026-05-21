import streamlit as st
from datetime import datetime

def show():
    st.markdown("""<h2 style='color:#a78bfa;font-family:Orbitron,sans-serif;'>
        💬 Chat Rooms</h2>""", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🎲 Ludo Chat Room", "🏃 Chase Chat Room"])

    def render_chat(chat_key, room_name, color, players):
        msgs = st.session_state[chat_key]

        # Room header
        st.markdown(f"""
        <div style='background:linear-gradient(90deg,#1a0a2e,#0f0f1a);
                    border-radius:12px;padding:0.8rem 1.2rem;margin-bottom:1rem;
                    border:1px solid {color};display:flex;justify-content:space-between;'>
            <div>
                <span style='color:{color};font-weight:700;'>{room_name}</span>
                <span style='color:#94a3b8;font-size:0.8rem;margin-left:1rem;'>
                    👥 {len(players)} players online</span>
            </div>
            <span style='color:#10b981;font-size:0.8rem;'>🟢 Live</span>
        </div>""", unsafe_allow_html=True)

        # Online players
        p_html = "".join([f"<span style='background:{color}22;color:{color};padding:3px 10px;border-radius:12px;font-size:0.78rem;margin:2px;display:inline-block;'>👾 {p}</span>" for p in players])
        st.markdown(f"<div style='margin-bottom:0.8rem;'>{p_html}</div>", unsafe_allow_html=True)

        # Messages
        st.markdown("""
        <div style='background:#0a0a0a;border-radius:14px;padding:1rem;
                    height:350px;overflow-y:auto;border:1px solid #1a1a2e;'>""",
                    unsafe_allow_html=True)
        for m in msgs:
            is_me = m["user"] == st.session_state.player_name
            align = "flex-end" if is_me else "flex-start"
            bg    = f"linear-gradient(135deg,{color},{color}99)" if is_me else "#1a1a2e"
            st.markdown(f"""
            <div style='display:flex;justify-content:{align};margin:6px 0;'>
                <div style='max-width:70%;'>
                    <div style='color:#94a3b8;font-size:0.7rem;
                                text-align:{"right" if is_me else "left"};
                                margin-bottom:2px;'>{m["user"]} · {m["time"]}</div>
                    <div style='background:{bg};color:white;padding:8px 14px;
                                border-radius:{"14px 14px 4px 14px" if is_me else "14px 14px 14px 4px"};
                                font-size:0.9rem;'>{m["msg"]}</div>
                </div>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Input
        c1, c2 = st.columns([5,1])
        with c1:
            msg = st.text_input("", placeholder="Type a message... 😄🎲🏆",
                                key=f"msg_{chat_key}", label_visibility="collapsed")
        with c2:
            if st.button("Send 📤", key=f"send_{chat_key}"):
                if msg.strip():
                    st.session_state[chat_key].append({
                        "user": st.session_state.player_name,
                        "msg": msg,
                        "time": datetime.now().strftime("%H:%M")
                    })
                    st.rerun()

        # Quick emojis
        st.markdown("<div style='margin-top:6px;'>", unsafe_allow_html=True)
        e_cols = st.columns(8)
        emojis = ["😄","🎲","🏆","🔥","💪","😎","🎉","👏"]
        for col, emoji in zip(e_cols, emojis):
            with col:
                if st.button(emoji, key=f"emoji_{chat_key}_{emoji}"):
                    st.session_state[chat_key].append({
                        "user": st.session_state.player_name,
                        "msg": emoji,
                        "time": datetime.now().strftime("%H:%M")
                    })
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with tab1:
        render_chat("chat_ludo", "🎲 Ludo Room #4521", "#a78bfa",
                    ["Ashu","ProGamer_X","BlazeFire","NightOwl99"])
    with tab2:
        render_chat("chat_chase", "🏃 Chase Room #2341", "#10b981",
                    ["Ashu","Opponent"])
