from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies.auth import (
    AuthenticatedUser,
    get_current_user,
    oauth2_scheme,
)
from app.database.supabase import create_user_supabase_client


router = APIRouter(
    prefix="/vacations",
    tags=["Vacations"],
)


def _is_hr_or_admin(user: AuthenticatedUser) -> bool:
    return user.role in {"RH", "ADMIN"}


def _get_client(token: str):
    try:
        return create_user_supabase_client(token)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Não foi possível conectar ao Supabase.",
        )


def _execute_query(query):
    try:
        result = query.execute()
        return result.data or []
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Não foi possível consultar os dados de férias no Supabase.",
        )


# ==========================================
# SOLICITAÇÕES DE FÉRIAS
# ==========================================

@router.get("/")
def get_vacations(
    token: str = Depends(oauth2_scheme),
    current_user: AuthenticatedUser = Depends(get_current_user),
):
    """Lista solicitações de férias conforme as permissões do usuário."""

    client = _get_client(token)

    query = client.table("vacation_requests").select("*")

    if not _is_hr_or_admin(current_user):
        query = query.eq("employee_id", current_user.employee_id)

    return _execute_query(query)


@router.get("/employee/{employee_id}")
def get_employee_vacations(
    employee_id: UUID,
    token: str = Depends(oauth2_scheme),
    current_user: AuthenticatedUser = Depends(get_current_user),
):
    """Lista solicitações de férias de um colaborador."""

    if (
        not _is_hr_or_admin(current_user)
        and str(employee_id) != current_user.employee_id
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não tem permissão para consultar as férias deste colaborador.",
        )

    client = _get_client(token)

    query = (
        client.table("vacation_requests")
        .select("*")
        .eq("employee_id", str(employee_id))
    )

    return _execute_query(query)


# ==========================================
# SALDOS DE FÉRIAS
# ==========================================

@router.get("/balances")
def get_vacation_balances(
    token: str = Depends(oauth2_scheme),
    current_user: AuthenticatedUser = Depends(get_current_user),
):
    """Lista saldos de férias conforme as permissões do usuário."""

    client = _get_client(token)

    query = client.table("vacation_balances").select("*")

    if not _is_hr_or_admin(current_user):
        query = query.eq("employee_id", current_user.employee_id)

    return _execute_query(query)


@router.get("/balances/employee/{employee_id}")
def get_employee_vacation_balances(
    employee_id: UUID,
    token: str = Depends(oauth2_scheme),
    current_user: AuthenticatedUser = Depends(get_current_user),
):
    """Consulta os saldos de férias de um colaborador."""

    if (
        not _is_hr_or_admin(current_user)
        and str(employee_id) != current_user.employee_id
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não tem permissão para consultar o saldo deste colaborador.",
        )

    client = _get_client(token)

    query = (
        client.table("vacation_balances")
        .select("*")
        .eq("employee_id", str(employee_id))
    )

    return _execute_query(query)


@router.get("/balances/{balance_id}")
def get_vacation_balance(
    balance_id: UUID,
    token: str = Depends(oauth2_scheme),
    current_user: AuthenticatedUser = Depends(get_current_user),
):
    """Busca um registro de saldo de férias pelo UUID."""

    client = _get_client(token)

    query = (
        client.table("vacation_balances")
        .select("*")
        .eq("id", str(balance_id))
    )

    rows = _execute_query(query)

    if not rows:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Saldo de férias não encontrado.",
        )

    return rows[0]


# ==========================================
# BUSCA DE SOLICITAÇÃO POR UUID
# Manter esta rota dinâmica por último.
# ==========================================

@router.get("/{vacation_id}")
def get_vacation(
    vacation_id: UUID,
    token: str = Depends(oauth2_scheme),
    current_user: AuthenticatedUser = Depends(get_current_user),
):
    """Busca uma solicitação de férias pelo UUID."""

    client = _get_client(token)

    query = (
        client.table("vacation_requests")
        .select("*")
        .eq("id", str(vacation_id))
    )

    rows = _execute_query(query)

    if not rows:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Solicitação de férias não encontrada.",
        )

    return rows[0]
