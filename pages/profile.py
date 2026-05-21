import streamlit as st

def show():
    st.markdown("""
    <div style='background:linear-gradient(135deg,#0a0a0a,#1a0a2e,#4c1d95);
                height:180px;border-radius:20px;margin-bottom:0;position:relative;overflow:hidden;'>
        <img src='https://images.unsplash.com/photo-1511512578047-dfb367046420?w=1200&q=60'
             style='width:100%;height:100%;object-fit:cover;opacity:0.3;'/>
        <div style='position:absolute;bottom:1rem;left:2rem;'>
            <h2 style='color:white;margin:0;font-family:Orbitron,sans-serif;'>
                {name}</h2>
        </div>
    </div>""".format(name=st.session_state.player_name), unsafe_allow_html=True)

    c1,c2,c3 = st.columns([1,4,2])
    with c1:
        st.markdown(f"""
        <div style='font-size:5rem;text-align:center;margin-top:-40px;
                    background:#1a0a2e;border-radius:50%;width:90px;height:90px;
                    display:flex;align-items:center;justify-content:center;
                    border:3px solid #7c3aed;'>
            {st.session_state.player_avatar}</div>""", unsafe_allow_html=True)
    with c2:
        total = st.session_state.wins + st.session_state.losses
        wr = round(st.session_state.wins/total*100) if total else 0
        st.markdown(f"""
        <div style='margin-top:0.5rem;'>
            <h3 style='color:#a78bfa;margin:0;'>{st.session_state.player_name}</h3>
            <p style='color:#94a3b8;margin:2px 0;'>🎮 Level 15 · ⭐ {wr}% Win Rate</p>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("✏️ Edit Profile")

    st.markdown("---")
    s1,s2,s3,s4 = st.columns(4)
    for col,(icon,val,label,color) in zip([s1,s2,s3,s4],[
        ("🏆", st.session_state.wins,   "Wins",    "#fbbf24"),
        ("❌", st.session_state.losses, "Losses",  "#ef4444"),
        ("💰", f"₹{st.session_state.wallet_balance}", "Balance","#10b981"),
        ("🎮", st.session_state.wins+st.session_state.losses,"Played","#a78bfa"),
    ]):
        with col:
            st.markdown(f"""
            <div style='background:#1a0a2e;padding:1.2rem;border-radius:14px;
                        text-align:center;border-bottom:3px solid {color};'>
                <div style='font-size:1.8rem;'>{icon}</div>
                <div style='font-size:1.8rem;font-weight:800;color:{color};'>{val}</div>
                <div style='color:#94a3b8;font-size:0.82rem;'>{label}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("✏️ Edit Profile"):
        st.session_state.player_name   = st.text_input("Username", value=st.session_state.player_name)
        st.session_state.player_avatar = st.selectbox("Avatar", ["🎮","👾","🕹️","🏆","⚡","🔥","💎","🦁"])
        if st.button("💾 Save"):
            st.success("Profile updated!")
