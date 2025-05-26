# Constants
PROMPT = "What do you want? "
JOKE = "Here is Joke for you! Why do programmers prefer dark mode? Because light attracts bugs! 🐛💡"
SORRY = "Sorry I only tell jokes 😅"

# Get user input
user_input = input(PROMPT).lower()

# Respond based on input
if user_input == "joke":
    print(JOKE)
else:
    print(SORRY)
