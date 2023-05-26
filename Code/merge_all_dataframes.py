import os
import pandas as pd

def merge_apartment_dataframes(path, province_name, geo_df, code_df):
    apartment_df = pd.read_csv(
        os.path.join(path, f'{province_name}.csv')
    )
    merged_df = geo_df.merge(code_df, on="법정동코드", how="left")
    merged_df = merged_df.merge(apartment_df, on="법정동", how="left")
    return merged_df

def merge_pop_dataframes(path, province_name, geo_df, code_df):
    population_by_age_df = pd.read_csv(
        os.path.join(path, f'{province_name}_age_population_2012_2022.csv')
    )
    merged_df = geo_df.merge(code_df, on="법정동코드", how="left")
    merged_df = merged_df.merge(population_by_age_df, on="법정동", how="left")
    return merged_df