def get_employee(client, employee_id: str):
    result = (
        client.table("employees")
        .select("id, full_name, job_title, department")
        .eq("id", str(employee_id))
        .limit(1)
        .execute()
    )

    employee = result.data[0] if result.data else None

    if employee is None:
        return None

    return {
        "id": employee["id"],
        "nome": employee["full_name"],
        "cargo": employee["job_title"],
        "departamento": employee["department"],
    }