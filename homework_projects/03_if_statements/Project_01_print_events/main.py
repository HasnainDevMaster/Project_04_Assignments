def main():
    print("Printing the first 20 even numbers:")
    
    # Loop through the first 20 numbers (0 to 19)
    for i in range(20):
        print(f"Even number {i + 1}: {i * 2}")  # Multiply index by 2 to get even numbers with a labeled message

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
