#!/usr/bin/env python3
"""
secure_password_generator.py
Generates strong passwords with customizable length and complexity.
Optionally hashes the password using SHA-256 or bcrypt.
"""

import string
import random
import hashlib
import bcrypt

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    """Generate a strong random password"""
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def hash_sha256(password):
    """Hash the password using SHA-256"""
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

def hash_bcrypt(password):
    """Hash the password using bcrypt"""
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed

if __name__ == "__main__":
    print("=== Secure Password Generator ===")
    length = int(input("Enter password length (default 12): ") or 12)
    password = generate_password(length)
    print(f"\nGenerated Password: {password}")

    # Ask user if they want to hash it
    choice = input("\nDo you want to hash the password? (yes/no): ").strip().lower()
    if choice == "yes":
        method = input("Choose hashing method (sha256/bcrypt): ").strip().lower()
        if method == "sha256":
            print(f"SHA-256 Hash: {hash_sha256(password)}")
        elif method == "bcrypt":
            print(f"bcrypt Hash: {hash_bcrypt(password)}")
        else:
            print("Invalid hashing method selected.")