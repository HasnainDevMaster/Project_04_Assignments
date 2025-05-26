def main():
    try:
        # Get the year from the user
        year = int(input("Please input a year: "))

        # Check leap year conditions
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print("That's a leap year!")
                else:
                    print("That's not a leap year.")
            else:
                print("That's a leap year!")
        else:
            print("That's not a leap year.")

    except ValueError:
        print("Invalid input! Please enter a valid number for the year.")

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
