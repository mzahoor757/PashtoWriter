from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os
import time
import streamlit as st

load_dotenv()
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")

secret_key = st.secret.get("OPEN_AI_KEY", "")

openai_model = ChatOpenAI(api_key=secret_key, model_name="gpt-4o")

sysMessage = """
    You are a Native Pashto Speaker who converts Roman Pashto into proper Pashto text.

    You will be given a Roman Pashto text and you will have to convert it into proper Pashto text.
"""

def roman_to_pashto(text, max_retries=3, delay=2):
    prompt = f"""
    Convert the following Roman Pashto text to Proper Pashto. 
    ONLY return the converted text. Do NOT provide explanations or additional information.
    
    Roman Pashto: {text}
    Proper Pashto:
    """.strip()
    
    for _ in range(max_retries):
        try:
            response = openai_model.invoke([
                SystemMessage(content="You are a Roman Pashto to Proper Pashto converter."),
                HumanMessage(content=prompt)
            ])
            return response.content  # Successful response
        except Exception as e:
            print(f"Error: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)  # Wait before retrying
            delay *= 2  # Exponential backoff
    
    return "⚠️ Error: Service unavailable. Try again later."