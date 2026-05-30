# # quick_check.py

# import pandas as pd

# df = pd.read_json(
#     "data/marketing_sample_for_amazon_com-amazon_fashion_products__20200201_20200430__30k_data.ldjson",
#     lines=True
# )

# print(df[
#     [
#         "uniq_id",
#         "product_name",
#         "brand",
#         "sales_price",
#         "weight",
#         "rating",
#         "colour"
#     ]
# ].head(10))




import pandas as pd

df = pd.read_json(
    "data/marketing_sample_for_amazon_com-amazon_fashion_products__20200201_20200430__30k_data.ldjson",
    lines=True
)

print(
    df[
        [
            "product_name",
            "brand",
            "sales_price",
            "weight",
            "rating",
            "colour"
        ]
    ].head(20)
)