import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini-pro-vision model and get respones
model = genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_response(input, image):                          
    if input != " ":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("Fake Note Classifier")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Tell me about the Note")

## If ask button is clicked
if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)