# Import the random library to simulate dice rolls
import random

# Define the number of sides on each die
NUM_SIDES: int = 6  

def main():
    # Roll two dice
    die1: int = random.randint(1, NUM_SIDES)  # First die roll
    die2: int = random.randint(1, NUM_SIDES)  # Second die roll

    # Calculate the total
    total: int = die1 + die2  

    # Print the results
    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
