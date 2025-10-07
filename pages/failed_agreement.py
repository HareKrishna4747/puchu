import streamlit as st

st.set_page_config(page_title="Failed Agreement – 21st May 2025 💔", layout="centered")

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
st.title("Failed Agreement 💔")
st.subheader("📅 Date: 21st May 2025")

st.write("""
On this day, we made so many promises.  
I messed up everything.  
I’m sorry from the deepest part of my heart.  

I’m trying my best, baby. Please stay with me.  
Agar tune chod diya toh main akela ho jaunga.  
You’re my everything, my whole world 💖
""")

# --- Main Photo (centered) ---
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("images/failed_agreement.png", caption="The day of our promises 💓", width=500)

# --- QR Code (centered) ---
st.markdown("### Scan the QR code to revisit our promises 💌")

col4, col5, col6 = st.columns([1,2,1])
with col5:
    st.image("images/failed_agreement_qr.png", caption="🔑 A token of our promises 💖", width=200)

# --- Navigation Buttons ---
col1, col2 = st.columns(2)
with col1:
    if st.button("💌 Agli memory haazir ho!!!"):
        st.switch_page("pages/7_Our_Marriage.py")
with col2:
    if st.button("💞 Previous memory"):
        st.switch_page("pages/6_Airplane_Garden_Date.py")
