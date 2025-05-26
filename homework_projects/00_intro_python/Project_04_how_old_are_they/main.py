def main():
    # Store each person's age based on the given conditions
    anton = 21  # Anton's age is given as 21 years old
    beth = anton + 6  # Beth is 6 years older than Anton
    chen = beth + 20  # Chen is 20 years older than Beth
    drew = chen + anton  # Drew is as old as Chen's age plus Anton's age
    ethan = chen  # Ethan is the same age as Chen

    # Print out the ages of each person
    print(f"Anton is {anton}")  # Display Anton's age
    print(f"Beth is {beth}")  # Display Beth's age
    print(f"Chen is {chen}")  # Display Chen's age
    print(f"Drew is {drew}")  # Display Drew's age
    print(f"Ethan is {ethan}")  # Display Ethan's age

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
