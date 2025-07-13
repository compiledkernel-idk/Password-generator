import random
import string

def generate_password(length, use_uppercase, use_digits, use_symbols):
    """
    Generates a random password based on specified criteria.

    Args:
        length (int): The desired length of the password.
        use_uppercase (bool): True if uppercase letters should be included.
        use_digits (bool): True if digits (0-9) should be included.
        use_symbols (bool): True if special symbols should be included.

    Returns:
        str: The generated password, or an error message if no character types are selected.
    """
    characters = string.ascii_lowercase # Start with lowercase letters by default

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected to generate a password."

    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    print("Welcome to the Password Generator!")

    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length <= 0:
            print("Password length must be a positive number.")
            exit()
    except ValueError:
        print("Invalid input for length. Please enter a number.")
        exit()

    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_digits = input("Include numbers? (yes/no): ").lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    generated_pw = generate_password(password_length, include_uppercase, include_digits, include_symbols)

    print(f"\nGenerated Password: {generated_pw}")
