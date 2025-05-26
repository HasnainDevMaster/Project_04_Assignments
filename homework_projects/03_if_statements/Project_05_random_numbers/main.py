import random  # Import the random module

# Define constants for number generation
N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    print("Generating 10 random numbers between 1 and 100:")
    
    # Loop to generate and print 10 random numbers
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")  # Print numbers in a single line

    print()  # Move to a new line after printing numbers

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
