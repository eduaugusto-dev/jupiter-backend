from app.repositories.conversation_repository import (
    create_conversation,
    add_messages_to_conversation,
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
    return create_conversation(
        client=client,
        employee_id=employee_id,
        question=question,
        response=response,
    )


def continue_conversation(
    client,
    conversation_id: str,
    employee_id: str,
    question: str,
    response: str,
):
    return add_messages_to_conversation(
        client=client,
        conversation_id=conversation_id,
        employee_id=employee_id,
        question=question,
        response=response,
    )


def get_employee_conversation_history(
    client,
    employee_id: str,
):
    return get_conversations_by_employee(
        client=client,
        employee_id=employee_id,
    )


def get_conversation_history(
    client,
    employee_id: str,
):
    return get_all_conversations(
        client=client,
        employee_id=employee_id,
    )


def get_conversation_messages(
    client,
    conversation_id: str,
):
    return get_messages_by_conversation(
        client=client,
        conversation_id=conversation_id,
    )