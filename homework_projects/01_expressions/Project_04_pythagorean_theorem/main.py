import math  # Import the math library to use sqrt()

def main():
    # Get the lengths of the two perpendicular sides from the user
    ab: float = float(input("Enter the length of AB: "))  
    ac: float = float(input("Enter the length of AC: "))  

    # Calculate the hypotenuse using the Pythagorean theorem
    bc: float = math.sqrt(ab ** 2 + ac ** 2)  

    # Display the result
    print(f"The length of BC (the hypotenuse) is: {bc}")

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
