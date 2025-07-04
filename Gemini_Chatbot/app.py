import os
import streamlit as st
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

st.set_page_config(
    page_title="gemini-2.0-flash - Chatbot ",
    page_icon=":robot:",  # Favicon emoji
    layout="wide")

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("Gemini 2.0 flash - ChatBot")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)
user_prompt = st.chat_input("Ask gemini-2.0-flash...")


if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to gemini-2.0-flash and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display gemini-2.0-flash's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)

