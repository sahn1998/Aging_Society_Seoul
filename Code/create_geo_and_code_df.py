import os
import pandas as pd
import geopandas as gpd
import numpy as np
import keys

class NeighborhoodProcessor:
    @staticmethod
    def read_geography_data(file_path):
        kr_dong_geo = gpd.read_file(file_path)
        kr_dong_geo.crs = "EPSG:5179"
        kr_dong_geo["EMD_CD"] = kr_dong_geo["EMD_CD"].astype(np.int64)
        return kr_dong_geo
    @staticmethod
    def preprocess_geo_dataframe(df, province_name):
        df = df[df["EMD_CD"].astype(pd.StringDtype()).str.startswith(keys.KOREA_PROVINCE_CODE_PREFIX[province_name])] # seoul geography data frame
        df = df.drop("EMD_KOR_NM", axis=1)
        df = df.rename({'EMD_CD': '법정동코드'}, axis=1)
        return df
    @staticmethod
    def preprocess_code_dataframe(df):
        df.reset_index(inplace=True)
        df = df.iloc[1:, :]
        df["법정동"] = df["법정동명"].str.rsplit().str[-1]
        df.loc[:, "법정동코드"] = df["법정동코드"].astype(pd.StringDtype()).str[:-2].astype(np.int64)
        return df
    
def main(province_name):
    neighborhood_processor = NeighborhoodProcessor()
    
    geo_df = neighborhood_processor.read_geography_data("../KoreaGeoData/kr_dong.shp")
    geo_df = neighborhood_processor.preprocess_geo_dataframe(geo_df, province_name)
    
    # Create necessary code dataframe that has submunicipality codes
    code_df = pd.read_excel(f'../KoreaRegionalCode/{province_name}_code.xls', index_col=0)
    code_df = neighborhood_processor.preprocess_code_dataframe(code_df)
    
    return geo_df, code_df
    


