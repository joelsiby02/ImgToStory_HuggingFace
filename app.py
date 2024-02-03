from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
import os
import requests
from io import BytesIO
import streamlit as st
import base64
from PIL import Image


# Load environment variables from .env file
load_dotenv(find_dotenv())

# Image2Text using Salesforce blip model
def img2text(image):
    image_to_text = pipeline("image-to-text", model='Salesforce/blip-image-captioning-base')
    
    # Convert PIL image to bytes
    img_bytes = BytesIO()
    image.save(img_bytes, format="JPEG")
    img_bytes = img_bytes.getvalue()

    # Convert image bytes to base64 string
    base64_image = base64.b64encode(img_bytes).decode("utf-8")

    # If the model accepts raw image bytes, provide the image directly
    result = image_to_text(base64_image)[0]
    text = result['generated_text']
    return text, result

# Input from the previous model text to story

def generate_story(scenario):
    # Remove `max_new_tokens` to use only `max_length`
    story_pipe = pipeline("text-generation", model="Meli/GPT2-Prompt", max_length=200) 
    
    # Provide the scenario directly to generate the story
    generated_text = story_pipe(scenario)[0]['generated_text'].strip()  # Remove leading/trailing whitespaces
    
    # Define tokens to be removed
    tokens_to_remove = ["[newline]", "[endprompt]"]
    
    # Remove specified tokens
    for token in tokens_to_remove:
        generated_text = generated_text.replace(token, "")
    
    return generated_text.strip()

# Example scenario: "Say something about the sentence or describe the moment."
scenario = "make a short happy story challenge"
generated_story = generate_story(scenario)

print("Generated Story:")
print(generated_story)



# Previous generated story to audio generation
def text_to_speech(msg):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {os.getenv('HUGGING_FACE_API_TOKEN')}"}  # Use the environment variable
    payload = {
        "inputs": msg
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        content_type = response.headers['content-type']
        if 'audio' in content_type:
            with open('audio.flac', 'wb') as file:
                file.write(response.content)
            print("Audio file saved successfully.")
        else:
            print("Error: No audio content found in the API response.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def main():
    st.set_page_config(page_title='Image to Story App', page_icon='😁')
    st.header("Turn your image into a short Story")
    
    uploaded_file = st.file_uploader("Choose an image..", type=['jpg', 'jpeg'])
    
    if uploaded_file is not None:
        bytes_data = uploaded_file.read()  # Use read() instead of getvalue()
        with open(uploaded_file.name, 'wb') as file:
            file.write(bytes_data)
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        scenario, _ = img2text(Image.open(uploaded_file))
        story = generate_story(scenario)
        text_to_speech(story)
        
        with st.expander("Scenario"):
            st.write(scenario)
        with st.expander("Story"):
            st.write(story)
        
        st.audio("audio.flac")

if __name__ == '__main__':
    main()
