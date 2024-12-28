import streamlit as st
from langchain.llms import HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from huggingface_hub import login

# Load environment variables from the .env file
load_dotenv()

# Get the Hugging Face access token from the environment variable
hf_token = os.getenv('HF_HOME')

# Check if the token is loaded properly
if hf_token:
    print("Token successfully loaded.")
    login(token=hf_token)
else:
    st.error("Hugging Face token is not set or invalid.")

def load_answer(question):
    if not question.strip():
        return "Please enter a question."

    try:
        # Initialize the HuggingFaceEndpoint with the correct repo_id
        llm = HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.2")
        temperature = 0.7  # Lower values make responses more deterministic

        # Use __call__ method for invoking the model
        answer = llm(question)  # You can also pass additional parameters like temperature, etc.
        return answer.strip()  # Clean any extra spaces or line breaks
    except Exception as e:
        return f"An error occurred while getting the answer: {e}"

# App UI starts here
st.set_page_config(page_title="Simple LangChain Q&A App", page_icon=":robot:")
st.header("Simple LangChain Q&A App")

# Get user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text

# Get the user input text
user_input = get_text()

# Only generate answer when the button is pressed
submit = st.button('Generate')

if submit:
    if not user_input.strip():
        st.warning("Please enter a question.")
    else:
        response = load_answer(user_input)

        st.subheader("Answer:")
        # Ensure the response is formatted correctly for multiline output
        st.markdown(f"<div style='white-space: pre-wrap; word-wrap: break-word; width: 100%;'>{response}</div>", unsafe_allow_html=True)
