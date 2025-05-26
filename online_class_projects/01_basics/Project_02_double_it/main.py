def main():
    while True:
        user_input = input("Enter a number to double: ")

        # Validate input: must be a positive integer
        if user_input.isdigit():
            curr_value = int(user_input)
            if curr_value > 0:
                break
            else:
                print("⚠️ Please enter a number greater than 0.")
        else:
            print("⚠️ Invalid input. Please enter a valid number.")

    # If the number is already 100 or more
    if curr_value >= 100:
        print("✅ The number is already 100 or more. No doubling needed!")
    else:
        print("🔁 Doubling steps:")
        step = 1
        while curr_value < 100:
            next_value = curr_value * 2
            print(f"Step {step}: {curr_value} → {next_value}")
            curr_value = next_value
            step += 1
        print("🎉 Done! The value is now 100 or more.")

# Run the program
if __name__ == '__main__':
    main()
