
from datetime import datetime
from typing import Any

from pydantic import BaseModel


class ChatRequest(BaseModel):
    """
    Requisição enviada ao Júpiter.
    """
    message: str


class ChatResponse(BaseModel):
    """
    Resposta padronizada do Júpiter.
    """
    response: str
    intent: str
    source: str
    conversation_id: str | None = None
    timestamp: datetime
    metadata: dict[str, Any] = {}
