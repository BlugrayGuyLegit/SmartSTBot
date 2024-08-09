import random

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
