import streamlit as st
import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(question):
    response = model.generate_content("Write a 4 lines poem on " + question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Poem Demo")
st.header("Gemini Poem Application")
user_input = st.text_input("Topic")
submit = st.button("Generate Poem")
if submit:
    res = get_gemini_response(user_input)
    st.subheader("Poem on " + user_input)        
    st.write(res)
