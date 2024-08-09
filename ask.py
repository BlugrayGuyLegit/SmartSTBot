import random

# Liste de déclencheurs pour "dead chat"
dctriggers = [':dead_chat:', '# DEAD CHAT', 'dead chat', 'chat is ded', 'dead general']

bye = ['bye', 'goodbye', 'cia', 'ciao', 'seya', 'seeya', 'syl', 'ttyl', 'see you later', 'talk to you later']

gn = ['gn', 'goodnight', 'good night']

# Liste de déclencheurs pour "bro im ded"
broimded = [':bro_im_ded:', 'Bro im dead', 'bro im ded', 'im dead', 'im ded', 'bro is ded', 'bro is dead']

# Liste de salutations possibles
greetings = [
    'hello', 'hi', 'hey', 'sup', 'yo', 'howdy', 'hola', 'bonjour', 'salut', 'greetings',
    'hiya', 'whatsup', 'what\'s up', 'good day', 'gday', 'how\'s it going', 'how are you'
]

# Liste de réponses aux salutations
greeting_responses = [
    'Hi {user}!', 'Hello {user}, how are you?', 'Hey {user}!', 'Yo {user}!', 'What\'s up {user}?',
    'Howdy {user}!', 'Hola {user}!', 'Hey there {user}!', 'Sup {user}!', 'Greetings {user}!'
]

# Liste de réponses positives et négatives
positive_responses = ['good', 'fine', 'great', 'well', 'okay', 'ok']
negative_responses = ['bad', 'not good', 'terrible', 'sad', 'awful']

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Vérifier si le message correspond à un déclencheur de "dead chat"
    if any(trigger in message.content.lower() for trigger in dctriggers):
        await message.channel.send('I agree with your opinion, someone needs to revive the chat to keep it alive...')
        return

    # Vérifier si le message correspond à un déclencheur de "bro im ded"
    if any(trigger in message.content.lower() for trigger in broimded):
        await message.channel.send('/revive')
        return

    if any(trigger in message.content.lower() for trigger in gn):
        await message.channel.send('goodnight!')
        return

    if any(trigger in message.content.lower() for trigger in bye):
        await message.channel.send('bye, see you later!')
        return

    # Vérifier si le message commence par une salutation
    if any(message.content.lower().startswith(greeting) for greeting in greetings):
        response = random.choice(greeting_responses).format(user=message.author.name)
        await message.channel.send(response)
        return
    
    # Vérifier si le message contient le mot "time"
    if 'time' in message.content.lower():
        timezone = pytz.timezone('America/New_York')  # Fuseau horaire de Washington, D.C.
        current_time = datetime.now(timezone).strftime('%H:%M:%S')
        await message.channel.send(f'The current time is {current_time} in Washington, D.C. (ET)')
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

    # Liste de questions/réponses spécifiques à Skibidi Toilet
    skibidi_questions = [
    "What is Skibidi Toilet?",
    "Who is the main character in Skibidi Toilet?",
    "What are the Skibidi Toilets fighting against?",
    "How did the Skibidi Toilet meme start?",
    "Is Skibidi Toilet a game or a video series?",
    "Where can I watch Skibidi Toilet?",
    "What is the Skibidi Bop Bop Dop meme?",
    "Why is Skibidi Toilet popular?",
    "Who created the Skibidi Toilet series?",
    "Are there different types of Skibidi Toilets?",
    "What is the story behind the Skibidi Toilet videos?",
    "Can you explain the Skibidi Toilet lore?",
]

skibidi_answers = {
    "What is Skibidi Toilet?": "Skibidi Toilet is a popular internet meme featuring a bizarre scenario involving toilets with human heads.",
    "Who is the main character in Skibidi Toilet?": "The main characters in the Skibidi Toilet series are typically the Skibidi Toilets themselves, often engaged in strange battles.",
    "What are the Skibidi Toilets fighting against?": "The Skibidi Toilets are often depicted fighting against other bizarre entities like Cameramen, TV Men, and other unusual beings.",
    "How did the Skibidi Toilet meme start?": "The meme started as a part of a video series on YouTube by DaFuq!?Boom!, which gained popularity due to its absurd and humorous content.",
    "Is Skibidi Toilet a game or a video series?": "Skibidi Toilet is primarily a video series that has spawned various memes and fan content.",
    "Where can I watch Skibidi Toilet?": "You can watch the Skibidi Toilet series on YouTube, where the original videos are posted.",
    "What is the Skibidi Bop Bop Dop meme?": "The Skibidi Bop Bop Dop meme is a related meme where a character performs a funny dance to a catchy tune.",
    "Why is Skibidi Toilet popular?": "Skibidi Toilet is popular due to its unique blend of humor, absurdity, and catchy music, which appeals to a wide audience.",
    "Who created the Skibidi Toilet series?": "The Skibidi Toilet series was created by a YouTuber named DaFuq!?Boom!",
    "Are there different types of Skibidi Toilets?": "Yes, there are various types of Skibidi Toilets depicted in the series, each with different characteristics.",
    "What is the story behind the Skibidi Toilet videos?": "The story behind the Skibidi Toilet videos is intentionally nonsensical and absurd, focusing on the chaotic world where these toilets exist.",
    "Can you explain the Skibidi Toilet lore?": "The Skibidi Toilet lore is not clearly defined, as the series focuses more on visual and absurd humor rather than a coherent story."
}

def get_skibidi_response(question):
    return skibidi_answers.get(question, "I'm not sure about that, but the Skibidi Toilet universe is full of surprises!")

def ask_skibidi_question():
    return random.choice(skibidi_questions)
