from app.repositories.conversation_repository import (
    create_conversation,
    get_conversations_by_employee,
    get_all_conversations,
    get_messages_by_conversation,
)


def save_conversation(
    client,
    employee_id: str,
    question: str,
    response: str,
):
    """
    Salva uma interação realizada com o Júpiter no Supabase.
    """

    return create_conversation(
        client=client,
        employee_id=employee_id,
        question=question,
        response=response,
    )


def get_employee_conversation_history(
    client,
    employee_id: str,
):
    """
    Recupera o histórico de conversas de um colaborador.
    """

    return get_conversations_by_employee(
        client=client,
        employee_id=employee_id,
    )


def get_conversation_history(
    client,
    employee_id: str,
):
    """
    Recupera as conversas do colaborador autenticado.
    """

    return get_all_conversations(
        client=client,
        employee_id=employee_id,
    )


def get_conversation_messages(
    client,
    conversation_id: str,
):
    """
    Recupera as mensagens de uma conversa específica,
    ordenadas cronologicamente.
    """

    return get_messages_by_conversation(
        client=client,
        conversation_id=conversation_id,
    )