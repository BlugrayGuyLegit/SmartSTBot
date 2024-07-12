import discord
import socket

# Configuration du bot Discord
client = discord.Client()

# Configuration de la connexion à ChatScript
HOST = 'localhost'  # Adresse IP du serveur ChatScript
PORT = 1024          # Port utilisé par le serveur ChatScript

def chat_with_chatscript(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(message.encode())
        response = s.recv(1024).decode()
        return response

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Envoyer le message à ChatScript et recevoir la réponse
    chat_response = chat_with_chatscript(message.content)
    await message.channel.send(chat_response)

# Exécuter le bot Discord avec le token approprié
client.run('DISCORD_BOT_TOKEN')
