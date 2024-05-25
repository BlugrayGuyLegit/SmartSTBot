import discord

custom_status = "BlugrayGuy.com"

async def set_custom_status(client):
    await client.change_presence(activity=discord.Game(name=custom_status))

# Exécution du gestionnaire de statut
client = discord.Client()
client.loop.create_task(set_custom_status(client))
client.run('TOKEN')
