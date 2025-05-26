# Define the maximum allowed Fibonacci value
MAX_TERM_VALUE: int = 10000  

def main():
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number

    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # Print Fibonacci number in a single line
        term_after_next = curr_term + next_term  # Calculate next term
        curr_term = next_term  # Move to next term
        next_term = term_after_next  # Update next term

    print()  # Move to a new line after printing numbers

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
