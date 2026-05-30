import pandas as pd

from app.preprocessing.feature_engineering import (
    prepare_features
)

from app.vector_search.faiss_index import (
    build_faiss_index,
    search_similar_products
)


class SimilarityService:

    def __init__(self):

        self.df = pd.read_json(
            "data/marketing_sample_for_amazon_com-amazon_fashion_products__20200201_20200430__30k_data.ldjson",
            lines=True
        )

        (
            self.features,
            self.vectorizer,
            self.scaler
        ) = prepare_features(self.df)

        (
            self.index,
            self.dense_matrix
        ) = build_faiss_index(
            self.features
        )

    def find_similar_products(
        self,
        product_id: str,
        num_similar: int = 5
    ):

        product_row = self.df[
            self.df["uniq_id"] == product_id
        ]

        if product_row.empty:
            raise ValueError(
                f"Product ID {product_id} not found"
            )

        product_index = product_row.index[0]

        scores, indices = search_similar_products(
            self.index,
            self.dense_matrix,
            product_index,
            num_similar
        )

        similar_products = (
            self.df.iloc[indices]["uniq_id"]
            .tolist()
        )

        return similar_products

if __name__ == "__main__":

    service = SimilarityService()

    sample_id = (
        service.df.iloc[0]["uniq_id"]
    )

    result = service.find_similar_products(
        sample_id,
        5
    )

    print(result)