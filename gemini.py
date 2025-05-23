import os
from dotenv import load_dotenv
import google.generativeai as genai

# 1. Load your .env and grab the key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not found in .env")
genai.configure(api_key=api_key)

def generate_ai_content(prompt: str) -> str:
    """
    Ask Gemini 2.5 Flash (preview 05-20) for a short explanation.
    Returns the trimmed text response.
    """
    model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')
    instruction = f"Give a short explanation for: {prompt}"
    response = model.generate_content(instruction)
    return response.text.strip()
