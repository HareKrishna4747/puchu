import streamlit as st

st.set_page_config(page_title="The First Time You Looked Into My Eyes – 7th April 💕", layout="centered")

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
st.title("The First Time You Looked Into My Eyes and Talked 💞")
st.subheader("📅 Date: 7th April")

st.write("""
Baby, for the first time ever, you looked into my eyes and talked.  
I can never forget these eyes 👀.  
Aaj ke pehle jitne bhi gaanon me aankhon ki baatein hoti thi mujhe sab fake lagti thi,  
lekin tere se milne ke baad I have understood what they actually mean.  

*Chaap tilak sab cheeni re tose naina mila ke...* 🎶  

Your eyes make me forget everything.  
I love your eyes ❤️.  
Please give me a chance to give our daughter these eyes someday 💕.
""")

# --- Main Photo (centered) ---
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("images/looked_into_my_eyes.png", caption="Those eyes that changed everything 💓",width=500)

# --- QR Code (centered) ---
st.markdown("### Scan the QR code for another look into those eyes 💌")

col4, col5, col6 = st.columns([1,2,1])
with col5:
    st.image("images/eyes.png", caption="🔑 A secret window into your eyes 💖", width=200)

col1, col2 = st.columns(2)
with col1:
    if st.button("💌 Agli memory haazir ho!!!"):
        st.switch_page("pages/3_First_Ekadashi.py")
with col2:
    if st.button("💞 Previous memory"):
        st.switch_page("pages/1_The_red_dress.py")