def main():
    # Get the numbers we want to divide
    dividend: int = int(input("Please enter an integer to be divided: "))  
    divisor: int = int(input("Please enter an integer to divide by: "))  

    # Perform integer division and find the remainder
    quotient: int = dividend // divisor  # Integer division
    remainder: int = dividend % divisor  # Modulo operation

    # Display the result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
