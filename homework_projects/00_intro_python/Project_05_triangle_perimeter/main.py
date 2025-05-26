def main():
    print("This program calculates the perimeter of a triangle.")

    # Function to get valid numeric input
    def get_valid_side(side_number):
        while True:
            try:
                side = float(input(f"What is the length of side {side_number}? "))  # Convert input to float
                if side > 0:  # Ensure positive length
                    return side
                else:
                    print("Side length must be a positive number. Try again.")
            except ValueError:
                print("Invalid input! Please enter a valid numeric value.")

    # Get valid side lengths from user
    side1 = get_valid_side(1)
    side2 = get_valid_side(2)
    side3 = get_valid_side(3)

    # Calculate the perimeter (sum of all sides)
    perimeter = side1 + side2 + side3

    # Display the calculated perimeter
    print(f"The perimeter of the triangle is {perimeter:.2f}")

# Required line to call the main() function
if __name__ == '__main__':
    main()
