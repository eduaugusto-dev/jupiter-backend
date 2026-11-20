from datetime import date
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.dependencies.auth import AuthenticatedUser, get_current_user, oauth2_scheme
from app.database.supabase import create_user_supabase_client


router = APIRouter(
    prefix="/payroll",
    tags=["Payroll"],
)


def _get_client(token: str):
    try:
        return create_user_supabase_client(token)
    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Não foi possível conectar ao Supabase.",
        )


def _execute_query(query):
    try:
        result = query.execute()
        return result.data or []
    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Não foi possível consultar os dados da folha de pagamento no Supabase.",
        )


# =========================================================
# SALÁRIO DO COLABORADOR AUTENTICADO
# =========================================================

@router.get("/salary")
def get_my_salary(
    token: str = Depends(oauth2_scheme),
    user: AuthenticatedUser = Depends(get_current_user),
):
    """
    Retorna o salário vigente do colaborador autenticado.
    """

    client = _get_client(token)
    today = date.today().isoformat()

    query = (
        client.table("employee_salaries")
        .select("*")
        .eq("employee_id", user.employee_id)
        .lte("effective_from", today)
        .or_(f"effective_until.is.null,effective_until.gte.{today}")
        .order("effective_from", desc=True)
        .limit(1)
    )

    records = _execute_query(query)

    if not records:
        raise HTTPException(
            status_code=404,
            detail="Salário vigente não encontrado.",
        )

    return records[0]


# =========================================================
# REGISTROS DE PAGAMENTO DO COLABORADOR
# =========================================================

@router.get("/records")
def get_my_payroll_records(
    token: str = Depends(oauth2_scheme),
    user: AuthenticatedUser = Depends(get_current_user),
):
    """
    Lista os registros de folha do colaborador autenticado.
    """

    client = _get_client(token)

    query = (
        client.table("payroll_records")
        .select("*")
        .eq("employee_id", user.employee_id)
        .order("reference_month", desc=True)
    )

    return _execute_query(query)


# =========================================================
# FOLHA DE UM MÊS ESPECÍFICO
# =========================================================

@router.get("/records/month/{reference_month}")
def get_my_payroll_by_month(
    reference_month: str,
    token: str = Depends(oauth2_scheme),
    user: AuthenticatedUser = Depends(get_current_user),
):
    """
    Consulta a folha do colaborador em determinado mês.
    Formato esperado: YYYY-MM (ex.: 2026-10).
    """

    try:
        year, month = map(int, reference_month.split("-"))

        if len(reference_month) != 7 or not (1 <= month <= 12):
            raise ValueError

        start_date = date(year, month, 1)

        if month == 12:
            next_month = date(year + 1, 1, 1)
        else:
            next_month = date(year, month + 1, 1)

    except (ValueError, TypeError):
        raise HTTPException(
            status_code=400,
            detail="Mês inválido. Utilize o formato YYYY-MM.",
        )

    client = _get_client(token)

    query = (
        client.table("payroll_records")
        .select("*")
        .eq("employee_id", user.employee_id)
        .gte("reference_month", start_date.isoformat())
        .lt("reference_month", next_month.isoformat())
    )

    records = _execute_query(query)

    if not records:
        raise HTTPException(
            status_code=404,
            detail="Registro de folha não encontrado para o mês informado.",
        )

    return records


# =========================================================
# REGISTRO INDIVIDUAL DE FOLHA
# =========================================================

@router.get("/records/{record_id}")
def get_my_payroll_record(
    record_id: UUID,
    token: str = Depends(oauth2_scheme),
    user: AuthenticatedUser = Depends(get_current_user),
):
    """
    Consulta um registro específico de folha.
    O RLS limita a visualização aos registros autorizados.
    """

    client = _get_client(token)

    query = (
        client.table("payroll_records")
        .select("*")
        .eq("id", str(record_id))
        .eq("employee_id", user.employee_id)
        .limit(1)
    )

    records = _execute_query(query)

    if not records:
        raise HTTPException(
            status_code=404,
            detail="Registro de folha não encontrado.",
        )

    return records[0]