from app.knowledge.retriever import search_documents


results = search_documents(
    "Como funciona o período de férias?"
)


for result in results:

    print("\n----------------")
    
    print(
        result["metadata"]
    )

    print(
        result["content"][:500]
    )