def main():
    # List of valid animals (a small sample, but can be expanded)
    valid_animals = [
        "dog", "cat", "lion", "tiger", "elephant", "giraffe", "zebra", "rabbit", "fox", "wolf",
        "bear", "deer", "cow", "horse", "sheep", "goat", "kangaroo", "panda", "crocodile", "dolphin"
    ]

    while True:
        # Prompt the user to enter their favorite animal
        animal = input("What's your favorite animal? ").strip().lower()

        # Validate input (ensure it's in the list of known animals)
        if animal in valid_animals:
            print(f"My favorite animal is also {animal}!")
            break
        else:
            print("Invalid input! Please enter a real animal name.")

if __name__ == '__main__':
    main()
