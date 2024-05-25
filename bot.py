import discord
import requests
from bs4 import BeautifulSoup
import os
import asyncio

# Configuration
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
URLS_TO_MONITOR = [
    'https://blugrayguylegit.github.io/Blugray/',  
    'https://dafuqboom.shop/'   
]

if not TOKEN or not CHANNEL_ID:
    raise ValueError("TOKEN and CHANNEL_ID must be set")

# Create an instance of a Client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Function to get the content of a webpage
def get_page_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.get_text()  # Or any specific part of the page you want to monitor

async def monitor_pages():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)

    while not client.is_closed():
        for index, url in enumerate(URLS_TO_MONITOR):
            # Get the previous content from a local file
            try:
                with open(f'previous_content_{index}.txt', 'r') as file:
                    previous_content = file.read()
            except FileNotFoundError:
                previous_content = ''

            # Get the current content of the page
            current_content = get_page_content(url)

            # Compare the content and send a message if there is an update
            if current_content != previous_content:
                await channel.send(f'The page at {url} has been updated.')

                # Update the previous content file
                with open(f'previous_content_{index}.txt', 'w') as file:
                    file.write(current_content)

        await asyncio.sleep(300)  # Wait for 5 minutes before checking again

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    client.loop.create_task(monitor_pages())

client.run(TOKEN)
