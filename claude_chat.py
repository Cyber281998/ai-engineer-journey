import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

print("Chat with Claude! Type 'quit' to exit.\n")

conversation = []

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    
    conversation.append({
        "role": "user",
        "content": user_input
    })
    
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=conversation
    )
    
    reply = message.content[0].text
    
    conversation.append({
        "role": "assistant", 
        "content": reply
    })
    
    print(f"\nClaude: {reply}\n")