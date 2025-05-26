def main():
    lst = []  # Initialize an empty list to store values

    # Continuously prompt the user for input
    while True:
        val = input("Enter a value (or press Enter to finish): ")  # Get user input
        if val == "":  # Stop when the user presses Enter without input
            break
        lst.append(val)  # Add the entered value to the list

    # Check if the list is empty before printing
    if lst:
        print(f"Here's the list: {lst}")
    else:
        print("The list is empty, no values were entered.")

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
