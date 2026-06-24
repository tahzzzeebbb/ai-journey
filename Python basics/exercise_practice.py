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