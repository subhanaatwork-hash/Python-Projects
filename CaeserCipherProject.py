
# A simple encryption/decryption tool using Caesar Cipher (shift cipher).

import sys

def encrypt(text, shift):
    """Encrypts the text by shifting each letter by 'shift' positions."""
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - ascii_offset + shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char   # non-letters stay unchanged
    return result

def decrypt(text, shift):
    """Decrypts the text by shifting each letter backwards by 'shift'."""
    return encrypt(text, -shift)  # decryption is just encryption with negative shift

def brute_force(text):
    """Tries all 25 possible shifts to crack the cipher."""
    print("\n--- Brute Force Decryption ---")
    for shift in range(1, 26):
        print(f"Shift {shift:2}: {decrypt(text, shift)}")
    print("--- End of brute force ---\n")

def main():
    print("=== Caesar Cipher Tool ===")
    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Brute force decrypt (try all shifts)")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            text = input("Enter the message to encrypt: ")
            try:
                shift = int(input("Enter shift value (positive integer): "))
            except ValueError:
                print("Invalid shift. Please enter an integer.")
                continue
            result = encrypt(text, shift)
            print(f"\nEncrypted message: {result}")

        elif choice == "2":
            text = input("Enter the message to decrypt: ")
            try:
                shift = int(input("Enter shift value (positive integer): "))
            except ValueError:
                print("Invalid shift. Please enter an integer.")
                continue
            result = decrypt(text, shift)
            print(f"\nDecrypted message: {result}")

        elif choice == "3":
            text = input("Enter the encrypted message to crack: ")
            brute_force(text)

        elif choice == "4":
            print("Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()