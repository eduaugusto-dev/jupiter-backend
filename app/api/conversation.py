import logging

from fastapi import APIRouter, Depends, HTTPException

from app.dependencies.auth import (
    AuthenticatedUser,
    get_current_user,
    oauth2_scheme,
)

from app.database.supabase import create_user_supabase_client

from app.services.conversation_service import (
    get_conversation_history,
    get_employee_conversation_history,
    get_conversation_messages,
)

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"],
)


@router.get("")
def get_all_conversations(
    token: str = Depends(oauth2_scheme),
    user: AuthenticatedUser = Depends(get_current_user),
):
    """
    Retorna as conversas do funcionário autenticado.
    """

    try:
        client = create_user_supabase_client(token)

        return get_conversation_history(
            client=client,
            employee_id=user.employee_id,
        )

    except Exception:
        logger.exception("Erro ao buscar histórico de conversas")
        raise HTTPException(
            status_code=500,
            detail="Não foi possível buscar o histórico de conversas.",
        )


@router.get("/me")
def get_my_conversations(
    token: str = Depends(oauth2_scheme),
    user: AuthenticatedUser = Depends(get_current_user),
):
    """
    Retorna o histórico do funcionário autenticado.
    """

    try:
        client = create_user_supabase_client(token)

        return get_employee_conversation_history(
            client=client,
            employee_id=user.employee_id,
        )

    except Exception:
        logger.exception("Erro ao buscar histórico do funcionário")
        raise HTTPException(
            status_code=500,
            detail="Não foi possível buscar suas conversas.",
        )


@router.get("/{conversation_id}/messages")
def get_messages(
    conversation_id: str,
    token: str = Depends(oauth2_scheme),
    user: AuthenticatedUser = Depends(get_current_user),
):
    """
    Recupera as mensagens de uma conversa específica.
    Somente o proprietário da conversa pode acessá-la.
    """

    try:
        client = create_user_supabase_client(token)

        conversations = get_employee_conversation_history(
            client=client,
            employee_id=user.employee_id,
        )

        conversation_exists = any(
            str(conversation["id"]) == str(conversation_id)
            for conversation in conversations
        )

        if not conversation_exists:
            raise HTTPException(
                status_code=404,
                detail="Conversa não encontrada.",
            )

        return get_conversation_messages(
            client=client,
            conversation_id=conversation_id,
        )

    except HTTPException:
        raise

    except Exception:
        logger.exception("Erro ao buscar mensagens da conversa")
        raise HTTPException(
            status_code=500,
            detail="Não foi possível buscar as mensagens da conversa.",
        )