import os 
import streamlit as st
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv 
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]


st.set_page_config(
    page_title= "Tariq's Blog Post Generator"
)

st.title("Tariq's Blog Post Generator")

openai_api_key = st.sidebar.text_input(
    label = "OpenAI API Key",
    type = "password") 


def generate_response(topic):
    llm = OpenAI(openai_api_key = openai_api_key)
    template = """
    As an experienced start-up and venture capitalist writer,
    generate a 400-word blog post about {topic}
    
    Your response whould be in this format:
    First, print the blog post.
    Then, sum the total number of words on it and print the results like this: This post has x words.
    """
    
    prompt = PromptTemplate(
        input_variables = ["topic"],
        template = template
    )
    query = prompt.format(topic=topic)
    response = llm(query, max_tokens=2048)
    return st.write(response)

topic_text = st.text_input("Enter topic: ")
if not openai_api_key.startswith("sk-"):
    st.warning("Enter Open AI Key")
if openai_api_key.startswith("sk-"):
    generate_response(topic_text)