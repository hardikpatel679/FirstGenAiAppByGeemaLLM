from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
groq_gemma2_llm = ChatGroq(model="llama-3.1-8b-instant", api_key=groq_api_key)


system_template = "Translate the following English text to {language}."
prompt = ChatPromptTemplate.from_messages([
    ("system",system_template),
    ("user","{text}")
])

parser = StrOutputParser()

chain = prompt| groq_gemma2_llm | parser

# Add routes to the app
app = FastAPI(title="Langchain server",
              version="0.1",
              description="A simple api server to test langchain runnable interfaces")

#adding translate route to the app

add_routes(
    app = app,
    runnable = chain,
    path= "/translate")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
    