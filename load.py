import pandas as pd
import folium
from geopy.geocoders import Nominatim


def main_load():
    df = pd.read_csv('transformed_data.csv')
    m = folium.Map()
    geolocator = Nominatim(user_agent="myGeocoder")
    for index, row in df.iterrows():
        location = geolocator.geocode(row['city'])
        lat = location.latitude
        lon = location.longitude
        temp = row['temperature']
        folium.Marker([lat, lon], popup=f"temperature: {temp}").add_to(m)



    m.save("map.html")

main_load()