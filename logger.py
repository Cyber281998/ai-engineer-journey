import requests
import json
from datetime import datetime

def get_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    data = response.json()
    return data["value"]

def save_joke(joke):
    log = {
        "timestamp": str(datetime.now()),
        "joke": joke
    }
    with open("jokes_log.json", "a") as f:
        f.write(json.dumps(log) + "\n")
    print("Joke saved to jokes_log.json")

joke = get_joke()
print(joke)
save_joke(joke)