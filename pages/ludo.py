import streamlit as st
import random

COLORS = {"Red":"🔴","Blue":"🔵","Green":"🟢","Yellow":"🟡"}
SAFE   = [1,9,14,22,27,35,40,48,53,61,66,74,79,87]

def init_ludo():
    return {c: [-1,-1,-1,-1] for c in COLORS}  # -1 = home, 0-56 = path, 57 = won

def show():
    st.markdown("""<h2 style='color:#a78bfa;font-family:Orbitron,sans-serif;'>
        🎲 LUDO — 4 Players</h2>""", unsafe_allow_html=True)

    # Setup
    if "ludo_state" not in st.session_state:
        st.session_state.ludo_state = {
            "board": init_ludo(),
            "turn": 0,
            "dice": 0,
            "rolled": False,
            "winner": None,
            "players": ["Ashu 🔴","Bot1 🔵","Bot2 🟢","Bot3 🟡"],
            "entry_fee": 50,
            "prize": 180,
        }
    s = st.session_state.ludo_state
    player_colors = ["Red","Blue","Green","Yellow"]
    current_color = player_colors[s["turn"] % 4]
    current_player = s["players"][s["turn"] % 4]

    # Entry fee banner
    st.markdown(f"""
    <div style='background:linear-gradient(90deg,#1a0a2e,#2d1b69);
                border-radius:12px;padding:1rem 1.5rem;margin-bottom:1rem;
                border:1px solid #7c3aed;display:flex;justify-content:space-between;'>
        <div>
            <span style='color:#a78bfa;font-weight:700;'>🎲 LUDO ROOM #4521</span>
            <span style='color:#94a3b8;font-size:0.82rem;margin-left:1rem;'>4/4 Players</span>
        </div>
        <div>
            <span style='color:#fbbf24;font-weight:700;'>💰 Entry: ₹{s["entry_fee"]}</span>
            <span style='color:#10b981;font-weight:700;margin-left:1rem;'>🏆 Prize: ₹{s["prize"]}</span>
        </div>
    </div>""", unsafe_allow_html=True)

    col_board, col_right = st.columns([3,2])

    with col_board:
        # Visual board
        st.markdown("""
        <div style='background:linear-gradient(135deg,#1a0a2e,#0f0f1a);
                    border-radius:16px;padding:1.5rem;border:2px solid #7c3aed;'>
            <div style='text-align:center;margin-bottom:1rem;'>
                <img src='https://images.unsplash.com/photo-1606503153255-59d5e417b6f4?w=500&q=70'
                     style='width:100%;max-height:300px;object-fit:cover;border-radius:12px;opacity:0.8;'/>
            </div>""", unsafe_allow_html=True)

        # Token positions
        for color, tokens in s["board"].items():
            icon = COLORS[color]
            pos_str = " | ".join([f"T{i+1}:{'Home' if t==-1 else 'Won🏆' if t==57 else f'Sq{t}'}"
                                   for i,t in enumerate(tokens)])
            st.markdown(f"""
            <div style='background:#0f0f1a;border-radius:8px;padding:6px 12px;
                        margin:4px 0;border-left:3px solid {"#ef4444" if color=="Red" else "#3b82f6" if color=="Blue" else "#10b981" if color=="Green" else "#fbbf24"};'>
                <span style='font-size:1rem;'>{icon}</span>
                <span style='color:#94a3b8;font-size:0.8rem;margin-left:8px;'>{pos_str}</span>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_right:
        if s["winner"]:
            st.markdown(f"""
            <div style='background:linear-gradient(135deg,#fbbf24,#f59e0b);
                        border-radius:16px;padding:2rem;text-align:center;'>
                <div style='font-size:3rem;'>🏆</div>
                <h2 style='color:#0a0a0a;margin:0;'>{s["winner"]} WINS!</h2>
                <p style='color:#0a0a0a;'>Prize: ₹{s["prize"]} credited!</p>
            </div>""", unsafe_allow_html=True)
            if st.button("🔄 New Game"):
                del st.session_state.ludo_state
                st.rerun()
        else:
            # Current turn
            st.markdown(f"""
            <div style='background:linear-gradient(135deg,#1a0a2e,#2d1b69);
                        border-radius:14px;padding:1.2rem;text-align:center;
                        border:2px solid #7c3aed;margin-bottom:1rem;'>
                <div style='color:#94a3b8;font-size:0.8rem;'>CURRENT TURN</div>
                <div style='font-size:2rem;'>{COLORS[current_color]}</div>
                <div style='color:white;font-weight:700;'>{current_player}</div>
            </div>""", unsafe_allow_html=True)

            # Dice
            dice_faces = ["","⚀","⚁","⚂","⚃","⚄","⚅"]
            if s["dice"] > 0:
                st.markdown(f"""
                <div style='text-align:center;font-size:5rem;
                            text-shadow:0 0 20px rgba(167,139,250,0.8);'>
                    {dice_faces[s["dice"]]}</div>
                <div style='text-align:center;color:#a78bfa;font-weight:700;'>
                    Rolled: {s["dice"]}</div>""", unsafe_allow_html=True)

            if not s["rolled"]:
                if st.button("🎲 Roll Dice", key="roll_ludo"):
                    s["dice"] = random.randint(1,6)
                    s["rolled"] = True
                    st.rerun()
            else:
                # Move token
                st.markdown("<div style='color:#94a3b8;font-size:0.85rem;'>Select token to move:</div>",
                            unsafe_allow_html=True)
                tokens = s["board"][current_color]
                for i, pos in enumerate(tokens):
                    can_move = (pos == -1 and s["dice"] == 6) or (0 <= pos < 57)
                    label = f"Token {i+1}: {'Home' if pos==-1 else f'Sq {pos}'}"
                    if st.button(label, key=f"move_{i}", disabled=not can_move):
                        if pos == -1 and s["dice"] == 6:
                            s["board"][current_color][i] = 1
                        elif 0 <= pos < 57:
                            new_pos = min(pos + s["dice"], 57)
                            s["board"][current_color][i] = new_pos
                        # Check win
                        if all(t == 57 for t in s["board"][current_color]):
                            s["winner"] = current_player
                            st.session_state.wallet_balance += s["prize"]
                        s["rolled"] = False
                        if s["dice"] != 6:
                            s["turn"] += 1
                        s["dice"] = 0
                        st.rerun()

                if st.button("⏭️ Skip Turn"):
                    s["rolled"] = False
                    s["turn"] += 1
                    s["dice"] = 0
                    st.rerun()

        # Players list
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""<div style='color:#a78bfa;font-weight:700;margin-bottom:8px;'>
            👥 Players</div>""", unsafe_allow_html=True)
        for i,(player,color) in enumerate(zip(s["players"],player_colors)):
            active = "border:2px solid #fbbf24;" if i == s["turn"]%4 else ""
            st.markdown(f"""
            <div style='background:#1a0a2e;border-radius:10px;padding:8px 12px;
                        margin:4px 0;{active}display:flex;justify-content:space-between;'>
                <span>{COLORS[color]} {player}</span>
                <span style='color:#94a3b8;font-size:0.78rem;'>
                    {sum(1 for t in s["board"][color] if t==57)}/4 home</span>
            </div>""", unsafe_allow_html=True)

    if st.button("🔄 Reset Game", key="reset_ludo"):
        del st.session_state.ludo_state
        st.rerun()
