import discord
import os
import random

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

    

# Liste de salutations possibles
greetings = [
    'hello', 'hi', 'hey', 'sup', 'yo', 'howdy', 'hola', 'bonjour', 'salut', 'greetings',
    'hiya', 'whatsup', 'what\'s up', 'good day', 'gday', 'how\'s it going', 'how are you'
]

# Liste de réponses aux salutations
greeting_responses = [
    'Hi {user}!', 'Hello {user}, how are you?', 'Hey {user}!', 'Yo {user}!', 'What\'s up {user}?',
    'Howdy {user}!', 'Hola {user}!', 'Bonjour {user}!', 'Salut {user}!', 'Greetings {user}!'
]

# Liste de réponses positives et négatives
positive_responses = ['good', 'fine', 'great', 'well', 'okay', 'ok']
negative_responses = ['bad', 'not good', 'terrible', 'sad', 'awful']

@client.event
async def on_message(message):
    # Ignorer les messages du bot lui-même
    if message.author == client.user:
        return

    # Vérifier si le message commence par une salutation
    if any(message.content.lower().startswith(greeting) for greeting in greetings):
        response = random.choice(greeting_responses).format(user=message.author.name)
        await message.channel.send(response)
        return
    
    # Vérifier les réponses aux questions "how are you" ou similaires
    if 'how are you' in message.content.lower():
        def check(m):
            return m.author == message.author and m.channel == message.channel

        # Attendre la réponse de l'utilisateur
        try:
            reply = await client.wait_for('message', check=check, timeout=30.0)
            if any(word in reply.content.lower() for word in positive_responses):
                await message.channel.send('I\'m glad to hear that!')
            elif any(word in reply.content.lower() for word in negative_responses):
                await message.channel.send('I\'m sorry to hear that.')
            else:
                await message.channel.send('Thanks for sharing!')
        except asyncio.TimeoutError:
            await message.channel.send('It seems like you didn\'t respond in time.')

async def send_message(channel_id, content):
    channel = client.get_channel(int(channel_id))
    if channel:
        await channel.send(content)
    else:
        print(f"Channel with ID {channel_id} not found.")

client.run(os.getenv('DISCORD_BOT_TOKEN'))
