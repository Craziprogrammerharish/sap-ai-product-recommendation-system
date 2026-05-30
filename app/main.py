
"""
SAP AI Product Recommendation System

Author: Harish B
Technical Assessment Submission

Description:
Product Similarity Search, Semantic Search,
Natural Language Query Processing,
and AI-Augmented Retrieval using Ollama.
"""

from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="SAP Product Similarity Search API"
)

app.include_router(router)


@app.get("/")
def health_check():

    return {
        "status": "running"
    }