from app.authorization.permissions import (
    ROLE_PERMISSIONS,
    Permission,
)


def has_permission(
    user,
    permission: Permission,
) -> bool:
    """
    Verifica se o usuário possui determinada permissão.
    """


    role = user.role


    permissions = ROLE_PERMISSIONS.get(
        role,
        []
    )


    return permission in permissions