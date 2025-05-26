def read_phone_numbers():
    """Ask the user for names/numbers to store in a phonebook (dictionary). Returns the phonebook."""
    phonebook = {}  # Create an empty dictionary

    while True:
        name = input("Enter a name (or press Enter to stop): ").strip()
        if name == "":  # Stop when the user presses Enter without input
            break
        number = input(f"Enter {name}'s phone number: ").strip()
        phonebook[name] = number  # Store name-number pair in dictionary

    return phonebook

def print_phonebook(phonebook):
    """Prints out all the names/numbers in the phonebook."""
    print("\nPhonebook Entries:")
    for name, number in phonebook.items():
        print(f"{name} -> {number}")

def lookup_numbers(phonebook):
    """Allows the user to look up phone numbers by name."""
    while True:
        name = input("Enter a name to look up (or press Enter to stop): ").strip()
        if name == "":  # Stop when the user presses Enter without input
            break
        if name in phonebook:
            print(f"{name}'s phone number is {phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook.")

def main():
    """Handles user input, stores contacts, and allows lookup."""
    phonebook = read_phone_numbers()  # Get user-inputted contacts
    print_phonebook(phonebook)  # Display all contacts
    lookup_numbers(phonebook)  # Allow user to search for contacts

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
