import os
import json
import google.generativeai as genai

# Get the working directory
working_directory = os.path.dirname(os.path.abspath(__file__))

# Define the config file path
config_file_path = os.path.join(working_directory, "config.json")

# Load the configuration data
with open(config_file_path, "r") as file:
    config_data = json.load(file)

# Get the API key from the configuration data
GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]

# Configure google.generativeai with the API key
genai.configure(api_key=GOOGLE_API_KEY)

#function to load gemini pro model
def load_gemini_pro_model():
    gemini_pro_model = genai.GenerativeModel("gemini-pro")
    return gemini_pro_model

#function to load image gemeni vision model
def gemini_pro_vision_response(prompt, image):
    gemini_pro_vision_model = genai.GenerativeModel("gemini-1.5-flash")
    response = gemini_pro_vision_model.generate_content([prompt, image])
    result = response.text
    return result


def embedding_model_response(input_text):
    embedding = genai.embed_content(model="models/text-embedding-004",
                                    content=input_text,
                                    task_type="retrieval_document")
    embedding_list = embedding["embedding"]
    return embedding_list


def gemini_pro_response(user_prompt):
    gemini_pro_model = genai.GenerativeModel("gemini-pro")
    response = gemini_pro_model.generate_content(user_prompt)
    result = response.text
    return result