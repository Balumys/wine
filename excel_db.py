import pandas as pd


def get_product_data(file, field_names):
    wines_df = pd.read_excel(file, names=field_names,
                             na_values=' ',
                             keep_default_na=False)
    grouped_df = wines_df.groupby('Category')

    wines = {name: group.to_dict(orient="records") for name, group in grouped_df}

    return wines
