import discord
import os
from googlesearch import search
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True

client = discord.Client(intents=intents)

# Liste des sites que le bot peut détecter
site_keywords = {
    'youtube': 'YouTube',
    'spotify': 'Spotify',
    'twitter': 'Twitter',
    'instagram': 'Instagram',
    'wikipedia': 'Wikipedia',
    'facebook': 'Facebook',
    'twitch': 'Twitch',
    'reddit': 'Reddit'
}

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if client.user in message.mentions:
        query = message.content.replace(f'@{client.user.name}', '').strip().lower()
        
        if query:
            await message.channel.send("Let me check that for you...")
            
            site_to_search = None
            
            # Détection du site dans la requête
            for keyword in site_keywords:
                if keyword in query:
                    site_to_search = site_keywords[keyword]
                    query = query.replace(keyword, '').strip()
                    break
            
            if site_to_search:
                search_query = f"{query} site:{site_to_search.lower()}.com"
                search_results = list(search(search_query, num_results=5))  # Convertir le générateur en liste
                
                if search_results:
                    await message.channel.send(f"Here's the {site_to_search} link I found for '{query}': {search_results[0]}")
                else:
                    await message.channel.send(f"Sorry, I couldn't find any {site_to_search} results for '{query}'.")
            else:
                # Si aucun site spécifique n'est détecté, on effectue une recherche générale
                search_results = list(search(query, num_results=5))  # Convertir le générateur en liste
                
                if search_results:
                    await handle_general_result(search_results[0], message)
                else:
                    await message.channel.send("I couldn't find a good answer, sorry!")

async def handle_general_result(url, message):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        if paragraphs:
            await message.channel.send(f"Here is what I found:\n\n{paragraphs[0].text[:500]}...\n\nSource: {url}")
    except Exception as e:
        print(f"Error processing {url}: {e}")
        await message.channel.send("I couldn't find a good answer, sorry!")

client.run(os.getenv('DISCORD_BOT_TOKEN'))
