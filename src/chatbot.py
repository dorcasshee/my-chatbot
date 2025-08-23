import random

class MyChatbot:
    def generate_response(self, user_msg: str) -> str:
        user_greetings = ['hello', 'hi', 'hey', 'herro', 'yo']
        chatbot_greetings = ['Hey there!', 'Hello!', 'Hi!', "Yo!"]
        introduction = 'How may I help you?'

        for keyword in user_greetings:
            if keyword in user_msg.lower():
                greeting = random.choice(chatbot_greetings)
                return f"{greeting} {introduction}"

        return "I do not understand your question. Could you try another query?"