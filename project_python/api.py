from google import genai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GENAVI_key")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Give me an idea about API in 100 words"
)

st.markdown(response.text)

