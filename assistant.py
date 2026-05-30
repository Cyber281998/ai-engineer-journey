import anthropic
import requests
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    data = response.json()
    temp = data["current_condition"][0]["temp_C"]
    feels_like = data["current_condition"][0]["FeelsLikeC"]
    description = data["current_condition"][0]["weatherDesc"][0]["value"]
    return f"{description}, {temp}°C, feels like {feels_like}°C"

def get_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    data = response.json()
    return data["value"]

def build_system_prompt():
    sydney_weather = get_weather("Sydney")
    joke = get_joke()
    
    return f"""You are a helpful personal assistant for Khoa, an IT engineer in Sydney learning AI engineering.

You have access to real-time information:
- Current Sydney weather: {sydney_weather}
- Today's Chuck Norris fact: {joke}

Use this information naturally when relevant. Be concise and practical.
When Khoa asks about weather, use the real data above.
When Khoa needs motivation, use the Chuck Norris fact creatively."""

def chat():
    print("Your Personal AI Assistant is ready!")
    print("Try asking about weather, or anything else.\n")
    print("Type 'quit' to exit.\n")
    
    system_prompt = build_system_prompt()
    conversation = []
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "quit":
            print("Goodbye Khoa!")
            break
        
        conversation.append({
            "role": "user",
            "content": user_input
        })
        
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            system=system_prompt,
            messages=conversation
        )
        
        reply = message.content[0].text
        
        conversation.append({
            "role": "assistant",
            "content": reply
        })
        
        print(f"\nAssistant: {reply}\n")

chat()