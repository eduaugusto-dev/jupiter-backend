from app.models import User


class UserRepository:
    """
    Repositório responsável pelo acesso aos usuários.

    Atualmente utiliza uma base temporária em memória.
    Futuramente será integrado ao PostgreSQL.
    """

    def __init__(self):
        """
        Inicializa o repositório.
        """

        self._users = {

            "admin@seguraoz.com": {
                "id": 1,
                "nome": "Administrador",
                "email": "admin@seguraoz.com",
                "role": "ADMIN",
                "password": "$2b$12$9Eg9du.7LdoiRW2HkzpFsOS48RfrMY9KfL3X4PnojtgxzaQJ3ao/S",
            },

            "colaborador@seguraoz.com": {
                "id": 2,
                "nome": "Colaborador Teste",
                "email": "colaborador@seguraoz.com",
                "role": "COLABORADOR",
                "password": "$2b$12$9Eg9du.7LdoiRW2HkzpFsOS48RfrMY9KfL3X4PnojtgxzaQJ3ao/S",
            },

            "rh@seguraoz.com": {
                "id": 3,
                "nome": "Analista RH",
                "email": "rh@seguraoz.com",
                "role": "RH",
                "password": "$2b$12$9Eg9du.7LdoiRW2HkzpFsOS48RfrMY9KfL3X4PnojtgxzaQJ3ao/S",
            },
        }

    # ==========================================================
    # Conversores
    # ==========================================================

    def _to_user(
        self,
        data: dict,
    ) -> User:
        """
        Converte um dicionário em um objeto User.
        """

        return User(
            id=data["id"],
            nome=data["nome"],
            email=data["email"],
            role=data["role"],
            password=data["password"],
        )

    # ==========================================================
    # Consultas
    # ==========================================================

    def get_by_email(
        self,
        email: str,
    ) -> User | None:
        """
        Busca um usuário pelo e-mail.
        """

        data = self._users.get(email)

        if data is None:
            return None

        return self._to_user(data)

    def get_by_id(
        self,
        user_id: int,
    ) -> User | None:
        """
        Busca um usuário pelo ID.
        """

        for data in self._users.values():

            if data["id"] == user_id:
                return self._to_user(data)

        return None

    def get_all(
        self,
    ) -> list[User]:
        """
        Retorna todos os usuários.
        """

        return [
            self._to_user(user)
            for user in self._users.values()
        ]