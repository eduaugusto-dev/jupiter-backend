from enum import Enum


class Permission(str, Enum):

    # Colaboradores
    VIEW_EMPLOYEES = "view_employees"
    MANAGE_EMPLOYEES = "manage_employees"


    # Salários
    VIEW_ALL_SALARIES = "view_all_salaries"
    VIEW_OWN_SALARY = "view_own_salary"


    # Férias
    VIEW_ALL_VACATIONS = "view_all_vacations"
    VIEW_OWN_VACATIONS = "view_own_vacations"
    MANAGE_VACATIONS = "manage_vacations"


    # Documentos RH
    VIEW_DOCUMENTS = "view_documents"
    MANAGE_DOCUMENTS = "manage_documents"


    # Conversação com Rogério
    CHAT_AGENT = "chat_agent"


    # Perfil
    VIEW_PROFILE = "view_profile"

ROLE_PERMISSIONS = {


    "RH": [

        Permission.VIEW_EMPLOYEES,
        Permission.MANAGE_EMPLOYEES,

        Permission.VIEW_ALL_SALARIES,

        Permission.VIEW_ALL_VACATIONS,
        Permission.MANAGE_VACATIONS,

        Permission.VIEW_DOCUMENTS,
        Permission.MANAGE_DOCUMENTS,

        Permission.CHAT_AGENT,
        Permission.VIEW_PROFILE,

    ],


    "GESTOR": [

        Permission.VIEW_EMPLOYEES,

        Permission.VIEW_ALL_VACATIONS,

        Permission.CHAT_AGENT,
        Permission.VIEW_PROFILE,

    ],


    "COLABORADOR": [

        Permission.VIEW_OWN_VACATIONS,
        Permission.VIEW_OWN_SALARY,

        Permission.CHAT_AGENT,
        Permission.VIEW_PROFILE,

    ]

}