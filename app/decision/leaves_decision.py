
from datetime import date, datetime


def handle_leaves_request(client, user):
    """
    Consulta as licenças e os afastamentos
    do funcionário autenticado.
    """

    employee_id = getattr(user, "employee_id", None)

    if not employee_id:
        return "Não foi possível identificar seu cadastro de funcionário."

    try:
        result = (
            client
            .table("employee_leaves")
            .select(
                "leave_type, start_date, end_date, "
                "days_count, status, notes"
            )
            .eq("employee_id", str(employee_id))
            .order("start_date", desc=True)
            .execute()
        )

        records = result.data or []

        if not records:
            return (
                "Não encontrei licenças ou afastamentos "
                "registrados para você."
            )

        responses = []

        leave_types = {
            "paternity": "Licença-paternidade",
            "maternity": "Licença-maternidade",
            "medical": "Licença médica",
        }

        statuses = {
            "approved": "Aprovada",
            "pending": "Pendente",
            "rejected": "Rejeitada",
            "cancelled": "Cancelada",
        }

        for record in records:
            leave_type = leave_types.get(
                record.get("leave_type"),
                record.get("leave_type", "Não informado")
            )

            status = statuses.get(
                record.get("status"),
                record.get("status", "Não informado")
            )

            start_date = date.fromisoformat(
                record["start_date"]
            ).strftime("%d/%m/%Y")

            end_date = date.fromisoformat(
                record["end_date"]
            ).strftime("%d/%m/%Y")

            days_count = record.get("days_count", 0)

            responses.append(
                f"{leave_type}\n"
                f"Período: {start_date} até {end_date}\n"
                f"Duração: {days_count} dias\n"
                f"Status: {status}"
            )

        return "Encontrei os seguintes registros de licença:\n\n" + (
            "\n\n".join(responses)
        )

    except Exception as e:
        print(f"[LEAVES_ERROR] {type(e).__name__}: {e}")

        return (
            "Não foi possível consultar suas licenças "
            "neste momento. Verifique o terminal da API."
        )
