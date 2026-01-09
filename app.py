import streamlit as st

# ---------- PAGE SETUP ----------
st.set_page_config(
    page_title="Animated Friendship",
    page_icon="🤗",
    layout="centered"
)

# ---------- SESSION STATE ----------
if "stage" not in st.session_state:
    st.session_state.stage = "idle"

# ---------- CSS FOR ANIMATIONS ----------
st.markdown("""
<style>
.scene {
    position: relative;
    height: 260px;
    width: 100%;
}

/* Friend emojis */
.friend {
    position: absolute;
    top: 80px;
    font-size: 80px;
}

/* Idle position */
.left-idle { left: 5%; }
.right-idle { right: 5%; }

/* Walking animation */
.left-walk { animation: walkRight 2s forwards; }
.right-walk { animation: walkLeft 2s forwards; }

@keyframes walkRight { from { left:5%; } to { left:40%; } }
@keyframes walkLeft  { from { right:5%; } to { right:40%; } }

/* Hug pulse */
.hug {
    font-size: 110px;
    text-align: center;
    animation: hugPulse 1.5s infinite;
}

@keyframes hugPulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.2); }
    100% { transform: scale(1); }
}

/* Shake animation for funny hug */
.shake {
    animation: shake 0.4s infinite;
}
@keyframes shake {
    0% { transform: rotate(0deg); }
    25% { transform: rotate(5deg); }
    50% { transform: rotate(0deg); }
    75% { transform: rotate(-5deg); }
    100% { transform: rotate(0deg); }
}

/* Floating hearts */
.heart {
    position: absolute;
    font-size: 28px;
    animation: floatUp 3s infinite;
}

@keyframes floatUp {
    0% { opacity:0; transform: translateY(20px); }
    50% { opacity:1; }
    100% { opacity:0; transform: translateY(-80px); }
}

/* Sparkle effect */
.sparkle {
    text-align: center;
    font-size: 22px;
    animation: sparkle 1.5s infinite;
}

@keyframes sparkle {
    0% { opacity: 0.3; }
    50% { opacity:1; }
    100% { opacity:0.3; }
}

/* Card style */
.card {
    background: linear-gradient(135deg, #ffecd2, #fcb69f);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    margin-top: 20px;
}

/* Bounce for hug */
.bounce {
    animation: bounce 0.8s infinite;
}

@keyframes bounce {
    0% { transform: translateY(0); }
    50% { transform: translateY(-12px); }
    100% { transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<h1 style='text-align:center; color:#ff4b4b;'>💖 Animated Friendship 💖</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Click buttons to see hugs, smiles, laughs and emotions!</p>", unsafe_allow_html=True)

# ---------- BUTTONS ----------
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("🚶 Walk"):
        st.session_state.stage = "walk"
with col2:
    if st.button("🤗 Hug"):
        st.session_state.stage = "hug"
with col3:
    if st.button("😊 Happy"):
        st.session_state.stage = "happy"
with col4:
    if st.button("😂 Funny"):
        st.session_state.stage = "funny"
with col5:
    if st.button("💞 Love"):
        st.session_state.stage = "love"

# ---------- SCENE ----------
if st.session_state.stage == "idle":
    st.markdown("""
    <div class="scene">
        <div class="friend left-idle">🧍‍♀️</div>
        <div class="friend right-idle">🧍‍♂️</div>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.stage == "walk":
    st.markdown("""
    <div class="scene">
        <div class="friend left-idle left-walk">🧍‍♀️</div>
        <div class="friend right-idle right-walk">🧍‍♂️</div>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.stage == "hug":
    st.markdown("<div class='hug bounce glow'>🤗</div>", unsafe_allow_html=True)
    st.success("True friends always come closer 🤍")
    st.balloons()

elif st.session_state.stage == "happy":
    st.markdown("<div class='hug bounce glow'>😄🤗😄</div>", unsafe_allow_html=True)
    st.success("Happiness grows when shared 🌸")
    st.balloons()
    # Floating hearts
    st.markdown("""
    <div class="heart" style="left:40%;">💛</div>
    <div class="heart" style="left:45%; animation-delay:1s;">💚</div>
    <div class="heart" style="left:50%; animation-delay:2s;">💛</div>
    """, unsafe_allow_html=True)

elif st.session_state.stage == "funny":
    st.markdown("<div class='hug shake bounce'>🤣🤗🤣</div>", unsafe_allow_html=True)
    st.warning("Best friends make everything fun 😆")
    st.balloons()
    # Sparkles
    st.markdown("<div class='sparkle'>✨ ✨ ✨</div>", unsafe_allow_html=True)

elif st.session_state.stage == "love":
    st.markdown("<div class='hug bounce glow'>💞🤗💞</div>", unsafe_allow_html=True)
    st.success("Friendship filled with love lasts forever 💖")
    st.balloons()
    st.markdown("""
    <div class="heart" style="left:42%;">💖</div>
    <div class="heart" style="left:48%; animation-delay:1s;">💗</div>
    <div class="heart" style="left:46%; animation-delay:2s;">💞</div>
    """, unsafe_allow_html=True)

# ---------- MESSAGE CARD ----------
st.markdown("""
<div class="card">
    Friendship is about joy, laughter, hugs and love. Every moment counts! 🌈
</div>
""", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("<p style='text-align:center; color:gray;'>All animations are Streamlit-safe & fully interactive ✨</p>", unsafe_allow_html=True)
