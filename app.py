import streamlit as st
import time

# Page setup
st.set_page_config(
    page_title="Good Friends Hug",
    page_icon="🤗",
    layout="centered"
)

# CSS for animation
st.markdown("""
<style>
.container {
    position: relative;
    height: 200px;
    width: 100%;
    overflow: hidden;
}

.friend {
    position: absolute;
    top: 50px;
    font-size: 80px;
    animation-duration: 3s;
    animation-fill-mode: forwards;
}

.left {
    left: 0%;
    animation-name: moveRight;
}

.right {
    right: 0%;
    animation-name: moveLeft;
}

@keyframes moveRight {
    from { left: 0%; }
    to { left: 40%; }
}

@keyframes moveLeft {
    from { right: 0%; }
    to { right: 40%; }
}

.hug {
    text-align: center;
    font-size: 90px;
    animation: hugPulse 1.5s infinite;
}

@keyframes hugPulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    "<h1 style='text-align:center; color:#ff4b4b;'>💖 Good Friends 💖</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Watch how true friends come together 🤍</p>",
    unsafe_allow_html=True
)

st.write("")

# Animation container
st.markdown("""
<div class="container">
    <div class="friend left">🧍‍♀️</div>
    <div class="friend right">🧍‍♂️</div>
</div>
""", unsafe_allow_html=True)

# Pause for movement
time.sleep(3)

# Hug moment
st.markdown(
    "<div class='hug'>🤗</div>",
    unsafe_allow_html=True
)

st.success("Good friends always find their way back to each other 💞")

st.balloons()

# Footer
st.markdown(
    "<p style='text-align:center; color:gray;'>Friendship shown through movement ✨</p>",
    unsafe_allow_html=True
)

    
