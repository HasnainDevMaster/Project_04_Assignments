def add_many_numbers(numbers: list[int]) -> int:
    """Takes in a list of numbers and returns the sum of those numbers."""
    total_so_far: int = 0  # Initialize sum variable
    
    for number in numbers:  # Loop through the list
        total_so_far += number  # Add each number to the total
    
    return total_so_far  # Return the final sum

# Main function to test the sum function
def main():
    numbers: list[int] = [10, 20, 30, 40, 50]  # list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Compute sum
    print(f"The sum of {numbers} is {sum_of_numbers}")  # Display result

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
