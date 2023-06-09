import json
import time

import requests

    # read the file cities.json and returns its content.
    # Example: this function should return ["Algiers", "Batna", "Tamanrasset"]
def get_list_of_cities():
    # Ouvrir le fichier en mode lecture
    with open('cities.json', 'r') as file:
    # Charger les données JSON à partir du fichier
        data = json.load(file)
        # Maintenant, vous pouvez accéder aux données du fichier JSON
        # et les utiliser selon vos besoins
        return data  

def get_lat_lon(city):
    # get latitude and longitude data of cities in Algeria 
    # using the API documented here: https://nominatim.org/release-docs/latest/api/Search/
    # Example: this function should return 36.6875, 3.125
    url = f"https://nominatim.openstreetmap.org/search?city={city}&country=Algeria&format=json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        
        if data:
            # Récupérer les coordonnées de la première entrée dans les résultats
            longitude = data[0]['lon']
            latitude = data[0]['lat']
            
            return latitude , longitude
        else:
            print("Aucun résultat trouvé.")
    else:
        print("La requête a échoué avec le code d'état :", response.status_code)
    

def get_current_weather(lat, lon):
    # get current weather data at (latitude, longitude)
    # using the API documented here: https://open-meteo.com/
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    response =requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
       
    else:
        print("The request failed with status code:", response.status_code)




def get_weather_all_cities(cities):
    data = dict()
    for city in cities:
        lat, lon = get_lat_lon(city)
        
        res = get_current_weather(lat, lon)
        data[city] = res
        
    return data

def save_output_data(data_):
    unix_timestamp = int(time.time())
    output_filename = f"raw_data_{unix_timestamp}.json"
    with open(output_filename, "w") as f:
        json.dump(data_, f)

def main_extract():
    cities = get_list_of_cities()
    print(cities)
    weather_data = get_weather_all_cities(cities)
    print(weather_data)
    save_output_data(weather_data)

main_extract()