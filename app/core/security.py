"""Validação de identidade usando exclusivamente o Supabase Auth.

A FastAPI não emite mais JWTs próprios nem armazena/verifica senhas locais.
A emissão e a validação dos tokens são responsabilidade do Supabase Auth.
"""

from typing import Any

from app.database.supabase import get_supabase_client


def get_supabase_authenticated_user(access_token: str) -> Any | None:
    """Valida o access token no Supabase Auth e retorna o usuário autenticado.

    A validação é feita pelo endpoint oficial get_user, não apenas pela leitura
    local do conteúdo do JWT. Em caso de token inválido/expirado, retorna None.
    """
    if not access_token or not access_token.strip():
        return None

    try:
        response = get_supabase_client().auth.get_user(access_token)
    except Exception:
        # Não expor detalhes internos do provedor nem aceitar token inválido.
        return None

    user = getattr(response, "user", None)
    if user is not None:
        return user

    # Compatibilidade com versões/respostas que encapsulam o usuário em data.
    data = getattr(response, "data", None)
    return getattr(data, "user", None) if data is not None else None
