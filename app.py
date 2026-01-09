import streamlit as st

# ---------- PAGE SETUP ----------
st.set_page_config(
    page_title="Happy Hug Animation",
    page_icon="🤗",
    layout="centered"
)

# ---------- SESSION STATE ----------
if "mode" not in st.session_state:
    st.session_state.mode = "idle"

# ---------- CSS (STREAMLIT SAFE) ----------
st.markdown("""
<style>
.scene {
    position: relative;
    height: 260px;
    width: 100%;
}

.friend {
    position: absolute;
    top: 90px;
    font-size: 85px;
}

.left { left: 35%; }
.right { right: 35%; }

/* Hug pulse */
.hug {
    font-size: 110px;
    text-align: center;
    animation: hugPulse 1.2s infinite;
}

@keyframes hugPulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.15); }
    100% { transform: scale(1); }
}

/* Glow aura */
.glow {
    filter: drop-shadow(0 0 15px #ffd700);
}

/* Floating hearts */
.heart {
    position: absolute;
    font-size: 28px;
    animation: floatUp 3s infinite;
}

@keyframes floatUp {
    0% { opacity: 0; transform: translateY(20px); }
    50% { opacity: 1; }
    100% { opacity: 0; transform: translateY(-80px); }
}

/* Bounce effect */
.bounce {
    animation: bounce 0.8s infinite;
}

@keyframes bounce {
    0% { transform: translateY(0); }
    50% { transform: translateY(-12px); }
    100% { transform: translateY(0); }
}

/* Sparkles */
.sparkle {
    text-align: center;
    font-size: 22px;
    animation: sparkle 1.5s infinite;
}

@keyframes sparkle {
    0% { opacity: 0.3; }
    50% { opacity: 1; }
    100% { opacity: 0.3; }
}

.card {
    background: linear-gradient(135deg, #ffe259, #ffa751);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown(
    "<h1 style='text-align:center; color:#ff4b4b;'>💖 Happy Hug 💖</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>A moment full of joy & friendship ✨</p>",
    unsafe_allow_html=True
)

# ---------- BUTTON ----------
if st.button("😊 Show Happy Hug"):
    st.session_state.mode = "happy"

# ---------- SCENE ----------
if st.session_state.mode == "happy":
    st.markdown("""
    <div class="scene">
        <div class="hug glow bounce">🤗</div>

        <div class="heart" style="left:40%;">💛</div>
        <div class="heart" style="left:45%; animation-delay:1s;">💖</div>
        <div class="heart" style="left:50%; animation-delay:2s;">💛</div>
        <div class="heart" style="left:55%; animation-delay:1.5s;">💖</div>

        <div class="sparkle">✨ ✨ ✨ ✨ ✨</div>
    </div>
    """, unsafe_allow_html=True)

    st.balloons()
    st.success("Happiness grows when hugs are shared 🤍")

# ---------- MESSAGE CARD ----------
st.markdown("""
<div class="card">
    True friendship shines brightest in happy moments 🌈
</div>
""", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown(
    "<p style='text-align:center; color:gray;'>All animations are Streamlit-safe & Cloud-ready</p>",
    unsafe_allow_html=True
)
