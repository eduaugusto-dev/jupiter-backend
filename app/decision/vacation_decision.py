
from app.tools.vacation_tool import get_employee_vacation


def handle_vacation_request(
    client,
    user,
):
    """
    Processa solicitações relacionadas às férias
    do colaborador autenticado.
    """

    vacation = get_employee_vacation(
        client=client,
        employee_id=user.employee_id,
    )

    if vacation is None:
        return (
            "Não encontrei informações "
            "de férias cadastradas."
        )

    return f"""
Encontrei suas informações de férias:

Período aquisitivo:
{vacation.get("periodo_aquisitivo_inicio")}
até
{vacation.get("periodo_aquisitivo_fim")}

Período de férias:
{vacation.get("data_inicio")}
até
{vacation.get("data_fim")}

Quantidade de dias:
{vacation.get("quantidade_dias")}

Status:
{vacation.get("status")}
"""
