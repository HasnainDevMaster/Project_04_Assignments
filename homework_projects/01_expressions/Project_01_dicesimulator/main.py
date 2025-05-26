# Import the random library, which lets us simulate dice rolls
import random

# Define the number of sides on each die
NUM_SIDES = 6  

# Function to roll two dice
def roll_dice():
    """Simulates rolling two dice and prints their total."""
    die1 = random.randint(1, NUM_SIDES)  # Roll first die
    die2 = random.randint(1, NUM_SIDES)  # Roll second die
    total = die1 + die2  # Calculate total
    print(f"Die 1: {die1}, Die 2: {die2} -> Total: {total}")

# Main function
def main():
    die1 = 10  # Local variable inside main()
    print(f"die1 in main() starts as: {die1}")  # Show initial value of die1

    # Call roll_dice() function three times
    roll_dice()
    roll_dice()
    roll_dice()

    print(f"die1 in main() is still: {die1}")  # Check if die1 changes

# Execute the main function when the script runs
if __name__ == '__main__':
    main()
