import os
from dotenv import load_dotenv
import streamlit as st
from langsmith import traceable
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

# langsmith Tracking 
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user","Question:{question}"),
])


st.title("This is my langchain demo with gemma LLM")
input_text = st.text_input("What is in your mind?")


llm = Ollama(model="gemma:2b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser


if input_text:
    response = llm.invoke(prompt.format_messages(question=input_text))
    st.write(response)