"""
-------------------------------------------------------
Interview Generator
-------------------------------------------------------
Purpose:
Communicates with Google Gemini AI.
-------------------------------------------------------
"""

from flask import current_app
from google import genai
import json


def generate_questions(prompt: str):

    api_key = current_app.config.get("GEMINI_API_KEY")

    client = genai.Client(
        api_key=api_key
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    # Remove markdown code fences if Gemini adds them
    if text.startswith("```json"):
        text = text.replace("```json", "", 1)

    if text.endswith("```"):
        text = text[:-3]

    return json.loads(text.strip())