from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.dependencies.auth import AuthenticatedUser, get_current_user
from app.schemas.auth import TokenResponse, UserResponse
from app.services.auth_service import login as login_service


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Autentica no Supabase Auth e retorna os tokens oficiais."""
    return login_service(
        email=form_data.username,
        password=form_data.password,
    )


@router.get("/perfil", response_model=UserResponse)
def perfil(user: AuthenticatedUser = Depends(get_current_user)):
    """Retorna o perfil do colaborador associado à conta autenticada."""
    return UserResponse(
        id=user.id,
        employee_id=user.employee_id,
        nome=user.employee.nome,
        email=user.email,
        role=user.role,
        cargo=user.employee.cargo,
        departamento=user.employee.departamento,
    )
