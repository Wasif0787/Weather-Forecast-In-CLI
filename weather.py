import requests
import json
import argparse

API_KEY = "d42c7d390414490323589822ed7b2094"  

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def display_weather(data):
    if data["cod"] == "404":
        print("City not found.")
    else:
        temperature = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        print(f"Weather: {weather_desc}")
        print(f"Temperature: {temperature}°C")

def main():
    parser = argparse.ArgumentParser(description="Get current weather forecast for a city")
    parser.add_argument("city", help="Name of the city")
    args = parser.parse_args()
    city = args.city

    weather_data = get_weather(city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
