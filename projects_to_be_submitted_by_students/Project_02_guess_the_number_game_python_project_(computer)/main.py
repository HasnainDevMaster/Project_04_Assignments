import random

"""
Computer Guesses Your Number 🎯

Description:
-------------
In this game, you (the human) think of a number between 1 and a given maximum,
and the computer will try to guess it. You give feedback after each guess:
- Enter 'H' if the guess is too high,
- Enter 'L' if it's too low,
- Enter 'C' if the guess is correct.

This game demonstrates:
✅ Binary search logic
✅ Using conditionals and loops
✅ Handling user input
"""

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    print(f"Think of a number between {low} and {high}, and I'll try to guess it!")

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # or high, since low == high
        feedback = input(f"\nIs {guess} too high (H), too low (L), or correct (C)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("Please enter only H, L, or C.")

    print(f"\n🎉 Yay! I guessed your number — {guess} — correctly!")

# Start the game
computer_guess(100)
