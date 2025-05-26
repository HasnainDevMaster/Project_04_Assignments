# Define the speed of light as a constant
C = 299792458  # Speed of light in meters per second

# Main function to calculate energy from mass
def main():
    while True:  # Creates a loop to continually read mass
        try:
            # Ask the user for mass in kilograms
            mass = float(input("Enter kilos of mass (or type 0 to exit): "))  
            
            # Exit condition
            if mass == 0:
                print("Exiting program. Goodbye!")
                break  # Stop the loop
            
            # Calculate energy using Einstein's equation
            energy = mass * (C ** 2)
            
            # Print results in a formatted manner
            print("\ne = m * C^2...")
            print(f"m = {mass} kg")
            print(f"C = {C} m/s")
            print(f"{energy:.2e} joules of energy!\n")  # Format large numbers
            
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Call the main function
if __name__ == '__main__':
    main()
