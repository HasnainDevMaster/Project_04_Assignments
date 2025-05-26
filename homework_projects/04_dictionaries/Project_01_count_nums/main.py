def get_user_numbers():
    """Prompts the user to enter numbers and stores them in a list."""
    user_numbers = []  # Initialize an empty list
    while True:
        user_input = input("Enter a number (or press Enter to finish): ").strip()
        if user_input == "":  # Stop when the user presses Enter without input
            break
        try:
            num = int(user_input)  # Convert input to an integer
            user_numbers.append(num)  # Add number to the list
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    return user_numbers

def count_nums(num_lst):
    """Counts occurrences of each number in the list using a dictionary."""
    num_dict = {}  # Initialize an empty dictionary
    for num in num_lst:
        num_dict[num] = num_dict.get(num, 0) + 1  # Increment count

    return num_dict

def print_counts(num_dict):
    """Prints the count of each unique number in the dictionary."""
    for num, count in num_dict.items():
        print(f"{num} appears {count} times.")

def main():
    """Handles user input, counts occurrences, and prints results."""
    user_numbers = get_user_numbers()  # Get user-inputted numbers
    if not user_numbers:
        print("No numbers entered. Exiting program.")
        return

    num_dict = count_nums(user_numbers)  # Count occurrences
    print_counts(num_dict)  # Display results

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
