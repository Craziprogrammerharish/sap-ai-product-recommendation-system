import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SemanticSearchService:

    def __init__(self):

        self.df = pd.read_json(
            "data/marketing_sample_for_amazon_com-amazon_fashion_products__20200201_20200430__30k_data.ldjson",
            lines=True
        )

        self.df["product_name"] = (
            self.df["product_name"]
            .fillna("")
            .astype(str)
        )

        self.df["brand"] = (
            self.df["brand"]
            .fillna("Unknown")
            .astype(str)
        )

        self.df["colour"] = (
            self.df["colour"]
            .fillna("Unknown")
            .astype(str)
        )

        self.df["combined_text"] = (
            self.df["product_name"]
            + " "
            + self.df["brand"]
            + " "
            + self.df["colour"]
        )

        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=5000
        )

        self.text_vectors = (
            self.vectorizer.fit_transform(
                self.df["combined_text"]
            )
        )

    def search(
        self,
        query: str,
        top_k: int = 5
    ):

        query_vector = self.vectorizer.transform(
            [query]
        )

        similarities = cosine_similarity(
            query_vector,
            self.text_vectors
        ).flatten()

        top_indices = (
            similarities.argsort()[-top_k:][::-1]
        )

        results = []

        for idx in top_indices:

            row = self.df.iloc[idx]

            results.append(
                {
                    "uniq_id": str(row["uniq_id"]),
                    "product_name": str(
                        row["product_name"]
                    ),
                    "brand": str(
                        row["brand"]
                    ),
                    "score": float(
                        similarities[idx]
                    )
                }
            )

        return results