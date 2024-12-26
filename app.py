import streamlit as st
from langchain.llms import HuggingFaceEndpoint
import os

api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")


def load_answer(question):
    if not question.strip():
        return "Please enter a question."
    llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2")  # Model link: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2
    answer = llm.invoke(question)
    return answer


# App UI starts here
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")


# Gets the user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text


user_input = get_text()
response = load_answer(user_input)

formatted_response = response.strip()  # Removes extra spaces or line breaks

submit = st.button('Generate')

# If generate button is clicked
if submit:
    st.subheader("Answer:")
    # Use st.text() with enough space to handle the large response
    st.text(formatted_response)  # This method ensures plain text formatting and does not cut off

    st.markdown(f"<div style='white-space: pre-wrap; word-wrap: break-word; width: 100%;'>{formatted_response}</div>",
                unsafe_allow_html=True)
