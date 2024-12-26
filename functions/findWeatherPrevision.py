import os
from dotenv import load_dotenv
import requests

load_dotenv()
key = os.getenv("API_KEY")

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric&lang=pt-br"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "weather": data["weather"][0]["description"]
            }
        else:
            return {"error": "Cidade não encontrada ou erro na API."}
    except Exception as e:
        return {"error": str(e)}