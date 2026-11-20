
from app.repositories.employee_repository import (
    get_employee_by_id,
    get_employee_by_matricula,
    get_all_employees,
)


def find_employee_by_id(client, employee_id: str):
    """
    Busca colaborador pelo ID (UUID).
    """

    return get_employee_by_id(
        client=client,
        employee_id=employee_id,
    )


def find_employee_by_matricula(client, matricula: str):
    """
    Busca colaborador pela matrícula.
    """

    return get_employee_by_matricula(
        client=client,
        matricula=matricula,
    )


def list_employees(client):
    """
    Lista os colaboradores autorizados pelo RLS.
    """

    return get_all_employees(client=client)
