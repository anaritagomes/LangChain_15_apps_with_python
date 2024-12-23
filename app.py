import streamlit as st
from langchain_openai import OpenAI

api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

def load_answer(question):
    llm = OpenAI(model_name="gpt-3.5-turbo-instruct",temperature=0)
    answer=llm.invoke(question)
    return answer

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

