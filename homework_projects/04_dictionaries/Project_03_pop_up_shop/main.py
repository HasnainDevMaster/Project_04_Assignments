def main():
    # Dictionary storing fruit names and their prices
    fruits = {
        "apple": 1.5,
        "durian": 50,
        "jackfruit": 80,
        "kiwi": 1,
        "rambutan": 1.5,
        "mango": 5
    }

    total_cost = 0  # Initialize total cost

    # Loop through each fruit in the dictionary
    for fruit_name, price in fruits.items():
        while True:
            try:
                amount_bought = input(f"How many ({fruit_name}) do you want to buy?: ").strip()
                if amount_bought == "":
                    amount_bought = 0  # Default to 0 if user presses Enter
                amount_bought = int(amount_bought)  # Convert input to integer
                if amount_bought < 0:
                    print("Please enter a valid non-negative number.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        total_cost += price * amount_bought  # Calculate total cost

    # Print the final total cost
    print(f"Your total is ${total_cost:.2f}")

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
