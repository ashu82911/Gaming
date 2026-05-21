import streamlit as st

def show():
    st.markdown("""
    <div style='background:linear-gradient(135deg,#0a0a0a,#1a0a2e,#4c1d95);
                padding:3rem 2rem;border-radius:20px;text-align:center;
                margin-bottom:2rem;position:relative;overflow:hidden;'>
        <img src='https://images.unsplash.com/photo-1511512578047-dfb367046420?w=1200&q=60'
             style='position:absolute;top:0;left:0;width:100%;height:100%;
                    object-fit:cover;opacity:0.15;border-radius:20px;'/>
        <div style='position:relative;'>
            <div style='font-size:4rem;'>🎮</div>
            <h1 style='color:white;font-size:3rem;margin:0.3rem 0;font-weight:900;
                       font-family:Orbitron,sans-serif;letter-spacing:3px;
                       text-shadow:0 0 30px rgba(167,139,250,0.8);'>Play&Win</h1>
            <p style='color:#c4b5fd;font-size:1.1rem;margin:0;'>
                🎲 Ludo · 🏃 Chase · 💬 Chat · 🔍 Global Matchmaking</p>
            <div style='margin-top:1.5rem;'>
                <span style='background:rgba(124,58,237,0.3);color:#a78bfa;padding:6px 16px;
                             border-radius:20px;font-size:0.85rem;margin:4px;display:inline-block;
                             border:1px solid #7c3aed;'>🎲 Ludo 4 Players</span>
                <span style='background:rgba(124,58,237,0.3);color:#a78bfa;padding:6px 16px;
                             border-radius:20px;font-size:0.85rem;margin:4px;display:inline-block;
                             border:1px solid #7c3aed;'>🏃 Chase 2 Players</span>
                <span style='background:rgba(124,58,237,0.3);color:#a78bfa;padding:6px 16px;
                             border-radius:20px;font-size:0.85rem;margin:4px;display:inline-block;
                             border:1px solid #7c3aed;'>💰 Win Real Money</span>
                <span style='background:rgba(124,58,237,0.3);color:#a78bfa;padding:6px 16px;
                             border-radius:20px;font-size:0.85rem;margin:4px;display:inline-block;
                             border:1px solid #7c3aed;'>🌍 Global Players</span>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

    # Stats
    c1,c2,c3,c4 = st.columns(4)
    for col,(icon,val,label,color) in zip([c1,c2,c3,c4],[
        ("🏆", st.session_state.wins,            "Wins",          "#fbbf24"),
        ("❌", st.session_state.losses,           "Losses",        "#ef4444"),
        ("💰", f"₹{st.session_state.wallet_balance}", "Balance",  "#10b981"),
        ("🎮", st.session_state.wins + st.session_state.losses, "Games Played","#a78bfa"),
    ]):
        with col:
            st.markdown(f"""
            <div style='background:linear-gradient(135deg,#1a0a2e,#2d1b69);
                        padding:1.2rem;border-radius:14px;text-align:center;
                        border:1px solid {color}44;box-shadow:0 0 20px {color}22;'>
                <div style='font-size:1.8rem;'>{icon}</div>
                <div style='font-size:1.8rem;font-weight:800;color:{color};'>{val}</div>
                <div style='color:#94a3b8;font-size:0.82rem;'>{label}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Game cards
    st.markdown("""<h3 style='color:#a78bfa;font-family:Orbitron,sans-serif;'>
        🕹️ Choose Your Game</h3>""", unsafe_allow_html=True)

    g1, g2 = st.columns(2)
    with g1:
        st.markdown("""
        <div style='background:linear-gradient(135deg,#1a0a2e,#2d1b69);
                    border-radius:20px;overflow:hidden;border:2px solid #7c3aed;
                    box-shadow:0 0 30px rgba(124,58,237,0.3);'>
            <img src='https://images.unsplash.com/photo-1606503153255-59d5e417b6f4?w=600&q=70'
                 style='width:100%;height:200px;object-fit:cover;opacity:0.7;'/>
            <div style='padding:1.5rem;'>
                <h2 style='color:#a78bfa;margin:0;font-family:Orbitron,sans-serif;'>
                    🎲 LUDO</h2>
                <p style='color:#94a3b8;margin:0.5rem 0;'>
                    Classic Ludo for <strong style="color:#fbbf24;">4 Players</strong>.
                    Roll dice, move tokens, reach home first!</p>
                <div style='display:flex;gap:8px;flex-wrap:wrap;margin-top:0.8rem;'>
                    <span style='background:#7c3aed33;color:#a78bfa;padding:3px 10px;
                                 border-radius:12px;font-size:0.78rem;'>👥 4 Players</span>
                    <span style='background:#fbbf2433;color:#fbbf24;padding:3px 10px;
                                 border-radius:12px;font-size:0.78rem;'>💰 Entry Fee</span>
                    <span style='background:#10b98133;color:#10b981;padding:3px 10px;
                                 border-radius:12px;font-size:0.78rem;'>💬 Group Chat</span>
                    <span style='background:#ef444433;color:#ef4444;padding:3px 10px;
                                 border-radius:12px;font-size:0.78rem;'>🌍 Global Match</span>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)
        st.button("🎲 Play Ludo Now", key="home_ludo")

    with g2:
        st.markdown("""
        <div style='background:linear-gradient(135deg,#0a1a0a,#1b4d1b);
                    border-radius:20px;overflow:hidden;border:2px solid #10b981;
                    box-shadow:0 0 30px rgba(16,185,129,0.3);'>
            <img src='https://images.unsplash.com/photo-1611996575749-79a3a250f948?w=600&q=70'
                 style='width:100%;height:200px;object-fit:cover;opacity:0.7;'/>
            <div style='padding:1.5rem;'>
                <h2 style='color:#10b981;margin:0;font-family:Orbitron,sans-serif;'>
                    🏃 CHASE</h2>
                <p style='color:#94a3b8;margin:0.5rem 0;'>
                    Snake & Ladder for <strong style="color:#fbbf24;">2 Players</strong>.
                    Climb ladders, avoid snakes, reach 100!</p>
                <div style='display:flex;gap:8px;flex-wrap:wrap;margin-top:0.8rem;'>
                    <span style='background:#10b98133;color:#10b981;padding:3px 10px;
                                 border-radius:12px;font-size:0.78rem;'>👥 2 Players</span>
                    <span style='background:#fbbf2433;color:#fbbf24;padding:3px 10px;
                                 border-radius:12px;font-size:0.78rem;'>💰 Entry Fee</span>
                    <span style='background:#7c3aed33;color:#a78bfa;padding:3px 10px;
                                 border-radius:12px;font-size:0.78rem;'>💬 Private Chat</span>
                    <span style='background:#ef444433;color:#ef4444;padding:3px 10px;
                                 border-radius:12px;font-size:0.78rem;'>🌍 Global Match</span>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)
        st.button("🏃 Play Chase Now", key="home_chase")

    st.markdown("<br>", unsafe_allow_html=True)

    # Live matches
    st.markdown("""<h3 style='color:#a78bfa;font-family:Orbitron,sans-serif;'>
        🔴 Live Matches</h3>""", unsafe_allow_html=True)
    matches = [
        ("🎲","Ludo Room #4521","ProGamer_X vs BlazeFire vs NightOwl vs Ashu","₹50 entry","🟢 Live","#fbbf24"),
        ("🏃","Chase Room #2341","QuantumKid vs ShadowByte","₹100 entry","🟢 Live","#10b981"),
        ("🎲","Ludo Room #1122","CyberAshu vs StarPlayer vs Rahul vs Priya","₹20 entry","⏳ Waiting","#a78bfa"),
    ]
    for icon,room,players,fee,status,color in matches:
        st.markdown(f"""
        <div style='background:linear-gradient(90deg,#1a0a2e,#0f0f1a);
                    border-radius:12px;padding:1rem 1.5rem;margin:6px 0;
                    border-left:4px solid {color};display:flex;
                    justify-content:space-between;align-items:center;'>
            <div>
                <span style='font-size:1.2rem;'>{icon}</span>
                <strong style='color:white;margin-left:8px;'>{room}</strong>
                <div style='color:#94a3b8;font-size:0.82rem;margin-top:2px;'>{players}</div>
            </div>
            <div style='text-align:right;'>
                <div style='color:#fbbf24;font-weight:700;'>{fee}</div>
                <div style='color:{color};font-size:0.8rem;'>{status}</div>
            </div>
        </div>""", unsafe_allow_html=True)
