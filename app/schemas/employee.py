from datetime import date
from uuid import UUID

from pydantic import BaseModel, EmailStr


class EmployeeResponse(BaseModel):
    id: UUID
    nome: str
    email: EmailStr
    cargo: str | None = None
    departamento: str | None = None
    role: str
    employee_code: str | None = None
    employment_status: str
    hire_date: date | None = None
