import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash-lite")

def generate_state_report(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text

