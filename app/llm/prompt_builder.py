def build_prompt(
    question: str,
    context: list
):
    """
    Monta o prompt com contexto RH.
    """

    context_text = "\n\n".join(
        [
            item["content"]
            for item in context
        ]
    )


    prompt = f"""
Você é o Júpiter, assistente virtual de RH da SeguraOz.

Sua função é responder dúvidas de colaboradores
utilizando exclusivamente o contexto fornecido.

Se a informação não estiver no contexto,
informe que não possui essa informação.

Contexto:

{context_text}


Pergunta:

{question}


Resposta:
"""


    return prompt