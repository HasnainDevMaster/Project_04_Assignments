from hashlib import sha256

def hash_password(password):
    """Hashes a password using SHA-256."""
    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, password_to_check):
    """Returns True if the hashed password matches the stored hash for the given email."""
    if email in stored_logins and stored_logins[email] == hash_password(password_to_check):
        return True
    return False

def main():
    # Dictionary storing emails and their hashed passwords
    stored_logins = {
        "example@gmail.com": hash_password("password123"),
        "user@secure.com": hash_password("my_secure_pass"),
        "admin@website.com": hash_password("admin2025")
    }

    # Test login functionality
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

    if login(email, stored_logins, password):
        print("Login successful!")
    else:
        print("Invalid email or password.")

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
