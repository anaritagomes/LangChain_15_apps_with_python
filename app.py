import streamlit as st
from langchain.llms import HuggingFaceEndpoint

api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2") # Model link : https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

# The LLM takes a prompt as an input and outputs a completion
our_query = "What is the current president of the USA?"

#Last week langchain has recommended to use invoke function for the below please :)
completion = llm.invoke(our_query)
