
import requests
import os
from dotenv import load_dotenv

load_dotenv()
APIKEY = os.environ['APIKEY']  # reads the environment variable
LAT = os.environ['LAT']  # reads the environment variable
LONG = os.environ['LONG']  # reads the environment variable

response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=" + LAT + "&lon=" + LONG + "&appid=" + APIKEY + "&units=metric")

print(response.status_code)
print(response.json())


