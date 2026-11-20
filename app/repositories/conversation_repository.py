from typing import Any


def create_conversation(
    client,
    employee_id: str,
    question: str,
    response: str,
):
    """
    Cria uma conversa no Supabase e registra
    a pergunta do colaborador e a resposta do Júpiter.
    """

    conversation_data = {
        "employee_id": str(employee_id),
        "title": question[:100],
        "status": "active",
    }

    try:
        conversation_result = (
            client.table("conversations")
            .insert(conversation_data)
            .execute()
        )

        conversations = conversation_result.data or []

        if not conversations:
            raise RuntimeError(
                "Não foi possível criar a conversa no Supabase."
            )

        conversation = conversations[0]
        conversation_id = conversation["id"]

        messages_data = [
            {
                "conversation_id": conversation_id,
                "role": "user",
                "content": question,
                "metadata": {},
            },
            {
                "conversation_id": conversation_id,
                "role": "assistant",
                "content": response,
                "metadata": {},
            },
        ]

        (
            client.table("messages")
            .insert(messages_data)
            .execute()
        )

        return conversation

    except Exception:
        raise


def get_conversations_by_employee(
    client,
    employee_id: str,
):
    """
    Retorna as conversas de um colaborador específico.

    A consulta também é protegida pelas políticas RLS
    do Supabase.
    """

    result = (
        client.table("conversations")
        .select("*")
        .eq("employee_id", str(employee_id))
        .order("created_at", desc=True)
        .execute()
    )

    return result.data or []


def get_all_conversations(
    client,
    employee_id: str,
):
    """
    Retorna conversas do colaborador autenticado.

    Não realiza consultas globais sem identificação
    de colaborador.
    """

    return get_conversations_by_employee(
        client=client,
        employee_id=employee_id,
    )
    
def get_messages_by_conversation(client, conversation_id: str):
    result = (
        client.table("messages")
        .select("*")
        .eq("conversation_id", str(conversation_id))
        .order("created_at", desc=False)
        .execute()
    )

    return result.data or []

