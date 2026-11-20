from functools import lru_cache

from supabase import Client, create_client

from app.core.config import settings


def _validate_supabase_settings() -> None:
    missing = [
        name
        for name, value in (
            ("SUPABASE_URL", settings.SUPABASE_URL),
            ("SUPABASE_ANON_KEY", settings.SUPABASE_ANON_KEY),
        )
        if not value.strip()
    ]
    if missing:
        raise RuntimeError(
            "Configuração do Supabase ausente: " + ", ".join(missing)
        )


@lru_cache
def get_supabase_client() -> Client:
    """Cliente base do Supabase para operações sem identidade de usuário.

    Não use este cliente para consultas que dependem das políticas RLS do
    colaborador. Para isso, crie um cliente por requisição com o JWT do usuário.
    """
    _validate_supabase_settings()
    return create_client(settings.SUPABASE_URL, settings.SUPABASE_ANON_KEY)


def create_user_supabase_client(access_token: str) -> Client:
    """Cria um cliente isolado, vinculado ao JWT de um usuário autenticado.

    Uma instância por requisição evita compartilhar/mutar o token entre
    requisições concorrentes do FastAPI e permite que o PostgreSQL aplique RLS.
    """
    if not access_token or not access_token.strip():
        raise ValueError("O access token do usuário é obrigatório.")

    _validate_supabase_settings()
    client = create_client(settings.SUPABASE_URL, settings.SUPABASE_ANON_KEY)
    client.postgrest.auth(access_token)
    return client


def create_supabase_auth_client() -> Client:
    """Cria cliente isolado para operações de autenticação com credenciais.

    O login altera o estado de sessão do cliente Supabase. Por isso, não deve
    usar o cliente global/cacheado compartilhado entre requisições FastAPI.
    """
    _validate_supabase_settings()
    return create_client(settings.SUPABASE_URL, settings.SUPABASE_ANON_KEY)
