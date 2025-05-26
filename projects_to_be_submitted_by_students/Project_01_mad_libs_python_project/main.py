"""
Mad Libs - Fun with F-Strings 🎉

Description:
-------------
This is a simple Python project that asks the user to input different types of words
(adjective, verb, noun, etc.) and then inserts those words into a pre-defined story 
template using f-strings. The final result is a personalized paragraph.

It's a great beginner-friendly project to understand:
✅ string concatenation
✅ user input
✅ using f-strings to format strings cleanly
"""


# Collect user inputs:

adjective = input("Adjective: ")
language = input("Programming language: ")
verb = input("Verb ending in 'ing': ")
tool = input("Dev tool: ")
ceo = input("Tech CEO or dev name: ")


# Create the Mad Lib using f-strings:

madlib = (
    f"Today, I was {verb} in {language} using {tool}. "
    f"It was so {adjective}, I nearly tossed my laptop—until {ceo} tweeted, "
    f"'Code like it compiles the first time.'"
)


# Print the final story:

print("\nHere’s your Mad Lib story:\n")
print(madlib)
