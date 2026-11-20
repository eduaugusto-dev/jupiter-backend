from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo


def get_employee_time_clock_records(client, employee_id: str):
    """
    Busca as marcações de ponto do colaborador autenticado
    referentes ao dia atual.

    Utiliza o fuso horário de São Paulo e retorna os registros
    em ordem cronológica.
    """

    timezone = ZoneInfo("America/Sao_Paulo")
    today = datetime.now(timezone).date()

    start_of_day = datetime.combine(
        today,
        time.min,
        tzinfo=timezone
    )

    end_of_day = start_of_day + timedelta(days=1)

    query = (
        client.table("time_clock_records")
        .select("*")
        .eq("employee_id", str(employee_id))
        .gte("recorded_at", start_of_day.isoformat())
        .lt("recorded_at", end_of_day.isoformat())
        .order("recorded_at")
    )

    result = query.execute()

    return result.data or []