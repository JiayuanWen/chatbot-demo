import requests
import os
from dotenv import load_dotenv

load_dotenv()

owm_key = os.getenv('OWM_API')

def get_weather_desc(location: str) -> str:
    """
    Retrieve and format the current weather description for a given location.

    Args:
        location (str): The city or location for which to retrieve the weather.

    Returns:
        str: A formatted string containing the current weather status, temperature, wind speed, and other relevant information.
    """
    try:
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={owm_key}&units=metric')
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        result = response.json()

        weather = result['weather'][0]['main']
        wind = result['wind']['speed']
        wind_f = result['wind']['speed'] * 2.23694
        temperature = result['main']['temp']
        temperature_f = (temperature * 9/5) + 32
        temperature_min = result['main']['temp_min']
        temperature_min_f = (temperature_min * 9/5) + 32
        temperature_max = result['main']['temp_max']
        temperature_max_f = (temperature_max * 9/5) + 3

        result_string: str = f"Weather status: {weather}, Temperature is {temperature} °C ({temperature_f} °F) with expected minimum of {temperature_min} °C ({temperature_min_f} °F) and maximum of {temperature_max} °C ({temperature_max_f} °F), Wind speed is {wind} m/s ({round(wind_f, 2)} mph)" 

        return result_string
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return "Cannot fetch weather data at the moment"
    except requests.exceptions.RequestException as req_err:
        print(f'Request error occurred: {req_err}')
        return "Cannot fetch weather data at the moment"