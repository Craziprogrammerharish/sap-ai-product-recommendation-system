"""
SAP AI Product Recommendation System

Author: Harish B
Technical Assessment Submission

Description:
Product Similarity Search, Semantic Search,
Natural Language Query Processing,
and AI-Augmented Retrieval using Ollama.
"""

import requests

from app.services.semantic_search_service import (
    SemanticSearchService
)


class AIQueryService:

    def __init__(self):

        self.semantic_service = (
            SemanticSearchService()
        )

    def process(
        self,
        query: str,
        top_k: int = 5
    ):

        prompt = f"""
Convert the user query into a clean product search query.

User Query:
{query}

Return only the cleaned search phrase.
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:1b",
                "prompt": prompt,
                "stream": False
            }
        )

        llm_query = (
            response.json()["response"]
            .strip()
        )

        results = (
            self.semantic_service.search(
                llm_query,
                top_k
            )
        )

        return {
            "original_query": query,
            "llm_query": llm_query,
            "results": results
        }