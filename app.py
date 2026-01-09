import streamlit as st
import random
import time

# Page config
st.set_page_config(
    page_title="Friendship Moments",
    page_icon="🤗",
    layout="centered"
)

# ---------------- CSS FOR GRAPHICS & MOTION ----------------
st.markdown("""
<style>
@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-15px); }
  100% { transform: translateY(0px); }
}

@keyframes glow {
  0% { box-shadow: 0 0 10px #ff9a9e; }
  50% { box-shadow: 0 0 25px #fad0c4; }
  100% { box-shadow: 0 0 10px #ff9a9e; }
}

.card {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    padding: 35px;
    border-radius: 25px;
    text-align: center;
    animation: glow 3s infinite;
}

.hug {
    font-size: 90px;
    animation: float 2.5s ease-in-out infinite;
}

.note {
    font-size: 22px;
    color: #5a1a1a;
    font-weight: 500;
}

.fade {
    animation: float 4s ease-in-out infinite;
    font-size: 18px;
    color: #444;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown(
    "<h1 style='text-align:center; color:#ff4b4b;'>💖 Friendship Moments 💖</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='fade' style='text-align:center;'>Some bonds move the heart, not just the screen</p>",
    unsafe_allow_html=True
)

st.write("")

# ---------------- GRAPHIC CARD ----------------
st.markdown("""
<div class="card">
    <div class="hug">🧍‍♀️🤗🧍‍♂️</div>
    <p class="note">
        A hug can say what words never can.<br>
        Friendship lives in moments like this.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- INTERACTIVE CONTROLS ----------------
mood = st.select_slider(
    "🌈 Feel the friendship vibe",
    options=["Happy 😊", "Calm 🌸", "Emotional 💞", "Funny 😂", "Forever ♾️"]
)

quotes = {
    "Happy 😊": [
        "Smiles grow brighter when shared 🌞",
        "Friendship makes ordinary days special 🌸"
    ],
    "Calm 🌸": [
        "Peace feels better with a friend 🤍",
        "Silent moments can be the strongest bond 🌿"
    ],
    "Emotional 💞": [
        "A true friend understands without words ❤️",
        "Hearts connect deeper than distance 💫"
    ],
    "Funny 😂": [
        "Best friends = unlimited laughter 😆",
        "Life is better with shared jokes 🤪"
    ],
    "Forever ♾️": [
        "Some bonds are timeless ♾️",
        "Friendship never fades 💎"
    ]
}

# ---------------- BUTTON ACTION ----------------
if st.button("✨ Feel the Moment"):
    with st.spinner("Creating a friendship moment..."):
        time.sleep(1.5)

    st.success(random.choice(quotes[mood]))
    st.balloons()
    st.snow()

# ---------------- AUTO-CHANGING QUOTE ----------------
st.write("")
auto_quotes = [
    "Friendship is a journey, not a destination 🌍",
    "Small moments create strong bonds 🤍",
    "Together feels better ✨"
]

st.info(random.choice(auto_quotes))

# ---------------- FOOTER ----------------
st.markdown(
    "<p style='text-align:center; color:gray;'>Crafted with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)
