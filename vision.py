import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Image Application")

input = st.text_input("Imput Prompt")

image=""  

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")
if submit:
    res=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(res)
