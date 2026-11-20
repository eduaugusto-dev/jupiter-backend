
def get_employee_vacation(
    client,
    employee_id: str,
):
    """
    Busca saldo e solicitação de férias do colaborador
    autenticado no Supabase.
    """

    balance_result = (
        client.table("vacation_balances")
        .select("*")
        .eq("employee_id", str(employee_id))
        .order("created_at", desc=True)
        .limit(1)
        .execute()
    )

    balances = balance_result.data or []

    if not balances:
        return None

    balance = balances[0]

    request_result = (
        client.table("vacation_requests")
        .select("*")
        .eq("employee_id", str(employee_id))
        .order("request_date", desc=True)
        .limit(1)
        .execute()
    )

    requests = request_result.data or []
    request = requests[0] if requests else {}

    return {
        "periodo_aquisitivo_inicio": balance.get(
            "acquisition_period_start"
        ),
        "periodo_aquisitivo_fim": balance.get(
            "acquisition_period_end"
        ),
        "data_inicio": request.get("start_date"),
        "data_fim": request.get("end_date"),
        "quantidade_dias": request.get("requested_days")
            or balance.get("total_days"),
        "status": request.get("status")
            or balance.get("status"),
        "total_dias": balance.get("total_days"),
        "dias_utilizados": balance.get("used_days"),
        "dias_disponiveis": balance.get("available_days"),
        "solicitacao": request or None,
        "saldo": balance,
    }


def get_employee_vacations(
    client,
    employee_id: str,
):
    """
    Retorna todos os saldos de férias do colaborador.
    """

    result = (
        client.table("vacation_balances")
        .select("*")
        .eq("employee_id", str(employee_id))
        .order("created_at", desc=True)
        .execute()
    )

    return result.data or []
