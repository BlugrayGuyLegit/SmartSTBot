import discord
import os

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

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

async def send_message(channel_id, content):
    channel = client.get_channel(int(channel_id))
    if channel:
        await channel.send(content)
    else:
        print(f"Channel with ID {channel_id} not found.")

client.run(os.getenv('DISCORD_BOT_TOKEN'))
