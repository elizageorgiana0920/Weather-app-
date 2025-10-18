import requests


API_KEY = "50e676d55260bd863b6e46249f0226ef"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\n🌍  Weather in \033[1;36m{city.capitalize()}\033[0m:")
        print(f"☁️  Description: \033[1;33m{weather}\033[0m")
        print(f"🌡️  Temperature: \033[1;31m{temp}°C\033[0m")
        print(f"💧  Humidity: \033[1;34m{humidity}%\033[0m")
        print(f"🌬️  Wind speed: \033[1;35m{wind_speed} m/s\033[0m\n")
    else:
        print("❌ City not found or invalid API key.\n")



print("🌦️  Simple Weather App (Console version)")
city = input("Enter a city name: ")
get_weather(city)
