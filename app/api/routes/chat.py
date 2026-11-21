
from fastapi import APIRouter, Depends, HTTPException

from app.dependencies.auth import (
    AuthenticatedUser,
    get_current_user,
    oauth2_scheme,
)
from app.database.supabase import create_user_supabase_client
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import chat as chat_service


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "/",
    response_model=ChatResponse,
)
def chat(
    request: ChatRequest,
    token: str = Depends(oauth2_scheme),
    user: AuthenticatedUser = Depends(get_current_user),
):
    """
    Endpoint principal do Júpiter.

    Autentica o colaborador e executa o agente
    sem persistir conversas ou mensagens no MVP.
    """
    try:
        client = create_user_supabase_client(token)

        result = chat_service(
            question=request.message,
            client=client,
            user=user,
        )

        return ChatResponse(**result)

    except HTTPException:
        raise

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Não foi possível processar sua mensagem.",
        )
