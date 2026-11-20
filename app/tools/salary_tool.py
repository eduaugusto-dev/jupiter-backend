
from datetime import date


def get_employee_salary(
    client,
    employee_id: str,
):
    """
    Busca o salário vigente do colaborador no Supabase.
    Retorna o registro mais recente vigente ou None.
    """

    today = date.today().isoformat()

    query = (
        client.table("employee_salaries")
        .select("*")
        .eq("employee_id", str(employee_id))
        .lte("effective_from", today)
        .or_(
            f"effective_until.is.null,effective_until.gte.{today}"
        )
        .order("effective_from", desc=True)
        .limit(1)
    )

    result = query.execute()
    records = result.data or []

    return records[0] if records else None
