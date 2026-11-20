from zoneinfo import ZoneInfo

from app.tools.time_clock_tool import get_employee_time_clock_records


def handle_time_clock_request(client, user):
    """
    Consulta e apresenta as marcações de ponto do colaborador
    autenticado referentes ao dia atual.
    """

    records = get_employee_time_clock_records(
        client=client,
        employee_id=user.employee_id
    )

    if not records:
        return "Não encontrei marcações de ponto registradas para você hoje."

    timezone = ZoneInfo("America/Sao_Paulo")

    record_labels = {
        "entry": "Entrada",
        "break_start": "Início do intervalo",
        "break_end": "Fim do intervalo",
        "exit": "Saída",
    }

    response = ["**Suas marcações de ponto de hoje:**\n"]

    for record in records:
        record_type = record.get("record_type", "")
        recorded_at = record.get("recorded_at")

        label = record_labels.get(record_type, record_type)

        if recorded_at:
            from datetime import datetime

            timestamp = datetime.fromisoformat(
                recorded_at.replace("Z", "+00:00")
            )

            timestamp = timestamp.astimezone(timezone)

            formatted_time = timestamp.strftime("%H:%M")

            response.append(f"• **{label}:** {formatted_time}")

        notes = record.get("notes")

        if notes:
            response.append(f"  Observação: {notes}")

    response.append(
        "\n\nSe precisar conferir alguma marcação, "
        "estou à disposição!"
    )

    return "\n".join(response)