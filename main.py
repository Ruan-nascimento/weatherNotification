from flask import Flask
from dotenv import load_dotenv
import requests
import os

load_dotenv()
key = os.getenv("API_KEY")
baseUrl = os.getenv("BASE_URL")

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def mainFunction():
  params = {"q": "Rio de Janeiro", "appid": key, "units": "metric", "lang": "pt_br"}
  response = requests.get(baseUrl, params=params)

  return response.json()



if __name__ == "__main__":
  app.run(port=5000, debug=True)
