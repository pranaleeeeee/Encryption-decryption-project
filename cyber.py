def clean_path(path):
    """Remove quotes and extra spaces from user file paths."""
    return path.strip().replace('"', '').replace("'", "")


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


def encrypt_file(input_path, output_path, key, shift):
    try:
        # Clean paths
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
        # Clean paths
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


def main():
    while True:
        print("\n===========================")
        print("       ENCRYPTION TOOL      ")
        print("===========================\n")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Encrypt File")
        print("4. Decrypt File")
        print("5. Exit\n")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            text = input("\nEnter text to encrypt: ")
            key = input("Enter key: ")
            shift = int(input("Enter shift value: "))
            encrypted = encrypt(text, key, shift)
            print("\nEncrypted Text:", encrypted)

        elif choice == "2":
            text = input("\nEnter text to decrypt: ")
            key = input("Enter key: ")
            shift = int(input("Enter shift value: "))
            decrypted = decrypt(text, key, shift)
            print("\nDecrypted Text:", decrypted)

        elif choice == "3":
            input_path = input("Enter input file path: ")
            output_path = input("Enter output file path: ")
            key = input("Enter key: ")
            shift = int(input("Enter shift value: "))
            encrypt_file(input_path, output_path, key, shift)

        elif choice == "4":
            input_path = input("Enter encrypted file path: ")
            output_path = input("Enter output file path: ")
            key = input("Enter key: ")
            shift = int(input("Enter shift value: "))
            decrypt_file(input_path, output_path, key, shift)

        elif choice == "5":
            print("\nExiting program...")
            break

        else:
            print("\nInvalid option. Try again.")


main()
