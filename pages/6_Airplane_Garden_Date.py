import streamlit as st

st.set_page_config(page_title="First Airplane Garden Date – 19th May 💕", layout="centered")

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
st.title("First Airplane Garden Date 💞")
st.subheader("📅 Date: 19th May")

st.write("""
Before this, we ate wada sambar.  
Remember how the watchman said, *"Ki bahut chalak ladki hain"*? 😄  
That day was full of laughter, love, and little surprises — memories I’ll cherish forever 💖
""")

# --- Main Photo (centered) ---
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("images/garden.png", caption="Our first airplane garden date 💓", width=500)

# --- QR Code (centered) ---
st.markdown("### Scan the QR code to relive this cute moment 💌")

col4, col5, col6 = st.columns([1,2,1])
with col5:
    st.image("images/garden_qr.png", caption="🔑 A memory frozen in time 💖", width=200)

# --- Navigation Buttons ---
col1, col2 = st.columns(2)
with col1:
    if st.button("💌 Agli memory haazir ho!!!"):
        st.switch_page("pages/failed_agreement.py")
with col2:
    if st.button("💞 Previous memory"):
        st.switch_page("pages/5_Meeting_Brother.py")
