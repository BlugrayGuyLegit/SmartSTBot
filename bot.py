import discord
from status_manager import set_custom_status

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    client.loop.create_task(set_custom_status(client))

client.run(os.getenv('DISCORD_BOT_TOKEN'))
