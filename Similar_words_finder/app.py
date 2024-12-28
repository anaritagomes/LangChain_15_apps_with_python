import streamlit as st
import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.document_loaders.csv_loader import CSVLoader
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set Streamlit page configuration
st.set_page_config(page_title="Educate Kids", page_icon=":robot:")
st.header("Hey, Ask me something & I will give out similar things")

# Initialize OpenAIEmbeddings
try:
    embeddings = OpenAIEmbeddings()
except Exception as e:
    st.error(f"Failed to initialize OpenAIEmbeddings: {e}")
    st.stop()

# Load CSV file
csv_path = "myData.csv"  # Ensure this file exists in the same directory
if not os.path.exists(csv_path):
    st.error(f"File not found: {csv_path}")
    st.stop()

try:
    loader = CSVLoader(
        file_path=csv_path,
        csv_args={"delimiter": ",", "quotechar": '"', "fieldnames": ["Words"]},
    )
    data = loader.load()
except Exception as e:
    st.error(f"Failed to load data from CSV: {e}")
    st.stop()

# Display loaded data
# st.write("Loaded data from CSV:", data)

# Create FAISS database
try:
    db = FAISS.from_documents(data, embeddings)
except Exception as e:
    st.error(f"Failed to initialize FAISS database: {e}")
    st.stop()


# Function to receive user input
def get_text():
    input_text = st.text_input("You: ", key="user_input")
    return input_text


user_input = get_text()
submit = st.button("Find Similar Things")

if submit:
    if not user_input:
        st.warning("Please enter a query.")
    else:
        try:
            # Perform similarity search
            docs = db.similarity_search(user_input, k=2)  # Limit results to top 2
            st.subheader("Top Matches:")
            for idx, doc in enumerate(docs):
                st.text(f"Match {idx + 1}: {doc.page_content}")
        except Exception as e:
            st.error(f"Failed to fetch similar things: {e}")
