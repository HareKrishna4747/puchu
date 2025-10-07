import streamlit as st

st.set_page_config(page_title="The Red Dress – 6th April 💃", layout="centered")
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
st.title("The Most Awaited Day of My Life 💖")
st.subheader("📅 Date: 6th April 2025")

st.write("""
Bubu, the best day of my life.  
First time in my life, I was this excited to meet someone.  
I dressed thoughtfully for the first time. You told me you loved sunflowers 🌻.  
We had such a wonderful day, walked on Bandstand, uss khali street par, we enjoyed McDonald's 🍔.  

Remember teri dress ki string tut gyi thi and you wished it happened after i came there.  
Babygurl, I love you 💞
""")

# --- Main Photo ---
st.image("images/red_dress.png", caption="You in red, my heart skipped a beat 💓")

# --- QR Code ---
st.markdown("### Scan the QR code for exclusive entry into Jayu's heart 💌")
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("images/lal_pari.png", caption="🔑 Secret entry to Jayu's heart 💖", width=200)

col1, col2 = st.columns(2)
with col1:
    if st.button("💌 Agli memory haazir ho!!!"):
        st.switch_page("pages/2_Looked_into_my_eyes.py")
with col2:
    if st.button("💞 Previous memory"):
        st.switch_page("app.py")
