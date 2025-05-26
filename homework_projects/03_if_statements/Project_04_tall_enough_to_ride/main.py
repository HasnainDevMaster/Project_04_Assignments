# Define the minimum height required for the ride
MINIMUM_HEIGHT: int = 50  

def main():
    try:
        # Get the user's height
        height = input("How tall are you? (Press Enter to exit): ").strip()
        
        # Exit if the user presses Enter without input
        if height == "":
            print("No height entered. Exiting program.")
            return
        
        height = float(height)  # Convert input to a number
        
        # Check height requirement
        if height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

    except ValueError:
        print("Invalid input! Please enter a valid number for your height.")

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
