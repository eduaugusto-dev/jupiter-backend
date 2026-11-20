from app.repositories.user_repository import UserRepository


def get_user_repository() -> UserRepository:
    """
    Retorna uma instância do repositório de usuários.
    """

    return UserRepository()