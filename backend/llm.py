# backend/llm.py

from groq import Groq
from backend.core.config import settings
from backend.core.logger import logger


client = Groq(api_key=settings.GROQ_API_KEY)


def generate_response(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model=settings.MODEL_NAME,  # Make sure model is valid
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        logger.error(f"LLM error: {e}")
        raise e
