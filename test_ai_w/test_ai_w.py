import requests

class WeatherBot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"

    def get_weather(self, city):
        url = self.base_url.format(city, self.api_key)
        try:
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200:
                weather_description = data['weather'][0]['description']
                temperature = data['main']['temp']
                return f"Weather in {city.capitalize()}: {weather_description.capitalize()}. Temperature: {temperature}°C."
            else:
                return "Failed to retrieve weather data. Please try again later."
        except Exception as e:
            return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    # Load API key from a secure location
    api_key = "3fdc3805678c4a0aff81bc73245707aa" 
    weather_bot = WeatherBot(api_key)
    print("Hi, I'm Weather Bot.")
    while True:
        city = input("Enter the city name (in English) or 'exit' to quit: ")
        if city.lower() == "exit":
            print("Goodbye!")
            break
        elif city.strip() == "":
            print("Please enter a city name.")
            continue
        weather_info = weather_bot.get_weather(city)
        print(weather_info)
