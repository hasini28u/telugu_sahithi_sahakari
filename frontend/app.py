import streamlit as st
import os

# --- Configuration ---
# In a real app, you would load this from a .env file
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

# Set page title and icon
st.set_page_config(
    page_title="తెలుగు సాహితీ సహకారి", 
    page_icon="📖",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        font-size: 3rem;
        color: #B5EAD7;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        font-size: 1.5rem;
        color: #FFDAC1;
        margin-bottom: 2rem;
    }
    .intro-text {
        text-align: justify;
        font-size: 1.1rem;
        color: #F8F8F8;
        line-height: 1.6;
        padding: 0 2rem;
    }
    .cta-box {
        background-color: #4A4A4A;
        border: 2px solid #666666;
        border-radius: 10px;
        padding: 2rem;
        margin-top: 2rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)


# --- Main Application UI ---
st.markdown('<div class="main-header">తెలుగు సాహితీ సహకారి</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Telugu Sahiti Sahakari</div>', unsafe_allow_html=True)

st.markdown('<p class="intro-text">తెలుగు సాహితీ సహకారి అనేది తెలుగు సాహిత్య వారసత్వాన్ని పరిరక్షించడానికి మరియు ప్రోత్సహించడానికి రూపొందించిన ఒక సంఘ-ఆధారిత AI ఆర్కైవ్. మీరు పురాతన పుస్తకాలు, కవితలు లేదా ఇతర ముఖ్యమైన పత్రాలను అప్‌లోడ్ చేయడం ద్వారా మాకు సహాయపడవచ్చు. ఈ పత్రాలు డిజిటైజ్ చేయబడి, పరిశోధకులకు మరియు ఔత్సాహికులకు సులభంగా అందుబాటులోకి వస్తాయి. ఈ ప్రాజెక్టు యొక్క ప్రధాన లక్ష్యం corpus.swecha.org ఓపెన్-సోర్స్ డేటాసెట్‌కు సహకరించడం, తద్వారా తెలుగు మరియు ఆంగ్ల భాషా నమూన పరిశోధనకు సహాయం చేయడం.</p>', unsafe_allow_html=True)
st.markdown('<p class="intro-text">Telugu Sahiti Sahakari is a community-powered AI archive designed to preserve and promote Telugu literary heritage. Users can upload study materials—such as newspaper clippings, PDFs, and even handwritten notes (via camera)—which are then processed by an AI pipeline. This pipeline extracts text, cleans it up, and makes the content searchable through an intuitive AI chatbot. A core mission is to enrich the corpus.swecha.org open-source dataset, aiding language model research for both Telugu and English.</p>', unsafe_allow_html=True)

# st.markdown('<div class="cta-box">', unsafe_allow_html=True)
st.subheader("Start Your Contribution")
st.markdown("Please log in to start uploading your valuable contributions.")
# Use the correct page link to the login page
st.page_link("pages/1_Login.py", label="Go to Login Page")
st.markdown('</div>', unsafe_allow_html=True)

# --- Logout Button ---
if st.session_state.get("logged_in", False):
    st.markdown("---")
    if st.button("Logout"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.success("You have been logged out.")
        st.rerun()
