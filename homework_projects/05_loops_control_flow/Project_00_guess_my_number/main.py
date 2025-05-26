import random  # Import the random module

def main():
    # Generate a random secret number between 0 and 99
    secret_number = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")

    while True:
        try:
            guess = int(input("Enter a guess: "))  # Convert user input to an integer

            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Congrats! The number was: {secret_number}")
                break  # Exit the loop when the correct number is guessed

        except ValueError:
            print("Invalid input! Please enter a number.")

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
