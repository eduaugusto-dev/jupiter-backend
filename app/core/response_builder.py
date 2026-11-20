from datetime import datetime, timezone
from typing import Any


def build_chat_response(
    *,
    response: str,
    intent: str,
    source: str,
    conversation_id: str | None = None,
    timestamp: datetime | None = None,
    metadata: dict[str, Any] | None = None,
) -> dict:
    """
    Padroniza todas as respostas retornadas pelo Júpiter.
    """

    return {
        "response": response,
        "intent": intent,
        "source": source,
        "conversation_id": conversation_id,
        "timestamp": timestamp or datetime.now(timezone.utc),
        "metadata": metadata or {},
    }