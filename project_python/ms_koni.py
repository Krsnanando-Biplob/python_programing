
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("geratE_key")

genai.configure(api_key = api_key)


model = genai.GenerativeModel("gemini-3-flash-preview")

st.title("Radha Rani", anchor=False)

promt = st.text_area("Prompt",placeholder="Ask anything...")

if st.button("Send message"):
    if promt:
        res = model.generate_content(promt)
        st.write(res.text)
    else:
        st.warning("Please enter a prompt")
        