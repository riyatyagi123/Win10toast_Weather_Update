from win10toast import ToastNotifier
import requests
import os
import time
from datetime import datetime

toaster = ToastNotifier()

user_api = os.environ.get('wheather1')  
location = "Rajasthan"

while True:
    try:
       
        complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()

        if api_data['cod'] != 200:
            print("Error fetching weather data:", api_data.get("message", "Unknown error"))
            break  

        temp_city = api_data['main']['temp'] - 273.15  # Convert Kelvin to Celsius
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        print("-------------------------------------------------------------")
        print(f"Weather Stats for - {location.upper()}  || {date_time}")
        print("-------------------------------------------------------------")
        print(f"Current temperature is: {temp_city:.2f}°C")
        print(f"Current weather desc  : {weather_desc}")
        print(f"Current Humidity      : {hmdt}%")
        print(f"Current wind speed    : {wind_spd} km/h")

        toaster.show_toast(
            "Weather Update",
            f"Temp: {temp_city:.2f}°C\nWeather: {weather_desc}\nHumidity: {hmdt}%\nWind: {wind_spd} km/h",
            threaded=True,
            duration=10 
        )
        time.sleep(1800)  

    except Exception as e:
        print("An error occurred:", str(e))
        break  
