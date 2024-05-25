import discord
import random
import asyncio

# List of custom statuses
statuses = "Look at the DaFuq!?Boom! Social"

async def set_custom_status(client):
    while True:
        # Choose a random status from the list
        status = random.choice(statuses)
        # Set the bot's status
        await client.change_presence(activity=discord.Game(name=status))
        # Wait for 3 seconds before changing the status again
        await asyncio.sleep(60)
