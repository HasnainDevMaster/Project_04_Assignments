def main():
    print("This program adds two numbers.")

    # Prompt the user to enter the first number
    num1 = int(input("Enter first number: "))  # Convert input to integer

    # Prompt the user to enter the second number
    num2 = int(input("Enter second number: "))  # Convert input to integer

    # Calculate the sum of the two numbers
    total = num1 + num2  # Perform addition

    # Print the total sum with an appropriate message
    print(f"The total sum is {total}.")  # Display the result

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
