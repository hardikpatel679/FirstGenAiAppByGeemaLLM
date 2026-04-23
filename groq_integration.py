import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage 
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# langsmith Tracking 
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

groq_api_key = os.getenv("GROQ_API_KEY")

st.title("Groq Integration")

input_text = st.text_input("What is in your mind?")

str_output_parser = StrOutputParser()


groq_gemma2_llm = ChatGroq(model="llama-3.1-8b-instant", api_key=groq_api_key)
messages = [
    SystemMessage(content="you are ai agent, help with the question:+{input_text}"),
    HumanMessage(content="{input_text}")
]


chain = groq_gemma2_llm | str_output_parser

if input_text:
    for message in messages:
        message.content = message.content.format(input_text=input_text)
    response = chain.invoke(messages)
    st.write(response)