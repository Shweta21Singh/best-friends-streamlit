import streamlit as st
import random

# Page setup
st.set_page_config(
    page_title="Best Friends Hug",
    page_icon="🤗",
    layout="centered"
)

# Custom CSS for graphics
st.markdown("""
<style>
body {
    background-color: #fff7f7;
}

.card {
    background: linear-gradient(135deg, #ffdde1, #ee9ca7);
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.15);
}

.hug {
    font-size: 90px;
    margin: 20px 0;
}

.note {
    font-size: 20px;
    color: #4a1c1c;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    "<h1 style='text-align:center; color:#ff4b4b;'>💖 Best Friends Forever 💖</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>A moment of warmth, trust, and friendship</p>",
    unsafe_allow_html=True
)

# Friendship card
st.markdown("""
<div class="card">
    <div class="hug">🧑‍🤝‍🧑🤗🧑‍🤝‍🧑</div>
    <p class="note">Some bonds don’t need words.<br>They are felt in a hug.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# Mood selector
mood = st.radio(
    "🌈 Choose the vibe",
    ["Happy 😊", "Emotional 💞", "Funny 😂", "Forever ♾️"],
    horizontal=True
)

quotes = {
    "Happy 😊": [
        "Friendship turns ordinary days into special ones 🌸",
        "Happiness is sharing smiles 🤍"
    ],
    "Emotional 💞": [
        "A hug from a friend can heal the heart ❤️",
        "True friends feel each other’s silence 🤍"
    ],
    "Funny 😂": [
        "Best friends laugh a little louder 😆",
        "Life is funnier with friends 🤪"
    ],
    "Forever ♾️": [
        "Some friendships are timeless ♾️",
        "Forever begins with a single bond 💎"
    ]
}

# Button action
if st.button("✨ Feel the Friendship"):
    st.success(random.choice(quotes[mood]))
    st.balloons()
    st.snow()

# Footer
st.markdown(
    "<p style='text-align:center; color:gray;'>Designed with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)


