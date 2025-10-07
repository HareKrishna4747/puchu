import streamlit as st

st.set_page_config(page_title="First Ekadashi Together – 8th April 💕", layout="centered")

# --- Custom Style ---
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #ffe6f0, #ffd6e0);
    font-family: 'Comic Sans MS', cursive, sans-serif;
}
h1, h2, h3 { text-align: center; color: #4b2e83; }
.stImage>img {
    border-radius: 15px;
    box-shadow: 0px 0px 15px #ff8fab;
}
</style>
""", unsafe_allow_html=True)

# --- Page Content ---
st.title("First Ekadashi Together 💞")
st.subheader("📅 Date: 8th April")

st.write("""
Baby, it was our first Ekadashi together.  
The way my head rested on your lap, I hope it remains like that for the rest of our 70 years.  
Every moment with you feels like eternity. 💖
""")

# --- Main Photo (centered) ---
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("images/first_ekadashi.png", caption="Our first Ekadashi together 💓", width=500)

# --- QR Code (centered) ---
st.markdown("### Scan the QR code for a sweet memory 💌")

col4, col5, col6 = st.columns([1,2,1])
with col5:
    st.image("images/first_ekadashi_qr.png", caption="🔑 A secret token of our first Ekadashi 💖", width=200)

# --- Navigation Buttons ---
col1, col2 = st.columns(2)
with col1:
    if st.button("💌 Agli memory haazir ho!!!"):
        st.switch_page("pages/2_1_infinity_beach_date.py")
with col2:
    if st.button("💞 Previous memory"):
        st.switch_page("pages/2_Looked_into_my_eyes.py")
