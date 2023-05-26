import draw_age_map
import geopandas as gpd
import draw_apartment_price_map
import matplotlib.pyplot as plt
import seaborn as sns

def createSeoulApartmentPriceMap(city_df, start_year, end_year):
    # Getting submunicipalities with zero transaction data
    seoul_blank_df = city_df[city_df["년"].isnull()].groupby(["법정동", "geometry", "법정동명"],as_index=False)["거래금액"].sum() 
    # Finding the mean housing price for from a start year to an end year
    seoul_housing_df = city_df[
        ((city_df['년'] >= start_year) & (city_df['년'] <= end_year))
    ].groupby(["법정동", "geometry", "법정동명"],as_index=False)["거래금액"].mean()
    
    # Merging DFs
    seoul_df = seoul_housing_df.merge(seoul_blank_df, how="outer")
    
    # Creating DFs into a GeoDataframe with EPSG:5179
    seoul_df = gpd.GeoDataFrame(seoul_df, geometry=seoul_df["geometry"])
    seoul_df.crs = "EPSG:5179"
    
    # Drawing the map
    seoul_map = draw_apartment_price_map.main(seoul_df)
    seoul_map
    
    # Saving the map as an html
    seoul_map.save(f'{start_year}-{end_year}ApartmentPriceVisualization.html')
# %%
def createPopulationVisualizationMapForAllYears(city_df, age_group):
    # Go through every year and get it's Population Visualization
    for year in city_df['년'].unique():
        # Get the mean population of each age group
        seoul_population_age = city_df[city_df["년"]==year].groupby(
                ["법정동", "geometry", "법정동명"],as_index=False
            )[age_group].mean()  
        
        # Creating DFs into a GeoDataframe with EPSG:5179
        seoul_population_age = gpd.GeoDataFrame(seoul_population_age, geometry=seoul_population_age["geometry"])
        seoul_population_age.crs = "EPSG:5179"
        
        # Drawing the map
        seoul_population_map = draw_age_map.main(seoul_population_age)
        seoul_population_map
        
        # Saving the map as an html
        seoul_population_map.save(f'{year}PopulationVisualization.html')

def createBarPlot(city_df, age_group):
    seoul_population_age_by_year = city_df.groupby('년', as_index=False)[age_group].sum()
    seoul_population_age_by_year.plot(x="년", y=age_group, kind="bar", figsize=(9, 8))
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Seoul Population By Age Group")
    plt.show()
    
def createLinePlot(city_df, age_group):
    seoul_population_age_by_year = city_df.groupby('년', as_index=False)[list].sum()
    seoul_population_age_by_year.plot(x="년", y=age_group, kind="line", figsize=(10, 10))
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(title="Age Groups")
    plt.title("Seoul Population for Each Age Group")
    plt.show()

def createHeatmap(city_df, age_group):
    # Defining figure size  
    # for the output plot 
    fig, ax = plt.subplots(figsize = (20, 10))
    
    
    # Displaying dataframe as an heatmap 
    # with diverging colourmap as RdYlGn
    seoul_population_age_by_year = city_df.groupby('년')[age_group].sum()

    sns.heatmap(seoul_population_age_by_year, cmap ='RdYlGn', linewidths = 0.50, annot = True)
    ax.set(xlabel='Age Groups',
        ylabel='Years',
        title='Heatmap of Each Age Group')