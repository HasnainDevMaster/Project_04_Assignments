def main():
    print("This program converts Fahrenheit to Celsius.")

    while True:
        try:
            # Prompt the user to enter a temperature in Fahrenheit
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))  # Convert input to float

            # Convert Fahrenheit to Celsius using the given formula
            celsius = (fahrenheit - 32) * 5.0 / 9.0

            # Display the result with two decimal places
            print(f"Temperature: {fahrenheit:.1f}F = {celsius:.2f}C")
            break  # Exit loop after successful conversion

        except ValueError:
            print("Invalid input! Please enter a valid numeric temperature.")  # Handle non-numeric input

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == "__main__":
    main()
