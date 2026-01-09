import streamlit as st

# ---------------- PAGE SETUP ----------------
st.set_page_config(
    page_title="Animated Friendship",
    page_icon="🤗",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "stage" not in st.session_state:
    st.session_state.stage = "idle"

# ---------------- CSS (STREAMLIT SAFE) ----------------
st.markdown("""
<style>
.scene {
    position: relative;
    height: 220px;
    width: 100%;
}

.friend {
    position: absolute;
    top: 60px;
    font-size: 80px;
}

.left-idle { left: 5%; }
.right-idle { right: 5%; }

.left-walk {
    animation: walkRight 2s forwards;
}
.right-walk {
    animation: walkLeft 2s forwards;
}

@keyframes walkRight {
    from { left: 5%; }
    to { left: 40%; }
}

@keyframes walkLeft {
    from { right: 5%; }
    to { right: 40%; }
}

.hug {
    text-align: center;
    font-size: 100px;
    animation: hugPulse 1.5s infinite;
}

@keyframes hugPulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.15); }
    100% { transform: scale(1); }
}

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

.card {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown(
    "<h1 style='text-align:center; color:#ff4b4b;'>💖 Good Friends 💖</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>Buttons control emotions & movement</p>",
    unsafe_allow_html=True
)

# ---------------- BUTTONS ----------------
col1, col2, col3, col4 = st.columns(4)

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

# ---------------- SCENE ----------------
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
    st.markdown("<div class='hug'>🤗</div>", unsafe_allow_html=True)
    st.success("True friends always come closer 🤍")

elif st.session_state.stage == "happy":
    st.markdown("<div class='hug'>🤗</div>", unsafe_allow_html=True)
    st.success("Happiness is better when shared 🌸")
    st.balloons()

elif st.session_state.stage == "funny":
    st.markdown("<div class='hug shake'>🤗</div>", unsafe_allow_html=True)
    st.warning("Best friends make everything fun 😆")
    st.balloons()

# ---------------- MESSAGE CARD ----------------
st.markdown("""
<div class="card">
    Friendship is not about words, it’s about moments.
</div>
""", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown(
    "<p style='text-align:center; color:gray;'>Stable animation using Streamlit session state</p>",
    unsafe_allow_html=True
)



