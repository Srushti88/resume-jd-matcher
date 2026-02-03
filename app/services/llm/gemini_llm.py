import requests
from app.services.llm.base import LLMProvider
from app.core.config import GEMINI_API_KEY


class GeminiLLM(LLMProvider):
    """
    Gemini implementation of LLMProvider.
    """

    def generate(self, prompt: str) -> str:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }

        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        return result["candidates"][0]["content"]["parts"][0]["text"]
