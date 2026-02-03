import requests
from app.services.llm.base import LLMProvider
from app.core.config import GROQ_API_KEY


class GroqLLM(LLMProvider):
    """
    Groq implementation of LLMProvider.
    """

    def generate(self, prompt: str) -> str:
        url = "https://api.groq.com/openai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(url, headers=headers, json=data)
        result = response.json()

         # DEBUG: print full response if error
        if "choices" not in result:
            print("Groq API Error:", result)
            return "Error from Groq API. Check API key or request."

    

        return result["choices"][0]["message"]["content"]
