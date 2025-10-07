import streamlit as st

st.set_page_config(page_title="For My Babygurl 💖", layout="centered")

# --- Custom Style ---
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #ffe6f0, #ffd6e0);
    font-family: 'Comic Sans MS', cursive, sans-serif;
}
h1, h2, h3 { text-align: center; color: #4b2e83; }
.stButton>button {
    background-color: #ff9aae;
    color: white;
    border-radius: 10px;
    padding: 0.6em 1.2em;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #ff7c96;
}
</style>
""", unsafe_allow_html=True)

# --- Verification ---
if "verified" not in st.session_state:
    st.session_state.verified = False

if not st.session_state.verified:
    st.title("💌 Who are you, beautiful?")
    st.write("Choose wisely 👇")

    col1, col2 = st.columns(2)
    with col1:
        strong = st.button("💪 Strong Independent Woman")
    with col2:
        babygurl = st.button("💖 Babygurl")

    if strong:
        st.error("🚫 Strong Independent Woman Not Allowed Here 🚫")
        st.warning("✨ Give an option to try again, maybe choose differently? 😉")

        if st.button("🔄 Try Again"):
            st.experimental_rerun()

    elif babygurl:
        st.success("Welcome to your exclusive zone, my babygurl 💖")
        st.session_state.verified = True
        st.rerun()

    st.stop()

# --- Memory Index Page ---
st.title("💖 Our Memories Together 💖")
st.write("Jayu's Puchki and Puchki's Jayu🌸")
st.image("images/main.jpeg", caption="Our journey, one memory at a time 💞", use_container_width=True)

# --- Option Buttons ---
col1, col2 = st.columns(2)
with col1:
    if st.button("💌 Pehli memory haazir ho!!!"):
        st.switch_page("pages/1_The_red_dress.py")
with col2:
    if st.button("💞 Add a New Memory"):
        st.info("Feature coming soon... stay tuned, babygurl 💫")
