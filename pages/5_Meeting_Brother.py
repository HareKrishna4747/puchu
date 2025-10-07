import streamlit as st

st.set_page_config(page_title="Meeting Your Brother – 17th May 💕", layout="centered")

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
st.title("Date With Your Brother 💞")
st.subheader("📅 Date: 17th May")

st.write("""
Baby, I was never doubtful about how serious you are with our relationship.  
Haan, main gussa mein kuch bhi bol deta hoon, lekin I don't doubt anything.  
Meeting your brother made me feel closer to you and your world 💖
""")

# --- Main Photo (centered) ---
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("images/brother.png", caption="Meeting your brother 💓", width=500)

# --- QR Code (centered) ---
st.markdown("### Scan the QR code for a sweet memory 💌")

col4, col5, col6 = st.columns([1,2,1])
with col5:
    st.image("images/brother_qr.png", caption="🔑 A token of that special day 💖", width=200)

# --- Navigation Buttons ---
col1, col2 = st.columns(2)
with col1:
    if st.button("💌 Agli memory haazir ho!!!"):
        st.switch_page("pages/6_Airplane_Garden_Date.py")
with col2:
    if st.button("💞 Previous memory"):
        st.switch_page("pages/4_First_Gift.py")
