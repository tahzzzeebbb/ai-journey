# 5 Python Exercises — AI App Style
# Your task: Create a function called format_message(role, content)
# that returns the formatted string
user = "Alice"
assistant = "Zara"
def format_message(role, content):
    return f"[{role}]: {content}"

# Test it with: format_message("user", "Hello there")
# format_message("assistant", "Hi! How can I help?")
print(format_message(user, "Hello there")) 
print(format_message(assistant, "Hi! How can I help?"))

# Exercise 2 — Conversation History
# Your task:
# 1. Create an empty list called history
# 2. Create a function add_message(history, role, content)
#    that appends {"role": role, "content": content} to history
# 3. Create a function show_history(history)
#    that prints each message formatted nicely

# Test with 3 messages — user, assistant, user
history = []

def add_message(history, role, content):
    history.append({"role": role, "content": content})

def show_history(history):
    for msg in history:
        print(f"[{msg['role']}]: {msg['content']}")

add_message(history, "user", "What is AI?")
add_message(history, "assistant", "AI is artificial intelligence!")
add_message(history, "user", "Cool, teach me more.")

show_history(history)

# Exercise 3 — Token Counter

#AI models charge by tokens. A simple estimate is 1 token ≈ 4 characters. Write a function that estimates token count for a message.

# Your task:
# Create a function count_tokens(text)
# that returns estimated token count (len(text) // 4)
# 
# Then write a function check_limit(text, max_tokens=100)
# that returns True if within limit, False if over
#
# Test with a short and a very long message

def count_tokens(text):
    return len(text) // 4

def check_limit(text, max_tokens=100):
    tokens = count_tokens(text)
    print(f"Estimated tokens: {tokens}")
    return tokens <= max_tokens

short_msg = "Hello, how are you?"
long_msg = "a" * 500

print(check_limit(short_msg))  # True
print(check_limit(long_msg))   # False

# Exercise 4 — Simple Intent Detector
#Chatbots detect what the user wants. Write a function that detects intent from a message.

# Your task:
# Create a function detect_intent(message) that returns:
# "greeting"   if message contains hello/hi/hey
# "farewell"   if message contains bye/goodbye
# "question"   if message contains what/how/why/when
# "unknown"    for anything else
#
# Test with 5 different messages
def detect_intent(message):
    message = message.lower()
    
    greetings = ["hello", "hi", "hey"]
    farewells = ["bye", "goodbye"]
    questions = ["what", "how", "why", "when"]
    
    for word in greetings:
        if word in message:
            return "greeting"
    
    for word in farewells:
        if word in message:
            return "farewell"
    
    for word in questions:
        if word in message:
            return "question"
    
    return "unknown"

print(detect_intent("Hey there!"))         # greeting
print(detect_intent("How does AI work?"))  # question
print(detect_intent("Goodbye!"))           # farewell
print(detect_intent("Python is cool"))     # unknown
print(detect_intent("What is LangChain")) # question

# Exercise 5 — Chatbot Class (put it all together)

#Combine everything into one Chatbot class that tracks history, detects intent, and responds accordingly.

# Your task:
# Create a class called SmartChatbot with:
# - __init__(self, name) → sets name, empty history
# - detect_intent(self, message) → from exercise 4
# - respond(self, message) → detects intent, gives reply,
#   saves to history, returns reply
# - show_history(self) → prints full conversation
#
# Run a 4-message conversation with it
class SmartChatbot:
    def __init__(self, name):
        self.name = name
        self.history = []

    def detect_intent(self, message):
        message = message.lower()
        if any(w in message for w in ["hello", "hi", "hey"]):
            return "greeting"
        if any(w in message for w in ["bye", "goodbye"]):
            return "farewell"
        if any(w in message for w in ["what", "how", "why", "when"]):
            return "question"
        return "unknown"

    def respond(self, message):
        intent = self.detect_intent(message)

        if intent == "greeting":
            reply = f"Hello! I'm {self.name}, your AI assistant!"
        elif intent == "farewell":
            reply = "Goodbye! Keep building amazing things!"
        elif intent == "question":
            reply = "Great question! I'm still learning to answer that."
        else:
            reply = f"Interesting! Tell me more."

        self.history.append({"user": message, "bot": reply})
        return reply

    def show_history(self):
        print(f"\n--- {self.name} Conversation History ---")
        for msg in self.history:
            print(f"You: {msg['user']}")
            print(f"{self.name}: {msg['bot']}\n")


# Test it
bot = SmartChatbot("Zara")
print(bot.respond("Hey there!"))
print(bot.respond("How does AI work?"))
print(bot.respond("What is Python?"))
print(bot.respond("Goodbye!"))
bot.show_history()