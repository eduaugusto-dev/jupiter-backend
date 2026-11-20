from enum import StrEnum


class Role(StrEnum):
    """
    Papéis (roles) utilizados pelo sistema de autorização do Rogério.
    """

    ADMIN = "ADMIN"
    RH = "RH"
    GESTOR = "GESTOR"
    COLABORADOR = "COLABORADOR"