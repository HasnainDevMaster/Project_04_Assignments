import random

def main():
    secret_number = random.randint(0, 99)
    print("🎯 I'm thinking of a number between 0 and 99...")

    while True:
        guess = input("Enter a guess: ")

        # Validate input
        if not guess.isdigit():
            print("⚠️ Please enter a valid number.")
            continue

        guess = int(guess)

        if guess < secret_number:
            print("🔻 Your guess is too low.\n")
        elif guess > secret_number:
            print("🔺 Your guess is too high.\n")
        else:
            print(f"🎉 Congrats! The number was: {secret_number}")
            break

# Call the main function
if __name__ == '__main__':
    main()
