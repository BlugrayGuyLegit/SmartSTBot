import os
import discord
import requests

# Configuration de Discord
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

# Configuration de Wit.ai
WIT_AI_TOKEN = "WH74G7K3UI4NCVC5M5M5PLAB2HEBIUKW"
WIT_AI_API_URL = "https://api.wit.ai/message?v=20240712&q="

# Événement de connexion du bot
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

# Événement de réception de message sur Discord
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Appel à Wit.ai pour comprendre le message
    response = wit_ai_request(message.content)
    
    # Récupérer la réponse de Wit.ai
    if response:
        await message.channel.send(response)

# Fonction pour appeler l'API Wit.ai
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
    
    # Récupérer la réponse de Wit.ai
    if 'intents' in data and data['intents']:
        return data['intents'][0]['name']
    else:
        return "Désolé, je ne comprends pas."

# Démarrer le bot Discord
client.run(os.getenv('DISCORD_BOT_TOKEN'))
