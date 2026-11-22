
from app.agent.orchestrator import agent
from app.core.response_builder import build_chat_response
from app.services.conversation_service import (
    save_conversation,
    continue_conversation,
)


def chat(
    question: str,
    client,
    user,
    conversation_id: str | None = None,
):
    result = agent.execute(
        question=question,
        user=user,
        client=client,
    )

    employee_id = user.employee_id

    if conversation_id:
        conversation = continue_conversation(
            client=client,
            conversation_id=conversation_id,
            employee_id=employee_id,
            question=question,
            response=result["response"],
        )
    else:
        conversation = save_conversation(
            client=client,
            employee_id=employee_id,
            question=question,
            response=result["response"],
        )

    return build_chat_response(
        response=result["response"],
        intent=result["intent"],
        source=result["source"],
        conversation_id=str(conversation["id"]),
    )
