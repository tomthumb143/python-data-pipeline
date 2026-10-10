import requests

def get_weather ():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
            "latitude" : 53.48,
            "longitude" : -2.24,
            "daily" : "temperature_2m_max,temperature_2m_min",
            "timezone" : "Europe/London"

    }

    response = requests.get(url, params=params, timeout=10)

    response.raise_for_status()

    return response.json()