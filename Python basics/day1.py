# variable - no type needed
name = "Ali"
age = 21
is_learning = True

print(name)
print(age)
print(is_learning)

# If / else — same logic as Java, no brackets
score = 85
if score >= 90:
    print("Excellent")
elif score  >= 70:
    print("good")
else:
    print("Keep practicing!")

# Lists — like arrays in Java
skills = ["Pyton", "Java", "Lang-Chain"]
print(skills[0])
skills.append("C++")
print(len(skills))

for skill in skills:
    print(skill)

# Functions
def greet(name, role="student"):
    return f"Your {name} and role is {role}" 

print(greet("Ali"))
print(greet("Ali", "developer"))

# Dictionary — like HashMap in Java
Person = {
    "name": "Ali",
    "age": 21,
    "skills": ["Python", "AI"]
}
print(Person["name"])
print(Person["age"])
print(Person["skills"][0])
print["city"]="Lahore" # add new key
print(Person)

# Python class vs Java class
# Java:  public class Chatbot { private String name; }
# Python: much simpler

class Chatbot:
    def __init__(self, name): # Constuctor __init__
        self.name = name
        self.history = []
    
    def respond(self, message):
        reply = f"{self.name}: I heard you say '{message}'"
        self.history.append(message)
        return reply

    def show_history(self):
        for i, msg in enumerate(self.history):
            print(f"{i+1}. {msg}")


# Use it
bot = Chatbot("Zara")
print(bot.respond("Hello"))
print(bot.respond("Teach me AI"))
bot.show_history()

  