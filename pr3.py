import random
from enum import Enum


class TemperatureUnit(Enum):
    Celsius = 'C'
    Fahrenheit = 'F'
    Kelvin = 'K'

cities = {
    "Абакан": random.randint(-30, 40),
    "Сорск": random.randint(-30, 40),
    "Усть-Абакан": random.randint(-30, 40),
    "Таштып": random.randint(-30, 40),
    "Боград": random.randint(-30, 40),
    "Копьёво": random.randint(-30, 40),
    "Абаза": random.randint(-30, 40),
    "Черногорск": random.randint(-30, 40),
}


def get_temperature(city):
    celsius = cities[city]
    fahrenheit = celsius * 9/5 + 32
    kelvin = celsius + 273.15
    return [round(celsius, 1), round(fahrenheit, 1), round(kelvin, 2)]


def filter_cities(temp_sign):
    return list(filter(lambda city: (temp_sign == '+' and cities[city] > 0) or 
                       (temp_sign == '-' and cities[city] < 0), cities.keys()))


def sort_cities(order='asc'):
    return sorted(cities.items(), key=lambda x: x[1], reverse=(order == 'desc'))


def display_weather(city):
    temp = get_temperature(city)
    return [f"{temp[0]}{TemperatureUnit.Celsius.value}", f"{temp[1]}{TemperatureUnit.Fahrenheit.value}", f"{temp[2]}{TemperatureUnit.Kelvin.value}"]


if __name__ == "__main__":
    city_name = input("Введите название города (например, 'Абакан'): ")
    if city_name in cities:
        print(f"Погода в {city_name}: {display_weather(city_name)}")
    else:
        print("Город не найден.")

    sign = input("Введите фильтрацию по температуре ('+' или '-'): ")
    filtered_cities = filter_cities(sign)
    city_weather_data = list(map(lambda city: [city, cities[city], TemperatureUnit.Celsius.value], filtered_cities))
    print(f"Города с температурой {sign} нуля: {city_weather_data}")

    sort_order = input("Введите сортировку по температуре ('asc' для возрастания или 'desc' для убывания): ")
    sorted_cities = sort_cities(sort_order)
    print(f"Отсортированные города: {sorted_cities}")