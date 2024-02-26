#!/usr/bin/python

import argparse

def assess_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in '!@#$%^&*()-_=+[{]};:|,.<>?`~' for char in password)

    # Assessing password strength based on criteria
    strength = 0
    if length >= 8:
        strength += 1
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    return min(int(strength * 2), 10)  # Cap strength to a maximum of 10 and remove decimal

def main():
    parser = argparse.ArgumentParser(description="Assess the strength of a password.")
    parser.add_argument("-p", "--password", help="Password to assess")
    args = parser.parse_args()

    if args.password:
        password = args.password
    else:
        password = input("Enter your password: ")

    strength = assess_password_strength(password)
    print(f"Password strength: {strength}/10")

if __name__ == "__main__":
    main()
