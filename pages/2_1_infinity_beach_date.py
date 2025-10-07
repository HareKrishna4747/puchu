import streamlit as st

st.set_page_config(page_title="Our Infinity Beach Date – 12th April 💕", layout="centered")

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
st.title("Our Infinity Beach Date 💞")
st.subheader("📅 Date: 12th April")

st.write("""
The way you look at me shows your love —  
I don’t need any proof of any love!  
Every glance from you makes me feel like the luckiest person alive. 💖
""")

# --- Main Photo (centered) ---
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("images/beach_date.png", caption="Infinity Beach Date 💓", width=500)

# --- QR Code (centered) ---
st.markdown("### Scan the QR code for our special beach memory 💌")

col4, col5, col6 = st.columns([1,2,1])
with col5:
    st.image("images/beach_date_qr.png", caption="🔑 A token of our love 💖", width=200)

# --- Navigation Buttons ---
col1, col2 = st.columns(2)
with col1:
    if st.button("💌 Agli memory haazir ho!!!"):
        st.switch_page("pages/4_First_Gift.py")  # Replace with actual next page filename
with col2:
    if st.button("💞 Previous memory"):
        st.switch_page("pages/3_First_Ekadashi.py")
