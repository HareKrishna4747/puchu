import streamlit as st

st.set_page_config(page_title="Prerna, Please… 💔", layout="centered")
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
    background: linear-gradient(120deg, #fff0f5, #ffe6ea);
    font-family: 'Comic Sans MS', cursive, sans-serif;
}
h1, h2, h3 { text-align: center; color: #7b2e2e; }
.stImage>img {
    border-radius: 15px;
    box-shadow: 0px 0px 15px #f08080;
}
p {
    text-align: center;
    font-size: 1.1rem;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# --- Page Content ---
st.title("Prerna… Please 💔")
st.subheader("A heartfelt plea from me to you")

st.write("""
Prerna,  
pls, I'm sorry.  
Bheekh managat hu. Jaisa Bhi hu tera hu.
Pls shaant ho jaa. Mian tera Jayu hu, sirf tera.
Pls puchu babygurl shaant ho jaa 💔  

I just want us to be okay again.  
""")

# --- (Optional) Photo or QR ---
