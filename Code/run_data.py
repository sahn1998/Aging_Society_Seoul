#%%
import create_district_csv
import create_geo_and_code_df
import merge_all_dataframes
import create_maps
import numpy as np

province_name = "Seoul"

# If you need to get data.
create_district_csv.main(province_name)

#geo_df, code_df = create_geo_and_code_df.main(province_name)

# To create a map of Seoul Apartment Price
'''
path = f'../{province_name}Data/HousingPrices/'
seoul_price_df = merge_all_dataframes.merge_apartment_dataframes(path, province_name, geo_df, code_df)
create_maps.createSeoulApartmentPriceMap(seoul_price_df, 2012, 2023)
'''

# To continue below this, you must run the code below.
'''
path= f'../{province_name}Data/Population/'
seoul_pop_df = merge_all_dataframes.merge_pop_dataframes(path, province_name, geo_df, code_df)
seoul_pop_df['년'] = seoul_pop_df['년'].astype(np.int64()) 

for col in seoul_pop_df.iloc[:, 1:]:
    seoul_pop_df = seoul_pop_df.rename({col : col.rsplit()[0][:-1]}, axis=1)
seoul_pop_df = seoul_pop_df.rename({"100": "100+"})
'''
# To create map of Population by Age Group of all years
'''
age_group = [
    "총 인구수",
    "0~9",
    "10~19",
    "20~29",
    "30~39",
    "40~49",
    "50~59",
    "60~69",
    "70~79",
    "80~89",
    "90~99",
    "100+" 
]

create_maps.PopulationVisualizationMapForAllYears(seoul_pop_df, age_group):
'''

# To create a bar plot of the population by age group
'''
age_group = [
    "0~9",
    "10~19",
    "20~29",
    "30~39",
    "40~49",
    "50~59",
    "60~69",
    "70~79",
    "80~89",
    "90~99",
    "100+" 
]
create_maps.createBarPlot(seoul_pop_df, age_group)
'''
# To create a line plot of the population by age group
'''
age_group = [
    "0~9",
    "10~19",
    "20~29",
    "30~39",
    "40~49",
    "50~59",
    "60~69",
    "70~79",
    "80~89",
    "90~99",
    "100+" 
]
create_maps.createLinePlot(city_df, age_group)
'''

# To create a heapmap of the population by age group
'''
age_group = [
    "0~9",
    "10~19",
    "20~29",
    "30~39",
    "40~49",
    "50~59",
    "60~69",
    "70~79",
    "80~89",
    "90~99",
    "100+" 
]
create_maps.createHeatmap(city_df, age_group)
'''
# %%
