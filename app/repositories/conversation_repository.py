from datetime import datetime, timezone


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


def add_messages_to_conversation(
    client,
    conversation_id: str,
    employee_id: str,
    question: str,
    response: str,
):
    """
    Adiciona mensagens a uma conversa existente.

    Verifica se a conversa pertence ao colaborador
    antes de registrar novas mensagens.
    """

    conversation_result = (
        client.table("conversations")
        .select("id")
        .eq("id", str(conversation_id))
        .eq("employee_id", str(employee_id))
        .limit(1)
        .execute()
    )

    conversations = conversation_result.data or []

    if not conversations:
        raise ValueError(
            "Conversa não encontrada ou não pertence ao colaborador."
        )

    messages_data = [
        {
            "conversation_id": str(conversation_id),
            "role": "user",
            "content": question,
            "metadata": {},
        },
        {
            "conversation_id": str(conversation_id),
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

    (
        client.table("conversations")
        .update({
            "updated_at": datetime.now(timezone.utc).isoformat()
        })
        .eq("id", str(conversation_id))
        .eq("employee_id", str(employee_id))
        .execute()
    )

    return conversations[0]


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
    """

    return get_conversations_by_employee(
        client=client,
        employee_id=employee_id,
    )


def get_messages_by_conversation(
    client,
    conversation_id: str,
):
    result = (
        client.table("messages")
        .select("*")
        .eq("conversation_id", str(conversation_id))
        .order("created_at", desc=False)
        .execute()
    )

    return result.data or []

