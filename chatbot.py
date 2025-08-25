import random

class MyChatbot:
    greetings = ['hello', 'hi', 'hey', 'herro', 'yo']
    greeting_responses = ['Hey there!', 'Hello!', 'Hi!', "Yo!"]
    
    who_keywords = ['who are you', 'hu r u', 'who r u', 'hu u', ' who u', 'what r u', 'what are you']
    introduction = "I am My Chatbot! I am a chatbot that can help you with basic questions, tell jokes, and share interesting facts. What would you like to chat about?"
    
    capability_keywords = ['what can you do', 'what can u do', 'what do you do', 'what do u do', 'capabilities', 'functions', 'what can i ask', 'what else can you do']
    capabilities = """I can chat with you! Try asking me to:
    - Say hello  
    - Tell you a joke
    - Share a fun fact
    - Tell you about Visa
    """
    
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? He was outstanding in his field!",
        "Why don't skeletons ever fight each other? Because they don’t have the guts.",
        "What do you call fake spaghetti? An impasta.",
        "Parallel lines have so much in common. It’s a shame they’ll never meet!",
        "Why don’t programmers like nature? Too many bugs.",
        "Why did the banker quit his job? He lost interest.",
        "Why don’t mathematicians argue? Because they can always agree on the sum of things."
    ]
    
    fun_facts = [
        "Did you know? Honey never spoils! Archaeologists have found edible honey in Egyptian tombs.",
        "Fun fact: A group of flamingos is called a 'flamboyance'!",
        "Bananas are berries, but strawberries are not.",
        "Octopuses have three hearts, and two of them stop beating when they swim.",
        "A day on Venus is longer than a year on Venus.",
        "The fingerprints of a koala are so similar to humans that they can confuse crime scene investigators.",
        "Did you know? The first-ever credit card was introduced in 1950 by Diners Club. Its inventor, Frank McNamara, forgot his wallet during a dinner in New York.",
        "Fun fact: Contactless payments are processed in less than half a second.",
        "Did you know? Mobile payments in China are so common that even street performers use QR codes to get tips.",
        "Fun fact: Bitcoin’s creator, Satoshi Nakamoto, has never been identified.",
        "Did you know? Kenya’s M-Pesa mobile money system handles more transactions than most of the country’s banks combined."
    ]
    
    company_info = """Visa Inc. is a global payments technology company.
    
    They do not issue credit or debit cards directly. Instead, they provide the secure payment network (VisaNet) that banks, fintechs, and merchants use to process transactions worldwide.
    
    Scale: VisaNet processes tens of thousands of transactions per second across 200+ countries.  
    Services: Credit/debit/prepaid card processing, contactless payments, online payments, fraud prevention, and cross-border transfers.  
    Mission: To connect the world through the most innovative, reliable, and secure digital payment network.  
    Fun fact: Visa began in 1958 as BankAmericard, and rebranded as Visa in 1976.
    """
    
    goodbye_words = ['bye', 'goodbye', 'see you', 'farewell']
    goodbye_responses = ["Goodbye! Have a great day!", "See you later!", "Take care!"]
    
    def generate_response(self, user_msg: str) -> str:
        question = user_msg.lower()
        
        if any(keyword in question for keyword in self.goodbye_words):
            return random.choice(self.goodbye_responses)
        
        if 'joke' in question or 'funny' in question:
            return random.choice(self.jokes)
        
        if 'fun fact' in question or 'fact' in question or 'interesting' in question:
            return random.choice(self.fun_facts)
        
        if 'visa' in question or 'company' in question:
            return self.company_info
            
        if any(keyword in question for keyword in self.who_keywords):
            return self.introduction
        
        if any(keyword in question for keyword in self.capability_keywords):
            return self.capabilities
        
        if any(keyword in question for keyword in self.greetings):
            return random.choice(self.greeting_responses) + " How can I help you today?"
            
        return "I'm sorry, I do not understand that. Try asking me to tell you a joke or fun fact instead!"