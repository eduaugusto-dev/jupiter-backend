from fastapi import HTTPException, status

from app.database.supabase import create_supabase_auth_client


def login(email: str, password: str) -> dict:
    """Autentica credenciais pelo Supabase Auth e devolve os tokens oficiais."""
    try:
        response = create_supabase_auth_client().auth.sign_in_with_password(
            {"email": email, "password": password}
        )
    except Exception:
        # Resposta genérica para não revelar se o e-mail existe.
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha inválidos",
        )

    session = getattr(response, "session", None)
    if session is None or not getattr(session, "access_token", None):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Não foi possível iniciar a sessão no Supabase Auth",
        )

    return {
        "access_token": session.access_token,
        "refresh_token": getattr(session, "refresh_token", None),
        "expires_in": getattr(session, "expires_in", None),
        "token_type": "bearer",
    }
