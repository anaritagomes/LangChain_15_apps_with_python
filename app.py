import streamlit as st
from langchain.llms import HuggingFaceEndpoint
import os 

api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2") # Model link : https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

# The LLM takes a prompt as an input and outputs a completion
our_query = "What is the current president of the USA?"

#Last week langchain has recommended to use invoke function for the below please :)
completion = llm.invoke(our_query)
print(completion)


#App UI starts here
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")

#Gets the user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text


user_input=get_text()
response = load_answer(user_input)

submit = st.button('Generate')  

#If generate button is clicked
if submit:

    st.subheader("Answer:")

    st.write(response)
