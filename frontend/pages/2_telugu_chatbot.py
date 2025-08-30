import streamlit as st
import google.generativeai as genai
import os

# --- Custom CSS for professional styling ---
st.markdown("""
<style>
    @import url('https://fonts.com/css2?family=Noto+Sans+Telugu:wght@400;700&display=swap');
    
    html, body, [class*="st-emotion-cache"] {
        font-family: 'Noto Sans Telugu', sans-serif;
    }
    .main-title {
        text-align: center;
        font-size: 3rem;
        color: #FFDAC1;
        font-weight: bold;
        margin-bottom: -0.5rem;
        text-shadow: 2px 2px 4px #000000;
    }
    .main-subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #B5EAD7;
        margin-bottom: 2rem;
    }
    .st-emotion-cache-1cypcdp {
        background-color: #2F3640; /* Chatbot background */
        border-radius: 10px;
        padding: 1rem;
        border: 1px solid #4A4A4A;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .st-emotion-cache-1oe58a9 {
        padding-top: 1rem;
    }
    .st-emotion-cache-h5h9f7 { /* User message bubble */
        background-color: #3F515B;
        border-radius: 10px;
        padding: 10px;
    }
    .st-emotion-cache-1r3feq5 { /* Bot message bubble */
        background-color: #2D3E4E;
        border-radius: 10px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. Configure the Google Generative AI API Key ---
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except KeyError:
    st.error("API Key not found. Please set `GOOGLE_API_KEY` in `secrets.toml`.")
    st.stop()

genai.configure(api_key=api_key)

# --- 2. Initialize the Gemini Model with a System Instruction ---
model_name = "gemini-1.5-flash"
# FIX: The system instruction is rephrased to be less restrictive, allowing the model
# to answer questions about a wider range of Telugu literary figures and topics.
system_instruction = (
    "You are a helpful and knowledgeable chatbot specialized in Telugu literature. "
    "Your name is 'Sahitya Sreshta' (సాహిత్య శ్రేష్ఠ). "
    "You can answer questions related to Telugu literature, poetry, famous authors, and literary works. "
    "Provide a detailed and comprehensive answer to each question. "
    "Your responses must be in conversational Telugu. "
    "For example: 'తెలుగు కవిత్వ పితామహుడు అల్లసాని పెద్దన.' "
    "If a question is not about Telugu literature, politely and conversationally respond in Telugu that you can only answer questions about that topic."
)
model = genai.GenerativeModel(
    model_name=model_name,
    system_instruction=system_instruction,
)

# --- 3. Set a descriptive page title and icon ---
st.set_page_config(
    page_title="తెలుగు సాహిత్య చాట్‌బాట్",
    page_icon="📚",
    layout="wide"
)

# --- Display Title and Subtitle ---
st.markdown("<h1 class='main-title'>📚 తెలుగు సాహిత్య చాట్‌బాట్</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='main-subtitle'>మీకు తెలుగు సాహిత్యం గురించి ఏది కావాలంటే అది అడగండి.</h3>", unsafe_allow_html=True)

# --- 4. Handle Chat History ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.chat_history.append({"role": "bot", "content": "నమస్తే! నేను తెలుగు సాహిత్యం గురించి సమాచారం అందించే చాట్ బాట్‌ని. మీకు ఏ విషయం గురించి తెలుసుకోవాలని ఉంది?"})

# --- 5. Display Chat Messages ---
for message in st.session_state.chat_history:
    role = "user" if message["role"] == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message["content"])

# --- 6. Handle User Input ---
if prompt := st.chat_input("మీ ప్రశ్న ఇక్కడ టైప్ చేయండి..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        with st.spinner("సాహిత్య శ్రేష్ఠ స్పందిస్తోంది..."):
            chat = model.start_chat()
            response = chat.send_message(prompt)
            bot_response = response.text
    except Exception as e:
        bot_response = f"క్షమించండి, మీ అభ్యర్థనను ప్రాసెస్ చేయడంలో ఒక లోపం జరిగింది: {e}"

    st.session_state.chat_history.append({"role": "bot", "content": bot_response})
    
    with st.chat_message("assistant"):
        st.markdown(bot_response)
