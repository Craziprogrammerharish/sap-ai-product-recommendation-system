from app.services.semantic_search_service import (
    SemanticSearchService
)


class NLQueryService:

    def __init__(self):

        self.semantic_service = (
            SemanticSearchService()
        )

    def process_query(
        self,
        query: str,
        top_k: int = 5
    ):

        query = query.lower()

        cleaned_query = (
            query
            .replace("show me", "")
            .replace("find", "")
            .replace("search for", "")
            .replace("products", "")
            .replace("product", "")
            .strip()
        )

        results = (
            self.semantic_service.search(
                cleaned_query,
                top_k
            )
        )

        return {
            "original_query": query,
            "processed_query": cleaned_query,
            "results": results
        }