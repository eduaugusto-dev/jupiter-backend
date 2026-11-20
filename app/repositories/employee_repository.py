
def get_employee_by_id(client, employee_id: str):
    """
    Busca colaborador pelo ID (UUID).
    """

    result = (
        client.table("employees")
        .select("*")
        .eq("id", str(employee_id))
        .limit(1)
        .execute()
    )

    return result.data[0] if result.data else None


def get_employee_by_matricula(client, matricula: str):
    """
    Busca colaborador pela matrícula.
    """

    result = (
        client.table("employees")
        .select("*")
        .eq("employee_code", matricula)
        .limit(1)
        .execute()
    )

    return result.data[0] if result.data else None


def get_all_employees(client):
    """
    Retorna todos os colaboradores autorizados pelo RLS,
    ordenados pelo nome.
    """

    result = (
        client.table("employees")
        .select("*")
        .order("full_name")
        .execute()
    )

    return result.data or []
