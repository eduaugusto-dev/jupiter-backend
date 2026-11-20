
import logging
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.dependencies.auth import (
    AuthenticatedUser,
    get_current_user,
    oauth2_scheme,
)

from app.database.supabase import create_user_supabase_client

from app.services.employee_service import (
    find_employee_by_id,
    find_employee_by_matricula,
    list_employees,
)


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
)


def is_hr_or_admin(user: AuthenticatedUser) -> bool:
    """
    Verifica se o usuário possui perfil de RH ou Admin.
    """
    role = (user.role or "").strip().upper()
    return role in {"RH", "ADMIN"}


@router.get("/")
def get_employees(
    token: str = Depends(oauth2_scheme),
    user: AuthenticatedUser = Depends(get_current_user),
):
    """
    Lista todos os colaboradores.
    Acesso permitido somente para RH e Admin.
    """

    if not is_hr_or_admin(user):
        raise HTTPException(
            status_code=403,
            detail="Você não tem permissão para listar colaboradores.",
        )

    try:
        client = create_user_supabase_client(token)

        return list_employees(client=client)

    except HTTPException:
        raise

    except Exception:
        logger.exception("Erro ao listar colaboradores")

        raise HTTPException(
            status_code=500,
            detail="Não foi possível listar os colaboradores.",
        )


@router.get("/{employee_id}")
def get_employee(
    employee_id: UUID,
    token: str = Depends(oauth2_scheme),
    user: AuthenticatedUser = Depends(get_current_user),
):
    """
    Busca colaborador pelo ID.
    O próprio colaborador ou RH/Admin podem consultar.
    """

    is_own_profile = str(employee_id) == str(user.employee_id)

    if not is_own_profile and not is_hr_or_admin(user):
        raise HTTPException(
            status_code=403,
            detail="Você não tem permissão para consultar este colaborador.",
        )

    try:
        client = create_user_supabase_client(token)

        employee = find_employee_by_id(
            client=client,
            employee_id=str(employee_id),
        )

        if employee is None:
            raise HTTPException(
                status_code=404,
                detail="Colaborador não encontrado.",
            )

        return employee

    except HTTPException:
        raise

    except Exception:
        logger.exception("Erro ao buscar colaborador por ID")

        raise HTTPException(
            status_code=500,
            detail="Não foi possível buscar o colaborador.",
        )


@router.get("/matricula/{matricula}")
def get_employee_by_matricula(
    matricula: str,
    token: str = Depends(oauth2_scheme),
    user: AuthenticatedUser = Depends(get_current_user),
):
    """
    Busca colaborador pela matrícula.
    Acesso permitido somente para RH e Admin.
    """

    if not is_hr_or_admin(user):
        raise HTTPException(
            status_code=403,
            detail="Você não tem permissão para consultar colaboradores por matrícula.",
        )

    try:
        client = create_user_supabase_client(token)

        employee = find_employee_by_matricula(
            client=client,
            matricula=matricula,
        )

        if employee is None:
            raise HTTPException(
                status_code=404,
                detail="Colaborador não encontrado.",
            )

        return employee

    except HTTPException:
        raise

    except Exception:
        logger.exception("Erro ao buscar colaborador por matrícula")

        raise HTTPException(
            status_code=500,
            detail="Não foi possível buscar o colaborador.",
        )