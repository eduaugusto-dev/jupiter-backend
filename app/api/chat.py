
import logging

from fastapi import APIRouter, Depends, HTTPException

from app.dependencies.auth import (
    AuthenticatedUser,
    get_current_user,
    oauth2_scheme,
)

from app.database.supabase import create_user_supabase_client

from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
)

from app.llm.chat_service import chat


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("", response_model=ChatResponse)
def chat_endpoint(
    request: ChatRequest,
    token: str = Depends(oauth2_scheme),
    user: AuthenticatedUser = Depends(get_current_user),
):
    """
    Endpoint principal do Júpiter.

    Autenticação via Supabase JWT.
    Consultas estruturadas via Supabase.
    RAG + LLM para conhecimento corporativo.
    """

    try:
        client = create_user_supabase_client(token)

        result = chat(
            question=request.message,
            client=client,
            user=user,
            conversation_id=request.conversation_id,
        )

        return result

    except HTTPException:
        raise

    except Exception:
        logger.exception("Erro ao processar mensagem no Júpiter")

        raise HTTPException(
            status_code=500,
            detail="Não foi possível processar sua mensagem.",
        )
