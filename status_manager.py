import discord
import random
import asyncio

statuses = [
    "I reply to your hello !",
    "Powered by KeamsOS"
]

async def set_custom_status(client):
    while True:
        status = random.choice(statuses)
        await client.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(60) 
