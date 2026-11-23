
def build_prompt(
    question: str,
    context,
):
    """
    Monta o prompt do Júpiter.
    Aceita contexto documental (RAG) ou contexto híbrido (SQL + RAG).
    """

    # Contexto RAG: lista de documentos/chunks
    if isinstance(context, list):
        context_text = "\n\n".join(
            item["content"]
            for item in context
            if isinstance(item, dict) and item.get("content")
        )

    # Contexto híbrido: string já consolidada pelo orquestrador
    elif isinstance(context, str):
        context_text = context

    else:
        context_text = ""

    prompt = f"""
Você é o Júpiter, assistente virtual de RH da SeguraOz.

Sua função é responder dúvidas dos colaboradores utilizando
as informações fornecidas no contexto.

REGRAS IMPORTANTES:

1. Utilize exclusivamente as informações presentes no contexto.
2. Não invente dados, políticas, prazos, valores ou procedimentos.
3. Diferencie dados individuais do colaborador de políticas gerais da empresa.
4. Quando houver dados estruturados (SQL/BDA) e documentos (RAG),
   utilize ambas as fontes quando forem relevantes para a pergunta.
5. Se as fontes não fornecerem informações suficientes para responder,
   informe claramente o que não foi encontrado.
6. Se houver informações de apenas uma fonte, responda somente com
   o que essa fonte permite afirmar.
7. Não considere informações pendentes como aprovadas.
8. Não invente conclusões sobre conformidade com políticas se os critérios
   necessários não estiverem documentados.
9. Oriente o colaborador a procurar o RH quando a informação ausente
   exigir validação humana.

CONTEXTO DISPONÍVEL:

{context_text}

PERGUNTA DO COLABORADOR:

{question}

RESPOSTA DO JÚPITER:
"""

    return prompt
