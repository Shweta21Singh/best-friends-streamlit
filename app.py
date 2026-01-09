import streamlit as st
import random

# ---------- PAGE SETUP ----------
st.set_page_config(
    page_title="Best Friends",  # <-- Updated page title
    page_icon="🤗",
    layout="centered"
)

# ---------- SESSION STATE ----------
if "stage" not in st.session_state:
    st.session_state.stage = "idle"

# ---------- INPUT: BEST FRIEND NAME ----------
friend_name = st.text_input("Enter your Best Friend's Name 💛", "")

# ---------- CSS FOR ANIMATIONS ----------
st.markdown("""
<style>
.scene { position: relative; height: 260px; width: 100%; }
.friend { position: absolute; top: 80px; font-size: 80px; }
.left-idle { left: 5%; } .right-idle { right: 5%; }
.left-walk { animation: walkRight 2s forwards; } .right-walk { animation: walkLeft 2s forwards; }
@keyframes walkRight { from { left:5%; } to { left:40%; } }
@keyframes walkLeft  { from { right:5%; } to { right:40%; } }
.hug { font-size: 110px; text-align: center; animation: hugPulse 1.5s infinite; }
@keyframes hugPulse { 0% { transform: scale(1); } 50% { transform: scale(1.2); } 100% { transform: scale(1); } }
.shake { animation: shake 0.4s infinite; }
@keyframes shake { 0% { transform: rotate(0deg); } 25% { transform: rotate(5deg); } 50% { transform: rotate(0deg); } 75% { transform: rotate(-5deg); } 100% { transform: rotate(0deg); } }
.heart { position: absolute; font-size: 28px; animation: floatUp 3s infinite; }
@keyframes floatUp { 0% { opacity:0; transform: translateY(20px); } 50% { opacity:1; } 100% { opacity:0; transform: translateY(-80px); } }
.sparkle { text-align: center; font-size: 22px; animation: sparkle 1.5s infinite; }
@keyframes sparkle { 0% { opacity: 0.3; } 50% { opacity:1; } 100% { opacity:0.3; } }
.card { background: linear-gradient(135deg, #ffecd2, #fcb69f); padding: 25px; border-radius: 20px; text-align: center; margin-top: 20px; }
.bounce { animation: bounce 0.8s infinite; }
@keyframes bounce { 0% { transform: translateY(0); } 50% { transform: translateY(-12px); } 100% { transform: translateY(0); } }
.glow { filter: drop-shadow(0 0 15px #ffd700); }
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<h1 style='text-align:center; color:#ff4b4b;'>💖 Best Friends 💖</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Click buttons to see hugs, smiles, laughs and love!</p>", unsafe_allow_html=True)

# ---------- BUTTONS ----------
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("🚶 Walk"): st.session_state.stage = "walk"
with col2:
    if st.button("🤗 Hug"): st.session_state.stage = "hug"
with col3:
    if st.button("😊 Happy"): st.session_state.stage = "happy"
with col4:
    if st.button("😂 Funny"): st.session_state.stage = "funny"
with col5:
    if st.button("💞 Love"): st.session_state.stage = "love"

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
    st.success(f"True friends like {friend_name if friend_name else 'your Best Friend'} always come closer 🤍")
    st.balloons()
elif st.session_state.stage == "happy":
    st.markdown("<div class='hug bounce glow'>😄🤗😄</div>", unsafe_allow_html=True)
    st.success(f"Happiness grows when shared with {friend_name if friend_name else 'your Best Friend'} 🌸")
    st.balloons()
    st.markdown("""
    <div class="heart" style="left:40%;">💛</div>
    <div class="heart" style="left:45%; animation-delay:1s;">💚</div>
    <div class="heart" style="left:50%; animation-delay:2s;">💛</div>
    """, unsafe_allow_html=True)
elif st.session_state.stage == "funny":
    st.markdown("<div class='hug shake bounce'>🤣🤗🤣</div>", unsafe_allow_html=True)
    st.warning(f"Best friends like {friend_name if friend_name else 'your Best Friend'} make everything fun 😆")
    st.balloons()
    st.markdown("<div class='sparkle'>✨ ✨ ✨</div>", unsafe_allow_html=True)
elif st.session_state.stage == "love":
    st.markdown("<div class='hug bounce glow'>💞🤗💞</div>", unsafe_allow_html=True)
    st.success(f"Friendship filled with love with {friend_name if friend_name else 'your Best Friend'} lasts forever 💖")
    st.balloons()
    st.markdown("""
    <div class="heart" style="left:42%;">💖</div>
    <div class="heart" style="left:48%; animation-delay:1s;">💗</div>
    <div class="heart" style="left:46%; animation-delay:2s;">💞</div>
    """, unsafe_allow_html=True)

# ---------- GOOD THOUGHTS CARD ----------
thoughts = [
    "A friend like a hug for your heart 🤍",
    "Laughter, joy, and trust make friendship eternal 🌈",
    f"{friend_name if friend_name else 'Best friends'} are the family we choose 💖",
    "Hugs can say what words cannot ✨",
    "Friendship is not about words, it’s about moments 🌸"
]

st.markdown(f"""
<div class="card">
    {random.choice(thoughts)}
</div>
""", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("<p style='text-align:center; color:gray;'>All animations are Streamlit-safe & fully interactive ✨</p>", unsafe_allow_html=True)
