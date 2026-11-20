
from groq import Groq

from app.core.config import settings


client = Groq(
    api_key=settings.GROQ_API_KEY
)


def generate_response(prompt: str):
    """
    Envia prompt para o modelo configurado na Groq.
    """

    response = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
