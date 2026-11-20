
from app.tools.salary_tool import get_employee_salary


def handle_salary_request(
    client,
    user,
):
    """
    Processa a consulta salarial do colaborador autenticado.
    """

    salary = get_employee_salary(
        client=client,
        employee_id=user.employee_id,
    )

    if salary is None:
        return (
            "Não encontrei informações salariais "
            "cadastradas para você."
        )

    amount = salary.get("salary_amount")

    if amount is None:
        return (
            "Encontrei seu cadastro salarial, mas o valor "
            "não está preenchido."
        )

    salario_formatado = (
        f"R$ {float(amount):,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

    return f"""
Encontrei suas informações salariais:

Salário atual:
{salario_formatado}

Data de vigência:
{salary.get("effective_from")}
"""
