# my_first_chatbot.py

class SimpleChatbot:
    def __init__(self, name):
        self.name = name
        self.history = []

    def respond(self, user_input):
        user_input = user_input.lower()

        if "hello" in user_input or "hi" in user_input:
            reply = "Hello! How can I help you today?"
        elif "name" in user_input:
            reply = f"My name is {self.name}!"
        elif "bye" in user_input:
            reply = "Goodbye! Keep learning!"
        else:
            reply = f"You said: '{user_input}'. I'm still learning!"

        self.history.append({
            "user": user_input,
            "bot": reply
        })
        return reply

# Run the chatbot
bot = SimpleChatbot("Zara")
print(f"{bot.name} is ready! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")
    response = bot.respond(user_input)
    print(f"{bot.name}: {response}\n")

    if "bye" in user_input.lower():
        break