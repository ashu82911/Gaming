import streamlit as st
from pages import home, ludo, chase, chat, matchmaking, profile, wallet

st.set_page_config(
    page_title="Play&Win",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;600;700&display=swap');
* { font-family: 'Inter', sans-serif; }
[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#0a0a0a,#1a0a2e,#0d0d2b) !important;
    border-right: 2px solid #7c3aed;
}
[data-testid="stSidebar"] * { color: #e2e8f0 !important; }
.main { background: #0f0f1a; }
.stButton>button {
    background: linear-gradient(90deg,#7c3aed,#4f46e5);
    color: white !important; border-radius: 12px; border: none;
    padding: 0.6rem 1.8rem; font-weight: 700; letter-spacing: 1px;
    box-shadow: 0 0 20px rgba(124,58,237,0.5); transition: all 0.3s;
}
.stButton>button:hover {
    box-shadow: 0 0 35px rgba(124,58,237,0.8); transform: translateY(-2px);
}
.stTextInput>div>div>input, .stSelectbox>div>div {
    background: #1a1a2e !important; color: white !important;
    border: 1px solid #7c3aed !important; border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ── Session State ────────────────────────────────────────────
defaults = {
    "player_name": "Ashu",
    "player_avatar": "🎮",
    "wallet_balance": 500,
    "wins": 12,
    "losses": 5,
    "chat_ludo": [
        {"user":"ProGamer_X","msg":"Ready to play! 🎲","time":"10:01"},
        {"user":"BlazeFire", "msg":"Let's go! 🔥",     "time":"10:02"},
        {"user":"Ashu",      "msg":"Game on! 💪",       "time":"10:03"},
    ],
    "chat_chase": [
        {"user":"NightOwl99","msg":"I'll win this time 😎","time":"09:45"},
        {"user":"Ashu",      "msg":"Challenge accepted! 🏃","time":"09:46"},
    ],
    "ludo_board": {},
    "chase_board": {"Ashu": 1, "Opponent": 1},
    "matchmaking_queue": [],
    "transactions": [
        {"type":"Add Money","amount":500,"status":"✅ Success","time":"Today 9:00 AM"},
        {"type":"Win",      "amount":100,"status":"✅ Credited","time":"Today 10:30 AM"},
        {"type":"Loss",     "amount":50, "status":"❌ Debited", "time":"Yesterday"},
    ],
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"""
    <div style='text-align:center;padding:1.2rem 0 0.5rem;'>
        <div style='font-size:3.5rem;'>🎮</div>
        <div style='font-size:1.6rem;font-weight:900;color:#a78bfa !important;
                    font-family:Orbitron,sans-serif;letter-spacing:2px;'>Play&Win</div>
        <div style='color:#7c3aed !important;font-size:0.72rem;letter-spacing:3px;'>
            GAMING PORTAL</div>
    </div>""", unsafe_allow_html=True)
    st.markdown("---")

    page = st.radio("", [
        "🏠  Home",
        "🎲  Ludo  (4 Players)",
        "🏃  Chase  (2 Players)",
        "💬  Chat Room",
        "🔍  Matchmaking",
        "👤  My Profile",
        "💰  Wallet",
    ])
    st.markdown("---")

    st.markdown(f"""
    <div style='background:linear-gradient(135deg,#1a0a2e,#2d1b69);
                border-radius:14px;padding:1rem;border:1px solid #7c3aed55;'>
        <div style='display:flex;align-items:center;gap:10px;'>
            <div style='font-size:2rem;'>{st.session_state.player_avatar}</div>
            <div>
                <div style='color:white !important;font-weight:700;'>
                    {st.session_state.player_name}</div>
                <div style='color:#a78bfa !important;font-size:0.75rem;'>
                    🏆 {st.session_state.wins}W · ❌ {st.session_state.losses}L</div>
            </div>
        </div>
        <div style='margin-top:0.6rem;background:#0f0f1a;border-radius:8px;
                    padding:6px 10px;text-align:center;'>
            <span style='color:#fbbf24 !important;font-weight:700;'>
                💰 ₹{st.session_state.wallet_balance}</span>
        </div>
    </div>""", unsafe_allow_html=True)

# ── Route ────────────────────────────────────────────────────
if   "Home"        in page: home.show()
elif "Ludo"        in page: ludo.show()
elif "Chase"       in page: chase.show()
elif "Chat"        in page: chat.show()
elif "Matchmaking" in page: matchmaking.show()
elif "Profile"     in page: profile.show()
elif "Wallet"      in page: wallet.show()
