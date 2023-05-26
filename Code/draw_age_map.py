

import folium

class AgeMapPlotter:
    def __init__(self):
        self.sample_map = folium.Map(
            location=[37.541, 126.986],
            zoom_start=11,
            min_zoom=10,
            max_zoom=14,
            overlay=True
        )

    def plot_map(self, df):

        highlight_function = lambda x: {
            'fillColor': '#000000', 
            'color':'#000000', 
            'fillOpacity': 0.50, 
            'weight': 0.1
        }
        style_function = lambda x: {
            'fillColor': '#ffffff',
            'color': '#000000',
            'fillOpacity': 0.1,
            'weight': 0.1
        }
        
        for col in df.iloc[:, 3:]:
            feature_group = folium.FeatureGroup(name=col,overlay=False).add_to(self.sample_map)
            choropleth = folium.Choropleth(
                geo_data=df,
                data=df,
                columns=['법정동', col],
                key_on="feature.properties.법정동",
                fill_color='YlGnBu',
                fill_opacity=0.8,
                line_opacity=0.6,
                line_color='#1B9C85',
                legend_name=col,
                smooth_factor=0,
                highlight=True,
                name=col,
                show=False,
                overlay=True,
                nan_fill_color="White"
            ).geojson.add_to(feature_group)
        
            folium.features.GeoJson(
                data=df,
                style_function=style_function,
                control=False,
                highlight_function=highlight_function,
                tooltip=folium.features.GeoJsonTooltip(
                    fields=['법정동명', col],
                    aliases=['지역', '총 인구수'],
                    style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
                )
            ).add_to(choropleth)
            
    def display_map(self):
        folium.TileLayer('cartodbpositron',overlay=True,name="View in Light Mode").add_to(self.sample_map)
        
        folium.LayerControl(collapsed=False).add_to(self.sample_map)
        return self.sample_map
    
def main(df):
    map_plotter = AgeMapPlotter()
    map_plotter.plot_map(df)
    sample_map = map_plotter.display_map()
    return sample_map