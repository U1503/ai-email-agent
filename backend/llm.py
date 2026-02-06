import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

def get_llm():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found in .env file")

    return ChatGroq(
        model="llama-3.1-8b-instant",   # Free fast model
        temperature=0,
        api_key=api_key
    )
