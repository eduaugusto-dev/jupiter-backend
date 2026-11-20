
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
        Orquestra as decisões do Júpiter.

        Primeiro tenta consultas estruturadas.
        Caso não encontre uma intenção tratada,
        segue para RAG + LLM.
        """

        decision = process_decision(
            message=question,
            user=user,
            client=client,
        )

        if decision:
            return decision

        context = search_documents(question)

        prompt = build_prompt(
            question=question,
            context=context,
        )

        response = generate_response(prompt)

        return {
            "response": response,
            "intent": "KNOWLEDGE_QUERY",
            "source": "rag_llm",
        }


agent = AgentOrchestrator()
