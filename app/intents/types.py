from enum import Enum


class Intent(str, Enum):

    # Férias
    VACATION_BALANCE = "vacation_balance"
    VACATION_REQUEST = "vacation_request"


    # Salários
    SALARY_QUERY = "salary_query"


    # Benefícios
    BENEFITS_QUERY = "benefits_query"


    # Ponto
    ATTENDANCE_QUERY = "attendance_query"


    # Documentos
    DOCUMENT_QUERY = "document_query"


    # Políticas RH
    HR_POLICY = "hr_policy"


    # Conversa geral
    GENERAL_CHAT = "general_chat"