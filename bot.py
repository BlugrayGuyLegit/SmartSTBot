import os
import discord
import requests

# Discord configuration
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

# Wit.ai configuration
WIT_AI_TOKEN = "WH74G7K3UI4NCVC5M5M5PLAB2HEBIUKW"
WIT_AI_API_URL = "https://api.wit.ai/message?v=20240712&q="

# Event: Bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

# Event: Message received
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if client.user.mentioned_in(message) or (message.reference and message.reference.resolved):
        # Call Wit.ai to understand the message
        response = wit_ai_request(message.content)
        
        # Respond based on Wit.ai response
        if response:
            await message.channel.send(response)
        else:
            await message.channel.send("Sorry, I don't understand.")
    
    # Additional message handling logic can be added here

# Function to call Wit.ai API
def wit_ai_request(message):
    headers = {
        'Authorization': f'Bearer {WIT_AI_TOKEN}',
        'Content-Type': 'application/json'
    }
    params = {
        'q': message
    }
    response = requests.get(WIT_AI_API_URL, headers=headers, params=params)
    data = response.json()
    
    # Retrieve Wit.ai intent name
    if 'intents' in data and data['intents']:
        return data['intents'][0]['name']
    else:
        return None

# Run the Discord bot
client.run(os.getenv('DISCORD_BOT_TOKEN'))
