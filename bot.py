import discord
from discord.ext import commands
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import os

# Configuration du bot Discord
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Configuration de ChatterBot
chatbot = ChatBot(
    'GToiletBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "Hmm, I'm not sure I understand. Could you rephrase?",
            'maximum_similarity_threshold': 0.90
        },
        {
            'import_path': 'responses.GToiletAdapter',
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Entraîner ChatterBot avec des données de corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')  # Entraîner avec des corpus anglais

# Événement lorsque le bot Discord est prêt
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Événement pour répondre aux messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Vérifier si le message mentionne le bot ou répond au bot
    if bot.user.mentioned_in(message) or message.reference:
        # Obtenir le message précédent de l'utilisateur
        previous_message = await message.channel.fetch_message(message.reference.message_id) if message.reference else None
        user_input = previous_message.content if previous_message else message.content
        
        # Obtenir la réponse de ChatterBot en fonction de l'entrée de l'utilisateur
        response = chatbot.get_response(user_input)
        
        # Envoyer la réponse de ChatterBot dans le même canal Discord
        await message.channel.send(response)

# Récupérer le token du bot à partir de GitHub secret
discord_token = os.getenv('DISCORD_BOT_TOKEN')

# Démarrer le bot Discord
bot.run(discord_token)
