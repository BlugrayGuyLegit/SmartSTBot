import discord
import random

# List of custom statuses
statuses = [
    "BlugrayGuy.com",
    "Smart Bot",
    "Check boom's social every time",
    "24/7 bot"
]

async def set_custom_status(client):
    while True:
        # Choose a random status from the list
        status = random.choice(statuses)
        # Set the bot's status
        await client.change_presence(activity=discord.Game(name=status))
        # Wait for an hour before changing the status again
        await asyncio.sleep(5)