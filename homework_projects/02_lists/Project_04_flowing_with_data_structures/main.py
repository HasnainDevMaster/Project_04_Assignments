def add_three_copies(my_list, data):
    """Adds three copies of data to the given list without returning it."""
    for _ in range(3):  # Loop three times
        my_list.append(data)  # Append data to the list

# Main function to test mutability
def main():
    message = input("Enter a message to copy: ")  # Get user input
    my_list = []  # Initialize an empty list

    print("List before:", my_list)  # Show list before modification
    add_three_copies(my_list, message)  # Call function to modify list
    print("List after:", my_list)  # Show list after modification

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
