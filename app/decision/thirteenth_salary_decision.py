
from datetime import date
from decimal import Decimal


def handle_thirteenth_salary_request(client, user):
    """
    Consulta o registro do 13º salário do funcionário
    autenticado no Supabase.
    """

    employee_id = getattr(user, "employee_id", None)

    if not employee_id:
        return "Não foi possível identificar seu cadastro de funcionário."

    current_year = date.today().year
    reference_month = f"{current_year}-12-01"

    try:
        result = (
            client
            .table("payroll_records")
            .select(
                "reference_month, payment_date, gross_amount, "
                "total_additions, total_deductions, net_amount, "
                "status, notes"
            )
            .eq("employee_id", str(employee_id))
            .eq("reference_month", reference_month)
            .limit(1)
            .execute()
        )

        records = result.data or []

        if not records:
            return (
                f"Não encontrei um registro de 13º salário "
                f"para você referente a {current_year}."
            )

        record = records[0]

        amount = Decimal(str(record.get("net_amount") or "0"))

        formatted_amount = (
            f"R$ {amount:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

        status_map = {
            "pending": "Pendente",
            "paid": "Pago",
            "completed": "Pago",
            "processing": "Em processamento",
            "cancelled": "Cancelado",
        }

        status = status_map.get(
            record.get("status"),
            record.get("status", "Não informado")
        )

        payment_date = record.get("payment_date")

        if payment_date:
            payment_date = date.fromisoformat(
                payment_date
            ).strftime("%d/%m/%Y")

            payment_info = f"Data de pagamento: {payment_date}"
        else:
            payment_info = (
                "Data de pagamento ainda não informada."
            )

        return (
            f"Seu 13º salário referente a {current_year} "
            f"está registrado no valor de {formatted_amount}. "
            f"Status do pagamento: {status}. "
            f"{payment_info}"
        )

    except Exception as e:
        print(
            f"[THIRTEENTH_SALARY_ERROR] "
            f"{type(e).__name__}: {e}"
        )

        return (
            "Não foi possível consultar seu 13º salário "
            "neste momento. Verifique o terminal da API."
        )
