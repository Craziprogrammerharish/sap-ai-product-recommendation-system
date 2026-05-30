"""
SAP AI Product Recommendation System

Author: Harish B
Technical Assessment Submission

Description:
Product Similarity Search, Semantic Search,
Natural Language Query Processing,
and AI-Augmented Retrieval using Ollama.
"""


import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from scipy.sparse import hstack


def prepare_features(df: pd.DataFrame):

    df = df.copy()

    # Handle missing values
    df["product_name"] = df["product_name"].fillna("")
    df["brand"] = df["brand"].fillna("Unknown")
    df["colour"] = df["colour"].fillna("Unknown")

    # Combined text feature
    df["combined_text"] = (
        df["product_name"].astype(str)
        + " "
        + df["brand"].astype(str)
        + " "
        + df["colour"].astype(str)
    )

    # TF-IDF
    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=5000
    )

    text_features = vectorizer.fit_transform(
        df["combined_text"]
    )

    # Numeric columns
    numeric_cols = [
        "sales_price",
        "rating",
        "no__of_reviews"
    ]

    numeric_df = (
        df[numeric_cols]
        .fillna(0)
    )

    scaler = StandardScaler()

    numeric_features = scaler.fit_transform(
        numeric_df
    )

    final_features = hstack(
        [text_features, numeric_features]
    )

    return (
        final_features,
        vectorizer,
        scaler
    )

if __name__ == "__main__":

    df = pd.read_json(
        "data/marketing_sample_for_amazon_com-amazon_fashion_products__20200201_20200430__30k_data.ldjson",
        lines=True
    )

    features, vectorizer, scaler = prepare_features(df)

    print("Feature Matrix Shape:")
    print(features.shape)