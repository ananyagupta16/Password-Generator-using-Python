import random
import string

def generate_password(length):
    # Define character sets for password complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on user's desired complexity
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password length is at least 8 characters
    length = max(length, 8)

    # Generate the password using random.choices
    password = ''.join(random.choices(all_characters, k=length))

    return password

def main():
    # Prompt user for password length
    length = int(input("Enter the desired length of the password: "))

    # Generate password
    password = generate_password(length)

    # Display the generated password
    print("Generated Password:", password)

main()
