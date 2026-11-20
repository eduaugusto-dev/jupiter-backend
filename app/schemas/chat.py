from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """
    Requisição enviada ao Júpiter.
    """
    message: str
    conversation_id: str | None = None


class ChatResponse(BaseModel):
    """
    Resposta padronizada do Júpiter.
    """
    response: str
    intent: str
    source: str
    conversation_id: str | None = None
    timestamp: datetime
    metadata: dict[str, Any] = Field(default_factory=dict)
