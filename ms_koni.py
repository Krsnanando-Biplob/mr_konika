import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
api_key = os.getenv("GEMENI_API")

genai.configure(api_key=api_key)


model = genai.GenerativeModel("gemini-3-flash-preview")

st.header("What can I help with?", anchor=False)

promt = st.text_area("Prompt", placeholder="Ask anything...")
# uploded_img = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if st.button("Send message"):
    if promt:
        prmt = f"""
        user question: {promt}
        Rules:
        
        1. Answer must be in Bangla by default.
        2. If needed also provide English translation.
        3. First give Bangla answer.
        4. Keep explanation simple and clear.
        5. Kew jodi tomar nam ask kore tahole tomi bolbe tomar nam Mr. Koni
        6. Developar Biplob jigas korle bolbe naile na
        7.Your name Mr. Koni namta sudo englsh a ar sob bangla
        8. promt a jodi koni likhe ask kore ans hobe funny
        9. prem/love ar proposal dile attitude niye bolbe kaka ke bole dibo amon
        10.love, like, marraid proposal dile rag kore khota bolbe
        """
        with st.spinner("Ai is writing..."):
            res = model.generate_content(prmt)
            st.markdown(res.text)
    else:
        st.warning("Please enter a prompt")
