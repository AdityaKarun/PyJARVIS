# Import required libraries
import os
import requests
from dotenv import load_dotenv
from modules.location import get_location

# Load environment variables from .env file
load_dotenv()

def get_weather():
    """
    Gets current weather information for the user's location using WeatherAPI.
    
    Returns:
        str: Weather report including temperature, conditions, and wind speed,
             or an error message if the weather data cannot be fetched
    """
    try:
        # Get API key from environment variables
        WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

        city = get_location()

        if not city:
            return "Could not determine your location for weather report."

        response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}")
        weather_data = response.json()

        condition = weather_data["current"]["condition"]["text"]
        temperature = weather_data["current"]["temp_c"]
        wind_speed = weather_data["current"]["wind_kph"]

        weather_report = (
            f"Currently in {city}, it's {condition} with a temperature of "
            f"{temperature} degree Celsius and wind speed of {wind_speed} kilometers per hour."
        )

        return weather_report
    
    except Exception as e:
        return f"Could not fetch weather data: {e}"

if __name__ == "__main__":
    print("Weather Report...")
    weather_report = get_weather()
    print(weather_report)