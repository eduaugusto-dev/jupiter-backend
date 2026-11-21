
import unicodedata


def normalize_text(text: str) -> str:
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    text = "".join(
        char for char in text
        if unicodedata.category(char) != "Mn"
    )
    return text


def classify_intent(message: str) -> str:
    if not message or not message.strip():
        return "KNOWLEDGE_QUERY"

    message = normalize_text(message)

    vacation_personal_keywords = [
        "meu saldo de ferias",
        "saldo das minhas ferias",
        "quantos dias de ferias tenho",
        "quantos dias tenho de ferias",
        "minhas ferias",
        "meu periodo de ferias",
        "quando serao minhas ferias",
        "quando vou tirar ferias",
        "tenho quantos dias de ferias",
        "quando fico de ferias",
        "quando entro de ferias",
        "quando comecam minhas ferias",
        "quando comeca minhas ferias",
        "quais as datas das minhas ferias",
        "quais sao as datas das minhas ferias",
    ]

    salary_personal_keywords = [
        "meu salario",
        "qual e meu salario",
        "quanto ganho",
        "quanto eu ganho",
        "minha remuneracao",
        "quanto recebo",
        "valor do meu salario",
        "meu pagamento",
    ]

    # Elegibilidade de benefícios
    benefit_eligibility_keywords = [
        "tenho direito ao beneficio",
        "tenho direito a esse beneficio",
        "tenho direito ao auxilio transporte",
        "tenho direito ao vale transporte",
        "tenho direito ao vale refeicao",
        "tenho direito ao auxilio alimentacao",
        "tenho direito ao auxilio home office",
        "tenho direito ao plano de saude",
        "tenho direito ao plano odontologico",
        "posso receber auxilio transporte",
        "posso receber vale transporte",
        "posso receber vale refeicao",
        "posso receber auxilio home office",
        "sou elegivel ao beneficio",
        "sou elegivel ao auxilio transporte",
        "quais sao os criterios para receber o beneficio",
        "quais sao os requisitos para receber o beneficio",
    ]

    # Benefícios em geral
    benefits_personal_keywords = [
        "meus beneficios",
        "quais sao meus beneficios",
        "quais beneficios tenho",
        "beneficios que tenho",
        "beneficios tenho",
        "meus beneficios ativos",
        "beneficios ativos para mim",
        "quais beneficios recebo",
        "quais beneficios a empresa oferece para mim",
        "quero consultar meus beneficios",
        "consultar beneficios",

        # Auxílio home office
        "meu auxilio home office",
        "auxilio home office",
        "quanto recebo de auxilio home office",
        "qual o valor do auxilio home office",
        "valor do meu auxilio home office",
        "como funciona o auxilio home office",

        # Plano de saúde
        "meu plano de saude",
        "plano de saude",
        "meu convenio medico",
        "convenio medico",
        "quanto vale meu plano de saude",
        "qual o valor do meu plano de saude",
        "como funciona meu plano de saude",
        "tenho plano de saude",

        # Plano odontológico
        "meu plano odontologico",
        "plano odontologico",
        "meu convenio odontologico",
        "convenio odontologico",
        "quanto vale meu plano odontologico",
        "qual o valor do meu plano odontologico",
        "como funciona meu plano odontologico",
        "tenho plano odontologico",

        # Vale-refeição
        "meu vale refeicao",
        "vale refeicao",
        "quanto recebo de vale refeicao",
        "qual o valor do meu vale refeicao",
        "valor do vale refeicao",
        "quanto tenho de vale refeicao",
        "quando recebo meu vale refeicao",
        "quando cai meu vale refeicao",
        "como funciona meu vale refeicao",
        "meu beneficio de alimentacao",
        "auxilio alimentacao",

        # Vale-transporte
        "meu vale transporte",
        "vale transporte",
        "quanto recebo de vale transporte",
        "qual o valor do meu vale transporte",
        "valor do vale transporte",
        "quanto tenho de vale transporte",
        "quando recebo meu vale transporte",
        "como funciona meu vale transporte",
        "meu beneficio de transporte",
        "auxilio transporte",
    ]

    time_clock_personal_keywords = [
        "meu ponto",
        "meus pontos",
        "meu ponto eletronico",
        "meu espelho de ponto",
        "minhas marcacoes",
        "minhas marcacoes de ponto",
        "marcacoes de hoje",
        "meus registros de ponto",
        "meu historico de ponto",
        "historico de ponto",
        "horario que entrei hoje",
        "que horas entrei hoje",
        "que horas sai hoje",
        "horario de entrada hoje",
        "horario de saida hoje",
        "bati meu ponto",
        "bati ponto hoje",
        "registros de hoje",
        "horas registradas hoje",
        "ultimo registro de ponto",
        "meu ultimo registro de ponto",
        "ultima marcacao de ponto",
        "minha ultima marcacao",
        "ultimo ponto registrado",
        "qual foi meu ultimo registro de ponto",
    ]

    time_bank_personal_keywords = [
        "meu banco de horas",
        "meus bancos de horas",
        "meu saldo de horas",
        "saldo do meu banco de horas",
        "saldo de banco de horas",
        "quanto tenho no banco de horas",
        "quantas horas tenho acumuladas",
        "horas acumuladas",
        "horas extras acumuladas",
        "estou devendo horas",
        "estou com horas negativas",
        "estou com horas positivas",
        "meu saldo de horas extras",
        "quanto devo de horas",
        "quanto tenho de horas extras",
        "como esta meu banco de horas",
    ]

    leaves_personal_keywords = [
        "minha licenca",
        "minhas licencas",
        "estou de licenca",
        "quando comeca minha licenca",
        "quando termina minha licenca",
        "quando acaba minha licenca",
        "meu afastamento",
        "meus afastamentos",
        "quando comeca meu afastamento",
        "quando termina meu afastamento",
        "quando acaba meu afastamento",
        "minha licenca paternidade",
        "licenca paternidade",
        "minha licenca maternidade",
        "licenca maternidade",
        "dias de licenca",
        "quantos dias de afastamento",
        "tenho alguma licenca registrada",
    ]

    thirteenth_salary_keywords = [
        "13 salario",
        "13o salario",
        "decimo terceiro",
        "meu decimo terceiro",
        "quanto vou receber de decimo terceiro",
        "quanto recebo de decimo terceiro",
        "valor do meu 13",
        "valor do 13",
        "valor do decimo terceiro",
        "quanto e meu decimo terceiro",
        "meu 13 salario",
        "meu 13o salario",
        "pagamento do decimo terceiro",
        "quando vou receber meu decimo terceiro",
        "quando sera pago meu decimo terceiro",
        "gratificacao natalina",
    ]

    if any(keyword in message for keyword in vacation_personal_keywords):
        return "VIEW_OWN_VACATIONS"

    if any(keyword in message for keyword in salary_personal_keywords):
        return "VIEW_OWN_SALARY"

    if any(keyword in message for keyword in benefit_eligibility_keywords):
        return "CHECK_BENEFIT_ELIGIBILITY"

    if any(keyword in message for keyword in benefits_personal_keywords):
        return "VIEW_OWN_BENEFITS"

    if any(keyword in message for keyword in time_clock_personal_keywords):
        return "VIEW_OWN_TIME_CLOCK"

    if any(keyword in message for keyword in time_bank_personal_keywords):
        return "VIEW_OWN_TIME_BANK"

    if any(keyword in message for keyword in leaves_personal_keywords):
        return "VIEW_OWN_LEAVES"

    if any(keyword in message for keyword in thirteenth_salary_keywords):
        return "VIEW_OWN_THIRTEENTH_SALARY"

    return "KNOWLEDGE_QUERY"
