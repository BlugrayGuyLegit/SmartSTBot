import discord
import random
import asyncio

statuses = [
    "Looking the Boom's merch",
    "Looking the Boom's channel",
    "BlugrayGuy.com"
]

async def set_custom_status(client):
    while True:
        status = random.choice(statuses)
        await client.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(60) 
