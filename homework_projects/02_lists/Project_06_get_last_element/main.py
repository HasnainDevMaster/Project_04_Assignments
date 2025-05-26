def get_last_element(lst):
    """Prints the last element of a provided list if it's not empty."""
    if lst:  # Check if the list has elements
        print(f"The last element in the list is: {lst[-1]}")
    else:
        print("The list is empty, so there's no last element to display.")

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
    get_last_element(lst)  # Print the last element (or a message if empty)

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
