def get_city():
    city_name = input("Which city do you want weather for? ")
    while len(city_name) == 0:
       city_name = input("Please enter a city: ")
    return city_name

selected_city = get_city()
print(f'{selected_city} selected as city for weather.') 

