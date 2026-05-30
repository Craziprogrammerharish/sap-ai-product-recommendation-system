
"""
SAP AI Product Recommendation System

Author: Harish B
Technical Assessment Submission

Description:
Product Similarity Search, Semantic Search,
Natural Language Query Processing,
and AI-Augmented Retrieval using Ollama.
"""

import faiss
import numpy as np


def build_faiss_index(feature_matrix):

    dense_matrix = feature_matrix.toarray().astype("float32")

    # Normalize for cosine similarity
    faiss.normalize_L2(dense_matrix)

    dimension = dense_matrix.shape[1]

    index = faiss.IndexFlatIP(dimension)

    index.add(dense_matrix)

    return index, dense_matrix


def search_similar_products(
    index,
    dense_matrix,
    product_index,
    top_k=5
):

    query_vector = dense_matrix[
        product_index:product_index + 1
    ]

    scores, indices = index.search(
        query_vector,
        top_k + 1
    )

    return scores[0][1:], indices[0][1:]


if __name__ == "__main__":

    import pandas as pd

    from app.preprocessing.feature_engineering import (
        prepare_features
    )

    df = pd.read_json(
        "data/marketing_sample_for_amazon_com-amazon_fashion_products__20200201_20200430__30k_data.ldjson",
        lines=True
    )

    features, _, _ = prepare_features(df)

    index, dense_matrix = build_faiss_index(
        features
    )

    scores, indices = search_similar_products(
        index,
        dense_matrix,
        product_index=0,
        top_k=5
    )

    print("Scores:")
    print(scores)

    print("\nIndices:")
    print(indices)