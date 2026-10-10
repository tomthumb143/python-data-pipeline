
import json
from weather_api import get_weather

def main():
    data = get_weather()
   # print(json.dumps(data, indent=4))
    dates = data["daily"]["time"]
    temps = data["daily"]["temperature_2m_max"]

    for date, temp in zip(dates, temps):
        print(date, temp)




if __name__ == "__main__":
    main()