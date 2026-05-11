from backend.rag import get_rag

# Similarity Threshold
# Lower score = better match
SIMILARITY_THRESHOLD = 1.5


def handle_query(query: str) -> str:

    try:

        print("\n🔥 handle_query CALLED 🔥")

        # Load RAG database
        rag = get_rag(query)

        # Get top matching result
        results = rag.similarity_search_with_score(query, k=1)

        print("RESULTS:", results)

        # Check if results exist
        if results and len(results) > 0:

            doc, score = results[0]

            print("\n===== DEBUG =====")
            print("Query:", query)
            print("Score:", score)
            print("Matched Content:", doc.page_content[:200])
            print("=================\n")

            # IMPORTANT:
            # In FAISS similarity_search_with_score
            # LOWER score = BETTER match

            if score <= SIMILARITY_THRESHOLD:

                return doc.page_content.strip()

        # No relevant match found
        return "No solution found. Ticket will be created."

    except Exception as e:

        print("ERROR in handle_query:", str(e))

        return "Something went wrong. Please try again."