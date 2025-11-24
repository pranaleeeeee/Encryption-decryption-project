def clean_path(path):
    """Remove quotes and extra spaces from user file paths."""
    return path.strip().replace('"', '').replace("'", "")


# ------------------ VIGENERE + SHIFT ENCRYPTION ------------------

def encrypt(text, key, shift):
    encrypted = ""
    key = key.lower()
    key_len = len(key)

    for i, ch in enumerate(text):
        if ch.isalpha():
            key_shift = ord(key[i % key_len]) - ord('a')
            base = ord('a') if ch.islower() else ord('A')
            new_char = chr((ord(ch) - base + key_shift + shift) % 26 + base)
            encrypted += new_char
        else:
            encrypted += ch
    return encrypted


def decrypt(ciphertext, key, shift):
    decrypted = ""
    key = key.lower()
    key_len = len(key)

    for i, ch in enumerate(ciphertext):
        if ch.isalpha():
            key_shift = ord(key[i % key_len]) - ord('a')
            base = ord('a') if ch.islower() else ord('A')
            new_char = chr((ord(ch) - base - key_shift - shift) % 26 + base)
            decrypted += new_char
        else:
            decrypted += ch
    return decrypted


# ------------------ FILE ENCRYPTION ------------------

def encrypt_file(input_path, output_path, key, shift):
    try:
        input_path = clean_path(input_path)
        output_path = clean_path(output_path)

        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()

        encrypted_text = encrypt(text, key, shift)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(encrypted_text)

        print("\nFile encrypted successfully!")
        print(f"Saved as: {output_path}")

    except FileNotFoundError:
        print("\nError: Input file not found.")
    except Exception as e:
        print("\nUnexpected error:", e)


def decrypt_file(input_path, output_path, key, shift):
    try:
        input_path = clean_path(input_path)
        output_path = clean_path(output_path)

        with open(input_path, "r", encoding="utf-8") as f:
            ciphertext = f.read()

        decrypted_text = decrypt(ciphertext, key, shift)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(decrypted_text)

        print("\nFile decrypted successfully!")
        print(f"Saved as: {output_path}")

    except FileNotFoundError:
        print("\nError: Input file not found.")
    except Exception as e:
        print("\nUnexpected error:", e)


# ------------------ CAESAR ONLY ENCRYPTION ------------------

def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# ------------------ MENU ------------------

def menu():
    print("\n===========================")
    print("      ENCRYPTION TOOL      ")
    print("===========================\n")
    print("1. Encrypt Text (Vigenère + Shift)")
    print("2. Decrypt Text (Vigenère + Shift)")
    print("3. Encrypt File")
    print("4. Decrypt File")
    print("5. Caesar Encrypt")
    print("6. Caesar Decrypt")
    print("7. Exit\n")

    return input("Enter your choice: ")


# ------------------ MAIN PROGRAM ------------------

def main():
    while True:
        choice = menu()

        if choice == "1":
            text = input("\nEnter text to encrypt: ")
            key = input("Enter key: ")
            shift = int(input("Enter shift: "))
            print("\nEncrypted Text:", encrypt(text, key, shift))

        elif choice == "2":
            text = input("\nEnter text to decrypt: ")
            key = input("Enter key: ")
            shift = int(input("Enter shift: "))
            print("\nDecrypted Text:", decrypt(text, key, shift))

        elif choice == "3":
            input_path = input("\nEnter input file path: ")
            output_path = input("Enter output file path: ")
            key = input("Enter key: ")
            shift = int(input("Enter shift: "))
            encrypt_file(input_path, output_path, key, shift)

        elif choice == "4":
            input_path = input("\nEnter encrypted file path: ")
            output_path = input("Enter output file path: ")
            key = input("Enter key: ")
            shift = int(input("Enter shift: "))
            decrypt_file(input_path, output_path, key, shift)

        elif choice == "5":
            text = input("\nEnter text: ")
            shift = int(input("Enter shift: "))
            print("\nCaesar Encrypted:", caesar_encrypt(text, shift))

        elif choice == "6":
            text = input("\nEnter text: ")
            shift = int(input("Enter shift: "))
            print("\nCaesar Decrypted:", caesar_decrypt(text, shift))

        elif choice == "7":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Try again.")


# ------------------ RUN ------------------

if __name__ == "__main__":
    main()
