"""
Gemini LLM Engine for ScamGuard AI
Uses NEW Google GenAI SDK (google-genai)
Model: gemini-2.5-flash
"""

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

# Client automatically reads GEMINI_API_KEY from environment
client = genai.Client()


def llm_analyze(message: str) -> str:
    prompt = (
        "You are ScamGuard AI, an expert scam detection system.\n\n"
        "Analyze the following message and provide:\n"
        "1. Scam Type\n"
        "2. Risk Level (Low / Medium / High)\n"
        "3. Explanation\n"
        "4. Safe Action Advice\n\n"
        f"Message:\n{message}"
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()
