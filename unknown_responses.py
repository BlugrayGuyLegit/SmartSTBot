import random

# Liste de réponses pour "I don't know"
unknown_responses = [
    "I don't know.",
    "I'm not sure about that.",
    "Sorry, I don't have an answer for you.",
    "I wish I knew!",
    "Hmm, I don't know the answer to that.",
    "That's a tough one, I don't know.",
    "I don't have that information.",
    "I'm not certain about that.",
    "I don't have an answer right now.",
    "That's beyond my knowledge."
]

def get_unknown_response():
    return random.choice(unknown_responses)
