import discord
import os
from googlesearch import search
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.default()  # Crée les intents par défaut
intents.message_content = True       # Active l'intent pour lire le contenu des messages
intents.presences = True             # Active l'intent pour suivre les présences des membres
intents.members = True               # Active l'intent pour suivre les membres (nécessaire pour certaines actions)

client = discord.Client(intents=intents)  # Passe les intents au client Discord

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if client.user in message.mentions:  # Si le bot est mentionné
        query = message.content.replace(f'@{client.user.name}', '').strip()
        
        if query:
            await message.channel.send("Let me check that for you...")
            
            # Effectuer une recherche Google
            search_results = search(query, num_results=5)
            
            for url in search_results:
                try:
                    # Obtenir le contenu de la page
                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    # Extraire le texte de la page (simplement les paragraphes pour cet exemple)
                    paragraphs = soup.find_all('p')
                    if paragraphs:
                        # Envoyer les premières lignes de la première page trouvée
                        await message.channel.send(f"Here is what I found:\n\n{paragraphs[0].text[:500]}...\n\nSource: {url}")
                        return
                except Exception as e:
                    print(f"Error processing {url}: {e}")
            
            await message.channel.send("I couldn't find a good answer, sorry!")

client.run(os.getenv('DISCORD_BOT_TOKEN'))
