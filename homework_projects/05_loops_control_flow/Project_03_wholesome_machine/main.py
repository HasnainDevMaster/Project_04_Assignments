# Define the affirmation message
AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    print(f"Please type the following affirmation: {AFFIRMATION}")
    
    # Get user input
    user_input = input().strip()

    # Loop until the user types the affirmation correctly
    while user_input != AFFIRMATION:
        print("Hmmm, that was not the affirmation.")
        print(f"Please type the following affirmation: {AFFIRMATION}")
        user_input = input().strip()

    # Congratulate the user upon correct input
    print("That's right! :)")

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
