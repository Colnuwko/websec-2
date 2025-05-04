import operator

import requests
key = "6372c732-186c-4529-8697-aeae19ad3de5"
YANDEX_API_URL = "https://api.rasp.yandex.net/v3.0/"
response = requests.get(f"{YANDEX_API_URL}stations_list/?apikey={key}&lang=ru_RU&format=json")

def get_stations(pick_country: str):
    all_stations = response.json()['countries']
    stations = []
    for country in all_stations:
        if country['title'] == pick_country: # выбираем поезда из выбранной страны
            for station_in_country in country['regions']: # пробегаекмся по всем регионам
                for station_in_settlements in station_in_country['settlements']: # пробегаекмся по всем населенным пунктам
                    for station in station_in_settlements['stations']: # пробегаекмся по всем станциям в населенном пункте
                        if station['transport_type'] in ['suburban', 'train']: # ну нет тут в списке этих электричек(((
                            stations.append({'code': station['codes']['yandex_code'], 'title': station['title']})
    stations = sorted(stations, key=lambda station: station['title'])
    return stations

def get_countries():
    countries = []
    for country in response.json()['countries']:
        if country['codes'] == {}:
            continue
        countries.append({'code': country['codes']['yandex_code'], 'title': country['title']})
    countries = sorted(countries, key=lambda item: item['title'])
    print(countries)
    return countries
