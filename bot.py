import discord
import os
import openai
import asyncio
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Configurer les clés API à partir des variables d'environnement
discord_token = os.getenv('DISCORD_BOT_TOKEN')
openai.api_key = os.getenv('OPENAI_API_KEY')

intents = discord.Intents.default()
intents.presences = True
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Vérifier si le message contient le mot "time"
    if 'time' in message.content.lower():
        await message.channel.send('Insérez ici votre réponse pour l\'heure à Washington, D.C.')

    # Utiliser l'API OpenAI pour répondre à tout autre message
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message.content,
        max_tokens=150
    )
    await message.channel.send(response.choices[0].text.strip())

async def send_message(channel_id, content):
    channel = client.get_channel(int(channel_id))
    if channel:
        await channel.send(content)
    else:
        print(f"Channel with ID {channel_id} not found.")

client.run(discord_token)
