# Define voting ages for fictional countries
PETURKSBOUIPO_AGE: int = 16
STANLAU_AGE: int = 25
MAYENGUA_AGE: int = 48

def main():
    try:
        # Get the user's age
        user_age = int(input("How old are you? "))  

        # Check voting eligibility for each country
        if user_age >= PETURKSBOUIPO_AGE:
            print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
        else:
            print(f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")

        if user_age >= STANLAU_AGE:
            print(f"You can vote in Stanlau where the voting age is {STANLAU_AGE}.")
        else:
            print(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE}.")

        if user_age >= MAYENGUA_AGE:
            print(f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
        else:
            print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
    
    except ValueError:
        print("Invalid input! Please enter a valid number for your age.")

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
