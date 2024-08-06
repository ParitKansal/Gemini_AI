
# Gemini AI Streamlit App
### [Project Link](https://paritkansal121-gemini-ai.streamlit.app/)


## Project Description 
The Gemini AI Streamlit App is a web application designed to leverage the capabilities of Google Gemini's AI models for various functionalities including a chatbot, image captioning, text embedding, and general question answering. Built using Streamlit, this app provides an intuitive and interactive interface for users to engage with AI-powered features.

## Key Features

### Chatbot Interface
- Users can interact with the chatbot powered by the Gemini Pro model.
- Chat history is maintained, allowing users to view previous interactions.
- Users input messages and receive responses directly from the chatbot.

### Image Captioning
- Users can upload images, and the app generates a descriptive caption using the Gemini Pro Vision model.
- The image is resized for better display, and the generated caption is shown alongside it.

### Text Embedding
- Users can input text to receive its embeddings.
- The embeddings are generated using a dedicated embedding model, suitable for various NLP tasks.

### General Q&A
- Users can ask any question and get a response from the Gemini Pro model.
- This feature allows for versatile query handling and provides information based on user prompts.


## Dependencies

**Streamlit**: For building the web application interface.

**Pillow**: For image processing.

**Google Generative AI**: For accessing Gemini AI models and functionalities.

## File Structure
**main.py**: The main script that sets up the Streamlit app and manages different functionalities through a sidebar menu.

**gemini_utility.py**: Contains functions to interact with Google Gemini AI models, including loading models and generating responses.

**requirements.txt**: Lists the required Python packages for the project.

**config.json**: Stores the Google API key for authenticating API requests.

## Configuration
The API key for Google Gemini is stored in **config.json** and used to configure the Gemini API client.
## Installation and Setup

### Clone the Repository
- Clone the repository to your local machine.

### Install Dependencies
```bash
  pip install -r requirements.txt
```

### Set Up Configuration
- Ensure that config.json contains the correct Google API key.

### Run the App
```bash
streamlit run main.py
```
### Access the App
- Open the provided URL in your browser to interact with the app.

## Usage Instructions
- **Chatbot**: Navigate to the "Chatbot" page to start a conversation with the AI.
- **Image Captioning**: Go to the "Image Captioning" page, upload an image, and click "Generate Caption" to receive a description.
- **Embed Text**: On the "Embed Text" page, enter text to get its embeddings.
- **Ask Anything**: Use the "Ask Anything" page to pose general questions and receive answers from the AI.
