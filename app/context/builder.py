from app.context.schemas import AgentContext



def build_context(
    user,
    intent,
    action,
    data=None,
    knowledge=None
):

    return AgentContext(

        user_id=user.id,

        user_name=user.employee.nome
            if user.employee
            else user.email,

        role=str(user.role),

        intent=intent,

        action=str(action),

        data=data,

        knowledge=knowledge,

    )