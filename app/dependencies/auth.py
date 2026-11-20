from dataclasses import dataclass
from types import SimpleNamespace
from typing import Any

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.core.security import get_supabase_authenticated_user
from app.database.supabase import create_user_supabase_client


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


@dataclass
class EmployeeContext:
    """Representação compatível com os campos usados pelo agente legado."""

    id: str
    auth_user_id: str
    nome: str
    email: str
    cargo: str | None = None
    departamento: str | None = None
    employee_code: str | None = None
    employment_status: str | None = None
    hire_date: str | None = None
    access_role: str | None = None


@dataclass
class AuthenticatedUser:
    """Identidade do Supabase adaptada ao contexto esperado pela aplicação."""

    id: str
    employee_id: str
    email: str
    role: str
    employee: EmployeeContext


def _normalize_role(access_role: str | None) -> str:
    """Converte os papéis do Supabase para os nomes usados pelo agente atual."""
    value = (access_role or "").strip().lower()
    role_mapping = {
        "hr": "RH",
        "rh": "RH",
        "admin": "ADMIN",
        "administrator": "ADMIN",
        "manager": "GESTOR",
        "gestor": "GESTOR",
        "employee": "COLABORADOR",
        "colaborador": "COLABORADOR",
    }
    return role_mapping.get(value, value.upper() or "COLABORADOR")


def _value(record: Any, key: str, default: Any = None) -> Any:
    """Lê um campo de registros retornados pelo SDK ou de dicionários."""
    if isinstance(record, dict):
        return record.get(key, default)
    return getattr(record, key, default)


def get_current_user(
    token: str = Depends(oauth2_scheme),
) -> AuthenticatedUser:
    """Valida o JWT no Supabase e carrega o perfil respeitando o RLS."""
    auth_user = get_supabase_authenticated_user(token)
    if auth_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    auth_user_id = str(_value(auth_user, "id", ""))
    email = _value(auth_user, "email")
    if not auth_user_id or not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Identidade do usuário não foi retornada pelo Supabase Auth",
        )

    try:
        # Cliente exclusivo desta requisição, autenticado com o JWT do usuário.
        # A consulta à tabela employees fica sujeita às políticas RLS.
        user_client = create_user_supabase_client(token)
        result = (
            user_client.table("employees")
            .select(
                "id, auth_user_id, full_name, employee_code, job_title, "
                "department, hire_date, employment_status, access_role"
            )
            .eq("auth_user_id", auth_user_id)
            .limit(1)
            .execute()
        )
        employee_rows = result.data or []
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Não foi possível consultar o perfil no Supabase",
        )

    if not employee_rows:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuário autenticado, mas sem colaborador vinculado no cadastro de RH",
        )

    employee_data = employee_rows[0]
    employee_id = str(_value(employee_data, "id", ""))
    if not employee_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cadastro de colaborador inválido",
        )

    access_role = _value(employee_data, "access_role")
    employee = EmployeeContext(
        id=employee_id,
        auth_user_id=auth_user_id,
        nome=_value(employee_data, "full_name", ""),
        email=email,
        cargo=_value(employee_data, "job_title"),
        departamento=_value(employee_data, "department"),
        employee_code=_value(employee_data, "employee_code"),
        employment_status=_value(employee_data, "employment_status"),
        hire_date=_value(employee_data, "hire_date"),
        access_role=access_role,
    )

    return AuthenticatedUser(
        id=auth_user_id,
        employee_id=employee_id,
        email=email,
        role=_normalize_role(access_role),
        employee=employee,
    )
