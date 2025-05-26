import random

"""
Number Guessing Game 🎯

Description:
-------------
This is a simple number guessing game where the **player** tries to guess a random number
between 50 and 100. You only have 5 chances to guess it correctly!

After each guess, you'll get feedback:
📉 Too low  
📈 Too high  
🎉 Correct!

The game keeps track of all your guesses and lets you play again if you want.

Great for beginners learning:
✅ Loops and conditionals  
✅ Exception handling  
✅ Lists and input  
✅ Functions and game logic
"""

def play_game():
    print("\n🎯 Welcome to the Number Guessing Game!")
    print("You have 5 chances to guess a number between 50 and 100.")

    number_to_guess = random.randrange(50, 100)
    chances = 5
    guess_counter = 0
    guesses = []

    while guess_counter < chances:
        try:
            my_guess = int(input(f"\nGuess #{guess_counter + 1}: "))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            continue

        guesses.append(my_guess)
        guess_counter += 1

        if my_guess == number_to_guess:
            print(f"🎉 Correct! The number was {number_to_guess}. You guessed it in {guess_counter} tries.")
            break
        elif my_guess < number_to_guess:
            print("📉 Too low! Try again.")
        elif my_guess > number_to_guess:
            print("📈 Too high! Try again.")

        if guess_counter == chances and my_guess != number_to_guess:
            print(f"\n😢 Out of chances! The number was {number_to_guess}. Better luck next time!")

    print(f"📜 Your guesses were: {guesses}")

def main():
    while True:
        play_game()
        again = input("\n🔁 Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
