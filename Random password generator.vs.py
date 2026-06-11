import random
import string

print("=== Random Password Generator ===")


length = int(input("Enter password length: "))


use_letters = input("Include letters? (y/n): ").lower()
use_numbers = input("Include numbers? (y/n): ").lower()
use_symbols = input("Include symbols? (y/n): ").lower()


characters = ""

if use_letters == 'y':
    characters += string.ascii_letters

if use_numbers == 'y':
    characters += string.digits

if use_symbols == 'y':
    characters += string.punctuation


if not characters:
    print("Error: Please select at least one character type.")
else:
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))

    print("\nGenerated Password:")
    print(password)