
from app.agent.orchestrator import agent
from app.core.response_builder import build_chat_response
from app.services.conversation_service import save_conversation


def chat(
    question: str,
    client,
    user,
):
    """
    Serviço principal de conversação do Júpiter.

    Executa o agente utilizando o Supabase
    e salva a interação do colaborador.
    """

    result = agent.execute(
        question=question,
        user=user,
        client=client,
    )

    conversation = save_conversation(
        client=client,
        employee_id=user.employee_id,
        question=question,
        response=result["response"],
    )

    return build_chat_response(
        response=result["response"],
        intent=result["intent"],
        source=result["source"],
        conversation_id=conversation.get("id"),
        timestamp=None,
    )