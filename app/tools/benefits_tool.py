from datetime import date


def get_employee_benefits(
    client,
    employee_id: str,
):
    """
    Busca os benefícios vigentes do colaborador autenticado
    no Supabase.
    Retorna uma lista de benefícios ou uma lista vazia.
    """

    today = date.today().isoformat()

    query = (
        client.table("employee_benefits")
        .select("*")
        .eq("employee_id", str(employee_id))
        .eq("status", "active")
        .lte("start_date", today)
        .or_(
            f"end_date.is.null,end_date.gte.{today}"
        )
        .order("benefit_name")
    )

    result = query.execute()

    return result.data or []