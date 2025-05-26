# Define the maximum allowed length for the list
MAX_LENGTH: int = 3  

def shorten(lst):
    """Removes elements from the end of lst until it is MAX_LENGTH items long."""
    if not lst:  # Check if the list is empty
        print("The list is empty. Nothing to shorten.")
        return
    
    while len(lst) > MAX_LENGTH:  # Keep removing until the list is short enough
        last_elem = lst.pop()  # Remove the last element
        print(f"Removed: {last_elem}")  # Print the removed element

def get_lst():
    """Prompts the user to enter elements one at a time and returns the resulting list."""
    lst = []
    while True:
        try:
            elem = input("Please enter an element of the list or press enter to stop: ").strip()
            if elem == "":  # Stop when the user presses enter without input
                break
            lst.append(elem)
        except Exception as e:
            print(f"Error: {e}. Please enter a valid value.")
    
    return lst

def main():
    lst = get_lst()  # Get user-inputted list
    if not lst:
        print("The list is empty. No values were entered.")
        return
    
    print(f"Original list: {lst}")  # Show the list before modification
    shorten(lst)  # Modify the list if needed
    print(f"Final list: {lst}")  # Show the list after modification

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
