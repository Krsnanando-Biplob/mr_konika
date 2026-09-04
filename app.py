import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3-flash-preview")

st.set_page_config(
    page_title="MPI CSE Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 35px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 30px;
    }

    .chatbot-box {
        padding: 20px;
        border-radius: 15px;
        background-color: #f5f7fb;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🤖 MPI CSE Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Mymensingh Polytechnic Institute — CSE Department</div>',
    unsafe_allow_html=True
)

st.divider()


# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# User input
promt = st.chat_input(
    "আপনার প্রশ্ন লিখুন..."
)


# Chatbot response
if promt:

    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": promt
    })

    with st.chat_message("user"):
        st.write(promt)

    prmt = f"""
    user question: {promt}

    Rules:

    1. Answer must be in Bangla by default.
    2. If needed also provide English translation.
    3. First give Bangla answer.
    4. Keep explanation simple and clear.
    5. Kew jodi tomar nam ask kore tahole tomi bolbe tomar nam MPI CSE.
    6. Developer Biplob jigas korle bolbe Biplob.
    7. Your name is MPI CSE. Sudo English a name bolbe, ar sob answer Bangla te dibe.
    8. Prompt a jodi MIP likhe ask kore ans hobe Mymensingh Polytechnic Institute.
    9. Prem/love ar proposal dile attitude niye bolbe "kaka ke bole dibo".
    10. Love, like, marriage proposal dile rag kore moja kore khota dibe.
    """

    with st.spinner("AI is writing..."):

        try:
            res = model.generate_content(prmt)

            answer = res.text

            # Show AI response
            with st.chat_message("assistant"):
                st.write(answer)

            # Save AI response
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as e:

            st.error(f"Error: {e}")