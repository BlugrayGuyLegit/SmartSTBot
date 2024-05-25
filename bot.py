import discord
from googleapiclient.discovery import build
import requests
from bs4 import BeautifulSoup
import os
import asyncio
from status_manager import set_custom_status  # Importez le gestionnaire de statut

intents = discord.Intents.default()
client = discord.Client(intents=intents)

client.loop.create_task(set_custom_status())

# Configuration
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
CHANNEL_ID_YOUTUBE = 'UCsSsgPaZ2GSmO6il8Cb5iGA'
URL_TO_MONITOR = 'https://dafuqboom.shop'

if not TOKEN or not CHANNEL_ID or not YOUTUBE_API_KEY or not CHANNEL_ID_YOUTUBE:
    raise ValueError("TOKEN, CHANNEL_ID, YOUTUBE_API_KEY, and CHANNEL_ID_YOUTUBE must be set")

# Create an instance of a Client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Function to get the content of a webpage
def get_page_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.get_text()  # Or any specific part of the page you want to monitor

# Function to get the latest video from a YouTube channel
def get_latest_video():
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    request = youtube.search().list(
        part='snippet',
        channelId=CHANNEL_ID_YOUTUBE,
        order='date',
        type='video'
    )
    response = request.execute()
    return response['items'][0] if response['items'] else None

async def check_new_content():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)

    while not client.is_closed():
        # Check for new video on YouTube channel
        latest_video = get_latest_video()
        if latest_video:
            video_title = latest_video['snippet']['title']
            video_link = f"https://www.youtube.com/watch?v={latest_video['id']['videoId']}"
            await channel.send(f"New video uploaded: {video_title}\n{video_link}")

        # Check for updates on the website
        current_content = get_page_content(URL_TO_MONITOR)
        try:
            with open('previous_content.txt', 'r') as file:
                previous_content = file.read()
        except FileNotFoundError:
            previous_content = ''
        
        if current_content != previous_content:
            await channel.send(f"The website at {URL_TO_MONITOR} has been updated.")
            with open('previous_content.txt', 'w') as file:
                file.write(current_content)

        await asyncio.sleep(300)  # Wait for 5 minutes before checking again

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    client.loop.create_task(check_new_content())
    client.loop.create_task(set_custom_status(client))  # Start custom status manager

client.run(TOKEN)
