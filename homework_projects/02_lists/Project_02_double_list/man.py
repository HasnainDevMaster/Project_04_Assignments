def main():
    # Create a list of numbers
    numbers: list[int] = [1, 2, 3, 4]  
    
    # Loop through the indices of the list
    for i in range(len(numbers)):  
        elem_at_index = numbers[i]  # Get the element at index i
        numbers[i] = elem_at_index * 2  # Double the value and update the list

    # Print the updated list with doubled values
    print(numbers)  

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
