from uuid import UUID

from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    refresh_token: str | None = None
    expires_in: int | None = None


class UserResponse(BaseModel):
    # id identifica a conta no Supabase Auth; employee_id identifica o cadastro RH.
    id: UUID
    employee_id: UUID
    nome: str
    email: EmailStr
    role: str
    cargo: str | None = None
    departamento: str | None = None
