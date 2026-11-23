
from app.decision.engine import process_decision
from app.knowledge.retriever import search_documents
from app.llm.prompt_builder import build_prompt
from app.llm.groq_client import generate_response


class AgentOrchestrator:

    def execute(
        self,
        question: str,
        user,
        client,
    ):
        """
        Orquestra o Júpiter utilizando dados estruturados (SQL)
        e conhecimento documental (RAG).

        Recupera dados estruturados quando disponíveis, busca
        documentos relevantes e combina os contextos para o LLM.
        """

        # 1. Consulta estruturada (SQL / BDA)
        decision = process_decision(
            message=question,
            user=user,
            client=client,
        )

        sql_context = ""

        if decision:
            sql_context = (
                decision.get("response", "")
                if isinstance(decision, dict)
                else str(decision)
            )

        # 2. Busca documental (RAG)
        document_context = search_documents(question)

        # 3. Combina os contextos recuperados
        combined_context = f"""
DADOS ESTRUTURADOS (SQL / BDA):
{sql_context or "Nenhum dado estruturado encontrado para esta consulta."}

BASE DE CONHECIMENTO (RAG):
{document_context or "Nenhum documento relevante encontrado."}
"""

        # 4. Construção do prompt com contexto híbrido
        prompt = build_prompt(
            question=question,
            context=combined_context,
        )

        # 5. Geração da resposta usando o LLM
        response = generate_response(prompt)

        # 6. Retorno padronizado
        return {
            "response": response,
            "intent": (
                decision.get("intent", "HYBRID_QUERY")
                if isinstance(decision, dict) and decision
                else "KNOWLEDGE_QUERY"
            ),
            "source": "hybrid_sql_rag" if decision else "rag_llm",
        }


agent = AgentOrchestrator()
