import requests

def get_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    data = response.json()
    return data["value"]

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    data = response.json()
    temp = data["current_condition"][0]["temp_C"]
    feels_like = data["current_condition"][0]["FeelsLikeC"]
    description = data["current_condition"][0]["weatherDesc"][0]["value"]
    return temp, feels_like, description

def daily_briefing():
    city = input("Enter your city: ")
    print("\n--- YOUR DAILY BRIEFING ---\n")
    
    temp, feels_like, description = get_weather(city)
    print(f"Weather in {city}:")
    print(f"  Condition : {description}")
    print(f"  Temp      : {temp}°C")
    print(f"  Feels like: {feels_like}°C")
    
    print("\nChuck Norris fact of the day:")
    print(f"  {get_joke()}")
    print("\n---------------------------")

daily_briefing()