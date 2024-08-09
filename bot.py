import discord
import os
import random
import asyncio
from datetime import datetime
import pytz
from skibidi_qr import ask_skibidi_question, get_skibidi_response  # Importation du module Skibidi
from unknown_responses import get_unknown_response  # Importation du module des réponses "I don't know"

intents = discord.Intents.default()
intents.presences = True
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'say: Hey @{client.user.name}'))
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Vérifier si le message correspond à une question sur Skibidi Toilet
    if 'skibidi' in message.content.lower():
        question = ask_skibidi_question()
        await message.channel.send(f'{question}')
        
        # Optionnel : Attendre la réponse de l'utilisateur et répondre
        try:
            def check(m):
                return m.author == message.author and m.channel == message.channel

            reply = await client.wait_for('message', check=check, timeout=30.0)
            response = get_skibidi_response(reply.content)
            
            if response:
                await message.channel.send(response)
            else:
                await message.channel.send(get_unknown_response())  # Réponse "I don't know" si aucune réponse n'est trouvée

        except asyncio.TimeoutError:
            await message.channel.send('It seems like you didn\'t respond in time.')
        return
    
    # (Autres vérifications pour "dead chat", "bro im ded", etc.)
    # (Le reste de ton script continue ici...)

    # Si le bot n'a pas de réponse spécifique, utiliser une réponse "I don't know"
    await message.channel.send(get_unknown_response())

client.run(os.getenv('DISCORD_BOT_TOKEN'))
