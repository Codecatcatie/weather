import requests
import sqlite3
import os

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env

API_KEY = os.getenv('API_KEY')

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main():
    while True:
        city = input("Enter the city name (or Q for exit): ")
        if city == 'Q':
            break 
        weather_data = get_weather(city)

        if weather_data:
            print(f"City: {weather_data['name']}")
            print(f"Temperature: {weather_data['main']['temp']}°C")
            print(f"Weather: {weather_data['weather'][0]['description']}")
        else:
            print("City not found or API request failed.")

if __name__ == "__main__":
    main()
    