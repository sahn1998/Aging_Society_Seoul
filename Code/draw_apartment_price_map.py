
import pandas as pd
import branca.colormap as cm
import folium

class HousingMapPlotter:
    def __init__(self):
        self.sample_map = folium.Map(
            location=[37.541, 126.986],
            zoom_start=11,
            min_zoom=10,
            max_zoom=14
        )

    def add_features(self, df):       
        style_function = lambda x: {
            'fillColor': '#FFFFFF',
            'color': '#000000',
            'fillOpacity': 0.1,
            'weight': 0.1
        }
        highlight_function = lambda x: {
            'fillColor': '#000000',
            'color': '#000000',
            'fillOpacity': 0.50,
            'weight': 0.1
        }
        NIL = folium.features.GeoJson(
            data=df,
            style_function=style_function,
            control=False,
            highlight_function=highlight_function,
            tooltip=folium.features.GeoJsonTooltip(
                fields=['법정동', '거래금액'],
                aliases=['지역', '평균 거래금액'],
                style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
            )
        )
        self.sample_map.add_child(NIL)
        self.sample_map.keep_in_front(NIL)

    def plot_map(self, df):
        folium.Choropleth(
            geo_data=df,
            data=df,
            columns=['법정동', '거래금액'],
            key_on="feature.properties.법정동",
            fill_color='YlGnBu',
            fill_opacity=0.8,
            line_opacity=0.6,
            line_color='#1B9C85',
            legend_name="Per 10,000 KRW",
            smooth_factor=0,
            Highlight=True,
            name="2020-2023 Average Apartment Prices per 10,000 KRW",
            show=True,
            overlay=True,
            nan_fill_color="White",
            threshold_scale=[0, 60000, 110000, 160000, 210000, 260000, 310000, 360000, 410000]
        ).add_to(self.sample_map)

        self.add_features(df)

    def display_map(self):
        return self.sample_map
    
def main(df):
    map_plotter = HousingMapPlotter()
    map_plotter.plot_map(df)
    sample_map = map_plotter.display_map()
    return sample_map