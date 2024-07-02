import argparse
import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected")

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description='Random Password Generator')
    parser.add_argument('-l', '--length', type=int, default=12, help='Length of the password')
    parser.add_argument('-u', '--uppercase', action='store_true', help='Include uppercase letters')
    parser.add_argument('-lw', '--lowercase', action='store_true', help='Include lowercase letters')
    parser.add_argument('-d', '--digits',action='store_true', help='Include digits')
    parser.add_argument('-s', '--special', action='store_true', help='Include special characters')

    args = parser.parse_args()

    try:
        password = generate_password(args.length, args.uppercase, args.lowercase, args.digits, args.special)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
