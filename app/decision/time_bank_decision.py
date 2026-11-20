
from datetime import date


def handle_time_bank_request(client, user):
    """
    Consulta o saldo de banco de horas do funcionário autenticado.
    """

    employee_id = getattr(user, "employee_id", None)

    if not employee_id:
        return "Não foi possível identificar seu cadastro de funcionário."

    current_month = date.today().replace(day=1).isoformat()

    try:
        result = (
            client
            .table("employee_time_banks")
            .select("reference_month, balance_minutes, notes")
            .eq("employee_id", str(employee_id))
            .eq("reference_month", current_month)
            .limit(1)
            .execute()
        )

        records = result.data or []

        if not records:
            return (
                "Não encontrei um registro de banco de horas "
                "para você no mês atual."
            )

        record = records[0]
        balance_minutes = int(record.get("balance_minutes", 0))

        sign = "+" if balance_minutes >= 0 else "-"
        absolute_minutes = abs(balance_minutes)

        hours = absolute_minutes // 60
        minutes = absolute_minutes % 60

        formatted_balance = (
            f"{sign}{hours:02d}h{minutes:02d}min"
        )

        reference_month = record.get("reference_month", current_month)

        month_label = date.fromisoformat(
            reference_month
        ).strftime("%m/%Y")

        if balance_minutes > 0:
            situation = "Você possui horas positivas."
        elif balance_minutes < 0:
            situation = "Você possui horas negativas."
        else:
            situation = "Seu banco de horas está zerado."

        return (
            f"Seu saldo de banco de horas referente a {month_label} "
            f"é de {formatted_balance}. {situation}"
        )

    except Exception as e:
        print(f"[TIME_BANK_ERROR] {type(e).__name__}: {e}")

        return (
            "Não foi possível consultar seu banco de horas neste momento. "
            "Verifique o terminal da API para identificar o erro."
        )