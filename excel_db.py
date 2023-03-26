import pandas as pd


def get_product_data():
    wines_df = pd.read_excel("wine2.xlsx", names=["Category", "Title", "Variety", "Price", "Image"], na_values=' ',
                             keep_default_na=False)
    grouped_df = wines_df.groupby('Category')

    wines = {}

    for name, group in grouped_df:
        wines[name] = group.to_dict(orient="records")

    return wines
