from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement

class GToiletAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def can_process(self, statement):
        return True  # Adapter pour toutes les déclarations

    def process(self, statement, additional_response_selection_parameters=None):
        if 'astro toilet' in statement.text.lower():
            response = "Oh no, not the Astro Toilets! We're with the Alliance here."
        elif 'insult' in statement.text.lower():
            response = "Oh dear, let's calm down a bit! We're all friends here, no need for insults."
        else:
            response = "I'm G-toilet, the toilet chief! How can I help you?"

        return Statement(text=response)
