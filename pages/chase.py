import streamlit as st
import random

SNAKES  = {17:7, 54:34, 62:19, 64:60, 87:24, 93:73, 95:75, 99:78}
LADDERS = {4:14, 9:31, 20:38, 28:84, 40:59, 51:67, 63:81, 71:91}

def show():
    st.markdown("""<h2 style='color:#10b981;font-family:Orbitron,sans-serif;'>
        🏃 CHASE — 2 Players</h2>""", unsafe_allow_html=True)

    if "chase_state" not in st.session_state:
        st.session_state.chase_state = {
            "positions": {"Ashu 🟣": 0, "Opponent 🟠": 0},
            "turn": 0,
            "dice": 0,
            "rolled": False,
            "winner": None,
            "entry_fee": 100,
            "prize": 180,
            "history": [],
        }
    s = st.session_state.chase_state
    players = list(s["positions"].keys())
    current = players[s["turn"] % 2]

    # Room banner
    st.markdown(f"""
    <div style='background:linear-gradient(90deg,#0a1a0a,#1b4d1b);
                border-radius:12px;padding:1rem 1.5rem;margin-bottom:1rem;
                border:1px solid #10b981;display:flex;justify-content:space-between;'>
        <div>
            <span style='color:#10b981;font-weight:700;'>🏃 CHASE ROOM #2341</span>
            <span style='color:#94a3b8;font-size:0.82rem;margin-left:1rem;'>2/2 Players</span>
        </div>
        <div>
            <span style='color:#fbbf24;font-weight:700;'>💰 Entry: ₹{s["entry_fee"]}</span>
            <span style='color:#10b981;font-weight:700;margin-left:1rem;'>🏆 Prize: ₹{s["prize"]}</span>
        </div>
    </div>""", unsafe_allow_html=True)

    col_board, col_right = st.columns([3,2])

    with col_board:
        # Board visual — 10x10 grid
        st.markdown("""
        <div style='background:linear-gradient(135deg,#0a1a0a,#0f0f1a);
                    border-radius:16px;padding:1rem;border:2px solid #10b981;'>
            <div style='color:#10b981;font-weight:700;text-align:center;
                        margin-bottom:0.5rem;font-family:Orbitron,sans-serif;'>
                🐍 SNAKE & LADDER BOARD 🪜</div>""", unsafe_allow_html=True)

        pos_ashu = s["positions"][players[0]]
        pos_opp  = s["positions"][players[1]]

        rows = []
        for row in range(9, -1, -1):
            cols_row = []
            for col in range(10):
                sq = row * 10 + (col + 1 if row % 2 == 0 else 10 - col)
                cell = str(sq)
                style = "background:#1a1a2e;color:#94a3b8;"
                if sq in SNAKES:
                    style = "background:#ef444422;color:#ef4444;"
                    cell = f"🐍{sq}"
                elif sq in LADDERS:
                    style = "background:#10b98122;color:#10b981;"
                    cell = f"🪜{sq}"
                if sq == pos_ashu and sq == pos_opp:
                    cell = "🟣🟠"
                    style = "background:#fbbf2422;color:#fbbf24;"
                elif sq == pos_ashu:
                    cell = f"🟣{sq}"
                    style = "background:#7c3aed44;color:#a78bfa;"
                elif sq == pos_opp:
                    cell = f"🟠{sq}"
                    style = "background:#f9731644;color:#fb923c;"
                cols_row.append(f"<td style='padding:4px;text-align:center;font-size:0.7rem;border-radius:4px;{style}'>{cell}</td>")
            rows.append("<tr>" + "".join(cols_row) + "</tr>")

        st.markdown(f"""
        <div style='overflow-x:auto;'>
        <table style='width:100%;border-collapse:separate;border-spacing:2px;'>
            {"".join(rows)}
        </table></div>
        <div style='margin-top:0.5rem;font-size:0.75rem;color:#94a3b8;'>
            🐍 Snake (go down) &nbsp;|&nbsp; 🪜 Ladder (go up) &nbsp;|&nbsp;
            🟣 {players[0]} &nbsp;|&nbsp; 🟠 {players[1]}
        </div></div>""", unsafe_allow_html=True)

    with col_right:
        if s["winner"]:
            st.markdown(f"""
            <div style='background:linear-gradient(135deg,#fbbf24,#f59e0b);
                        border-radius:16px;padding:2rem;text-align:center;'>
                <div style='font-size:3rem;'>🏆</div>
                <h2 style='color:#0a0a0a;margin:0;'>{s["winner"]} WINS!</h2>
                <p style='color:#0a0a0a;'>Prize ₹{s["prize"]} credited!</p>
            </div>""", unsafe_allow_html=True)
            if st.button("🔄 New Game", key="chase_new"):
                del st.session_state.chase_state
                st.rerun()
        else:
            # Positions
            for p in players:
                pos = s["positions"][p]
                color = "#a78bfa" if "🟣" in p else "#fb923c"
                st.markdown(f"""
                <div style='background:#1a0a2e;border-radius:10px;padding:10px 14px;
                            margin:6px 0;border-left:3px solid {color};
                            display:flex;justify-content:space-between;'>
                    <span style='color:white;font-weight:600;'>{p}</span>
                    <span style='color:{color};font-weight:700;'>
                        Square {pos if pos > 0 else "Start"}</span>
                </div>""", unsafe_allow_html=True)

            # Turn indicator
            st.markdown(f"""
            <div style='background:linear-gradient(135deg,#0a1a0a,#1b4d1b);
                        border-radius:14px;padding:1rem;text-align:center;
                        border:2px solid #10b981;margin:1rem 0;'>
                <div style='color:#94a3b8;font-size:0.8rem;'>CURRENT TURN</div>
                <div style='color:#10b981;font-weight:700;font-size:1.1rem;'>{current}</div>
            </div>""", unsafe_allow_html=True)

            dice_faces = ["","⚀","⚁","⚂","⚃","⚄","⚅"]
            if s["dice"] > 0:
                st.markdown(f"""
                <div style='text-align:center;font-size:4rem;
                            text-shadow:0 0 20px rgba(16,185,129,0.8);'>
                    {dice_faces[s["dice"]]}</div>
                <div style='text-align:center;color:#10b981;font-weight:700;'>
                    Rolled: {s["dice"]}</div>""", unsafe_allow_html=True)

            if not s["rolled"]:
                if st.button("🎲 Roll Dice", key="roll_chase"):
                    roll = random.randint(1,6)
                    s["dice"] = roll
                    old_pos = s["positions"][current]
                    new_pos = old_pos + roll

                    msg = f"{current} rolled {roll}"
                    if new_pos > 100:
                        new_pos = old_pos
                        msg += " — can't move (need exact)"
                    elif new_pos in SNAKES:
                        msg += f" 🐍 Snake! {new_pos}→{SNAKES[new_pos]}"
                        new_pos = SNAKES[new_pos]
                    elif new_pos in LADDERS:
                        msg += f" 🪜 Ladder! {new_pos}→{LADDERS[new_pos]}"
                        new_pos = LADDERS[new_pos]

                    s["positions"][current] = new_pos
                    s["history"].insert(0, msg)
                    s["rolled"] = True

                    if new_pos == 100:
                        s["winner"] = current
                        st.session_state.wallet_balance += s["prize"]
                    st.rerun()
            else:
                if st.button("➡️ Next Turn", key="next_chase"):
                    s["turn"] += 1
                    s["rolled"] = False
                    s["dice"] = 0
                    st.rerun()

        # Move history
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""<div style='color:#10b981;font-weight:700;margin-bottom:6px;'>
            📜 Move History</div>""", unsafe_allow_html=True)
        for h in s["history"][:8]:
            st.markdown(f"""
            <div style='background:#0a1a0a;border-radius:8px;padding:5px 10px;
                        margin:3px 0;color:#94a3b8;font-size:0.8rem;'>{h}</div>""",
                        unsafe_allow_html=True)

    if st.button("🔄 Reset Game", key="reset_chase"):
        del st.session_state.chase_state
        st.rerun()
