# Define the conversion factor as a constant
INCHES_IN_FOOT: int = 12  # There are 12 inches in 1 foot

# Main function to convert feet to inches
def main():
    # Ask the user for the number of feet (convert input to float for precision)
    feet: float = float(input("Enter number of feet: "))  
    
    # Perform the conversion
    inches: float = feet * INCHES_IN_FOOT  
    
    # Display the result
    print(f"That is {inches} inches!")

# This provided line is required at the end of a Python file to call the main() function
if __name__ == '__main__':
    main()
