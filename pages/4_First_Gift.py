import streamlit as st

st.set_page_config(page_title="Bubu – First Anniversary Gift 💕", layout="centered")
st.markdown("""
<style>
/* Hide Streamlit top-right hamburger menu */
#MainMenu {visibility: hidden;}

/* Hide Streamlit footer */
footer {visibility: hidden;}

/* Hide sidebar if exists */
[aria-label="Sidebar"] {display: none;}
</style>
""", unsafe_allow_html=True)
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
st.title("Bubu – The Most Beautiful Gift 💞")
st.subheader("📅 Date: 15th May 2025")

st.write("""
Bubu, the most beautiful gift given by you on our first anniversary together.  
Every time I see it, I am reminded of your love and thoughtfulness. Most beautiful of our moments aur uske captionss.  
I feel so blessed to have you in my life 💖
""")

# --- Main Photo (centered) ---
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("images/gift.png", caption="Our first anniversary gift 💓", width=500)

# --- QR Code (centered) ---
st.markdown("### Scan the QR code to relive this precious gift 💌")

col4, col5, col6 = st.columns([1,2,1])
with col5:
    st.image("images/gift_qr.png", caption="🔑 A token of your love 💖", width=200)

# --- Navigation Buttons ---
col1, col2 = st.columns(2)
with col1:
    if st.button("💌 Agli memory haazir ho!!!"):
        st.switch_page("pages/5_Meeting_Brother.py")
with col2:
    if st.button("💞 Previous memory"):
        st.switch_page("pages/3_First_Ekadashi.py")
