from fastapi import APIRouter


from app.api.routes.auth import router as auth_router
from app.api.routes.health import router as health_router

from app.api.chat import router as chat_router
from app.api.conversation import router as conversation_router
from app.api.employee import router as employee_router
from app.api.vacation import router as vacation_router
from app.api.me import router as me_router
from app.api.payroll import router as payroll_router


api_router = APIRouter()


# Health check
api_router.include_router(
    health_router
)


# Autenticação
api_router.include_router(
    auth_router
)


# Perfil do usuário
api_router.include_router(
    me_router
)


# Chat do Júpiter
api_router.include_router(
    chat_router
)


# Histórico de conversas
api_router.include_router(
    conversation_router
)


# Dados de colaboradores
api_router.include_router(
    employee_router
)


# Férias
api_router.include_router(
    vacation_router
)


# Folha de pagamento
api_router.include_router(
    payroll_router
)