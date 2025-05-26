# Useful constants to make the math easier and cleaner!
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    # Calculate the number of seconds in a year
    total_seconds: int = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    
    # Print the result in a formatted message
    print(f"There are {total_seconds} seconds in a year!")

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
