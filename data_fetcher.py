# data_fetcher.py
import requests

class DataFetcher:
    def __init__(self,api_key,city):
        self.api_key = api_key
        self.city = city

    def fetch_weather(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        try:
            if response.status_code == 200:
                data = response.json()
                print(data)
                # temperature = data['main']['temp']
                # weather_description = data['weather'][0]['description']
                return data
        except:
            print("Cannot Get Response")
            return None, None

