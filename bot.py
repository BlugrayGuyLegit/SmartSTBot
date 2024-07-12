import os
import discord
import requests

# Discord configuration
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

# Wit.ai configuration
WIT_AI_TOKEN = "PEQZ6JKGNRTNJUDGV6GQBEABT4JEI6UJ"
WIT_AI_API_URL = "https://api.wit.ai/message?v=20240712&q=bot"

# Bot ready event
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

# Message received event on Discord
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if client.user.mentioned_in(message) or (message.reference and message.reference.resolved):
        # Calling Wit.ai to understand the message
        response = wit_ai_request(message.content)
        
        # Respond based on Wit.ai response
        if response:
            await message.channel.send(response)
        else:
            await message.channel.send("Sorry, I don't understand.")

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
    
    # Check if Wit.ai recognized any intents
    if 'intents' in data and data['intents']:
        return data['intents'][0]['name']
    else:
        return None

# Start the Discord bot
client.run(os.getenv('DISCORD_BOT_TOKEN'))
