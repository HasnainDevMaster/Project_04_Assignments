def get_first_element(lst):
    """Prints the first element of a provided list (if it's not empty)."""
    if lst:  # Check if the list contains elements
        print(f"The first element in the list is: {lst[0]}")
    else:
        print("The list is empty, so there's no first element to display.")

def get_lst():
    """Prompts the user to enter elements one at a time and returns the resulting list."""
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")  

    while elem != "":  # Continue until the user presses enter without input
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")  

    return lst

def main():
    lst = get_lst()  # Get user-inputted list
    get_first_element(lst)  # Print the first element (or a message if empty)

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
