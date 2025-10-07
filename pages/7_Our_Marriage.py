import streamlit as st

st.set_page_config(page_title="Our Marriage – 23rd May 💍", layout="centered")

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
st.title("Our Marriage 💞")
st.subheader("📅 Date: 23rd May 2025")

st.write("""
Best day of my life. 💖  
The moment we said *“I do”*, I felt my world was complete.  
Every smile, every laugh, every tear that day belongs to us forever.  
I am so blessed to have you by my side 💍
""")

# --- Main Photo (centered) ---
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("images/marriage.png", caption="The happiest day of our life 💓", width=500)

# --- QR Code (centered) ---

# --- Navigation Buttons ---
col1, col2 = st.columns(2)
with col1:
    if st.button("💌 Agli memory haazir ho!!!"):
        st.switch_page("pages/sorry.py")
with col2:
    if st.button("💞 Previous memory"):
        st.switch_page("pages/7_Failed_Agreement.py")
