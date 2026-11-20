from fastapi import APIRouter, Depends

from app.dependencies.auth import AuthenticatedUser, get_current_user
from app.schemas.employee import EmployeeResponse


router = APIRouter(tags=["Profile"])


@router.get("/me", response_model=EmployeeResponse)
def get_me(user: AuthenticatedUser = Depends(get_current_user)):
    """Retorna o cadastro RH do colaborador autenticado via Supabase."""
    return EmployeeResponse(
        id=user.employee.id,
        nome=user.employee.nome,
        email=user.email,
        cargo=user.employee.cargo,
        departamento=user.employee.departamento,
        role=user.role,
        employee_code=user.employee.employee_code,
        employment_status=user.employee.employment_status or "unknown",
        hire_date=user.employee.hire_date,
    )
