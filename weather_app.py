import requests

API_KEY = '42efff0a984b3df5e92492f07988d7c7'  # Replace with your actual API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(location):
    try:
        response = requests.get(BASE_URL, params={
            'q': location,
            'appid': API_KEY,
            'units': 'metric'  # Use 'imperial' for Fahrenheit
        })
        data = response.json()
        
        if data['cod'] == 200:
            city = data['name']
            country = data['sys']['country']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            weather_desc = data['weather'][0]['description']

            print(f"Weather in {city}, {country}:")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {weather_desc.capitalize()}")
        else:
            print(f"Error: {data['message']}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    location = input("Enter a city name or ZIP code: ")
    get_weather(location)
