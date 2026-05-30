# from fastapi import APIRouter, HTTPException

# from app.services.similarity_service import SimilarityService

# from app.services.nl_query_service import (
#     NLQueryService
# )

# semantic_service = SemanticSearchService()

# nl_query_service = NLQueryService()



# from app.services.semantic_search_service import (
#     SemanticSearchService
# )
# service = SimilarityService()

# semantic_service = SemanticSearchService()


# router = APIRouter()

# service = SimilarityService()


"""
SAP AI Product Recommendation System

Author: Harish B
Technical Assessment Submission

Description:
Product Similarity Search, Semantic Search,
Natural Language Query Processing,
and AI-Augmented Retrieval using Ollama.
"""

from fastapi import APIRouter, HTTPException

from app.services.similarity_service import SimilarityService

from app.services.ai_query_service import (
    AIQueryService
)

from app.services.semantic_search_service import (
    SemanticSearchService
)

from app.services.nl_query_service import (
    NLQueryService
)

router = APIRouter()

service = SimilarityService()

semantic_service = SemanticSearchService()

nl_query_service = NLQueryService()

ai_query_service = AIQueryService()

@router.get("/find_similar_products")
def find_similar_products(
    product_id: str,
    num_similar: int = 5
):

    try:

        result = service.find_similar_products(
            product_id,
            num_similar
        )

        return {
            "product_id": product_id,
            "similar_products": result
        }

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
@router.get("/semantic_search")
def semantic_search(
    query: str,
    top_k: int = 5
):

    try:

        results = semantic_service.search(
            query,
            top_k
        )

        return {
            "query": query,
            "results": results
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
@router.get("/nl_query")
def nl_query(
    query: str,
    top_k: int = 5
):

    try:

        result = (
            nl_query_service.process_query(
                query,
                top_k
            )
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
@router.get("/ai_query")
def ai_query(
    query: str,
    top_k: int = 5
):

    try:

        result = ai_query_service.process(
            query,
            top_k
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
