from app.tools.benefits_tool import get_employee_benefits


def handle_benefits_request(
    client,
    user,
):
    """
    Processa a consulta dos benefícios do colaborador autenticado.
    """

    benefits = get_employee_benefits(
        client=client,
        employee_id=user.employee_id,
    )

    if not benefits:
        return (
            "Não encontrei benefícios ativos e vigentes "
            "cadastrados para você no momento."
        )

    response = [
        "Encontrei seus benefícios ativos na SeguraOz:\n"
    ]

    for benefit in benefits:
        name = benefit.get("benefit_name", "Benefício")
        category = benefit.get("benefit_category")
        description = benefit.get("benefit_description")
        value = benefit.get("benefit_value")

        response.append(f"\n**{name}**")

        if category:
            response.append(f"Categoria: {category}")

        if value is not None:
            formatted_value = (
                f"R$ {float(value):,.2f}"
                .replace(",", "X")
                .replace(".", ",")
                .replace("X", ".")
            )
            response.append(f"Valor: {formatted_value}")

        if description:
            response.append(f"Descrição: {description}")

    response.append(
        "\n\nSe precisar de mais informações sobre algum "
        "benefício, estou à disposição!"
    )

    return "\n".join(response)