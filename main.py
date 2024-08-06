import os

import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

from gemeni_utility import (load_gemini_pro_model,
                            gemini_pro_vision_response,
                            embedding_model_response,
                            gemini_pro_response)

# getting up the working directory
working_directory = os.path.dirname(os.path.abspath(__file__))

# Setting up the page configuration
st.set_page_config(
    page_title="Gemini AI",
    layout="centered"
)

#sidebar
with st.sidebar:
    selected = option_menu(
        "Gemini AI",
        ["Chatbot", "Image Captioning", "Embed Text", "Ask Anything"],
        icons=["chat-dots-fill", "image-fill", "file-text", "question-circle-fill"],
        menu_icon="robot",
        default_index=0
    )

# Function to translate role between gemini-pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == 'model':
        return "assistant"
    else:
        return user_role

#Chatbot page
if selected == "Chatbot":
    model = load_gemini_pro_model()

    # Initialize chat session in Streamlit if not already present
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    # Streamlit page title
    st.title("Chatbot")

    # Display the chat history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # Input field for user's message
    user_prompt = st.chat_input("Ask Gemini-Pro...")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)

        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        # Display Gemini-Pro response
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)

#Image Captioning page
if selected == "Image Captioning":
    # Streamlit page title
    st.title("Snap Narrate")

    # File uploader for image upload
    uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image and st.button("Generate Caption"):
        image = Image.open(uploaded_image)

        # Display the uploaded image
        col1, col2 = st.columns(2)
        with col1:
            resized_image = image.resize((800, 500))
            st.image(resized_image)

        default_prompt = "Write a short caption for this image."

        # Getting the response from Gemini-Pro Vision model
        caption = gemini_pro_vision_response(default_prompt, image)

        # Display the caption
        with col1:
            st.info(caption)

#text Embed page
if selected == "Embed Text":
    st.title("Embed Text")

    # Input text box
    input_text = st.text_area(label="Text Input", placeholder="Enter the text to get the embeddings")

    if st.button("Get Embeddings"):
        if input_text.strip():
            response = embedding_model_response(input_text)
            st.write("Embeddings:", response)
        else:
            st.warning("Please enter some text to get the embeddings.")

#Ask Anything page
if selected == "Ask Anything":
    st.title("Ask Me a Question")
    user_prompt = st.text_area(label="", placeholder="Ask Gemini-Pro...")
    if st.button("Get an Answer"):
        if user_prompt.strip():
            response = gemini_pro_response(user_prompt)
            st.markdown(response)
        else:
            st.warning("Please enter a question to get an answer.")