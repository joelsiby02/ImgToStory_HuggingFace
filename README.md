# Image to Story: Generative AI Project

## Overview

This project delves into the captivating world of Generative AI, leveraging Hugging Face's state-of-the-art pre-trained language models. The primary objective is to explore the nuances of these models while embarking on a fascinating journey to create short stories from simple images.

## Key Components

### 1. Learning Generative AI

The project serves as a platform to acquire skills in Generative AI. By utilizing Hugging Face's pre-trained language models, we aim to elevate our understanding and expertise in this exciting field.

### 2. Transforming Images into Stories

**Step 1: Image to Text**
- **Model:** Salesforce/blip-image-captioning-base
- **Task:** Convert images into descriptive text.
- **Rationale:** This model was chosen for its effectiveness in generating textual content based on visual input, providing a solid foundation for the subsequent storytelling step.

**Step 2: Story Generation from Text**
- **Model:** Meli/GPT2-Prompt
- **Task:** Generate short stories from textual prompts.
- **Rationale:** Utilizing the output from Step 1, this model crafts imaginative narratives, creating engaging and concise short stories.

### 3. Audio Narration for Lazy Readers

**Step 3: Text-to-Speech**
- **Model:** huggingface.co/models/espnet/kan-bayashi_ljspeech_vits
- **Task:** Convert generated stories into audio format.
- **Rationale:** Recognizing the need for convenience, this step enhances user experience by allowing them to listen to the generated stories, catering to those who prefer auditory content.

## Technology Stack

- **Framework:** Streamlit
- **Language Models Interaction:** Langchain
- **Output Visualization:** Streamlit Display

## Learning and Experimentation

The project incorporates the use of Streamlit, a powerful framework, to visualize and interact with the output of our language models. Langchain facilitates seamless communication with the pre-trained models, adding an element of fun and exploration to the learning process.


Follow if you want to run on your local machine

1. **Clone the Project:**
   Clone the project from the Git repository.

   ```bash
   git clone <repository-url>
   ```

2. **Install Requirements:**
   Navigate to the project directory and run the following command to install the required packages.

   ```bash
   pip install -r requirements.txt
   ```

3. **Create .env File:**
   Create a new file named `.env` in the project directory. Add the following line to the `.env` file:

   ```dotenv
   HUGGING_FACE_API_TOKEN=YourKeyFromHuggingFace
   ```

   Replace `YourKeyFromHuggingFace` with your actual Hugging Face API token.

4. **Run the App:**
   Open your code editor terminal and run the `app.py` file.

   ```bash
   python app.py
   ```

   It might take some time to set up.

5. **Start Streamlit:**
   In the terminal, type the following command to run the Streamlit app.

   ```bash
   streamlit run app.py
   ```

   If there are no errors, your default web browser should open, redirecting you to a local host.

6. **Upload Image:**
   On the Streamlit app, use the file uploader to insert an image.

7. **View Results:**
   The generated story and audio will be displayed below the image.


## Project Output

The output of our framework, showcasing the transformed stories, is displayed below. Dive into the world of AI-generated narratives and experience the creative synergy of image interpretation and storytelling.

[Output Displayed Below]

---

[Insert Output Display Here]
