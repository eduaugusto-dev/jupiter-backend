
from app.intents.classifier import classify_intent

from app.decision.vacation_decision import handle_vacation_request
from app.decision.salary_decision import handle_salary_request
from app.decision.benefits_decision import handle_benefits_request
from app.decision.time_clock_decision import handle_time_clock_request
from app.decision.time_bank_decision import handle_time_bank_request
from app.decision.leaves_decision import handle_leaves_request
from app.decision.thirteenth_salary_decision import handle_thirteenth_salary_request


def process_decision(message: str, user, client):
    intent = classify_intent(message)

    handlers = {
        "VIEW_OWN_VACATIONS": handle_vacation_request,
        "VIEW_OWN_SALARY": handle_salary_request,
        "VIEW_OWN_BENEFITS": handle_benefits_request,
        "VIEW_OWN_TIME_CLOCK": handle_time_clock_request,
        "VIEW_OWN_TIME_BANK": handle_time_bank_request,
        "VIEW_OWN_LEAVES": handle_leaves_request,
        "VIEW_OWN_THIRTEENTH_SALARY": handle_thirteenth_salary_request,
    }

    handler = handlers.get(intent)

    if handler is None:
        return None

    response = handler(client=client, user=user)

    return {
        "response": response,
        "intent": intent,
        "source": "decision_engine",
    }
