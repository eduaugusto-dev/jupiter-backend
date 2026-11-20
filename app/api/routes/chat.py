from datetime import datetime

from fastapi import APIRouter

from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
)


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post(
    "/",
    response_model=ChatResponse
)
def chat(
    request: ChatRequest
):
    """
    Endpoint principal do Júpiter.

    Futuramente:
    - Conversation Manager
    - Intent Classifier
    - Decision Engine
    - RAG
    - LLM
    """

    return ChatResponse(
        response=(
            "Olá, sou o Júpiter, agente inteligente de RH "
            "da SeguraOz. Como posso ajudar?"
        ),
        intent="GREETING",
        source="system",
        conversation_id=1,
        timestamp=datetime.now()
    )