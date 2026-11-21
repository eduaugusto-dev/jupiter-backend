
from app.agent.orchestrator import agent
from app.core.response_builder import build_chat_response


def chat(
    question: str,
    client,
    user,
):
    """
    Serviço principal de conversação do Júpiter.

    Executa consultas estruturadas ou RAG + LLM,
    sem persistir mensagens no Supabase durante o MVP.
    """

    result = agent.execute(
        question=question,
        user=user,
        client=client,
    )

    return build_chat_response(
        response=result["response"],
        intent=result["intent"],
        source=result["source"],
        conversation_id=None,
    )
