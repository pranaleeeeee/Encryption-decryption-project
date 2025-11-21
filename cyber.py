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


def main():
    while True:
        print("\n===========================")
        print("       ENCRYPTION TOOL      ")
        print("===========================\n")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit\n")

        choice = input("Enter the number: ").strip()

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
            print("\nExiting the program...")
            break

        else:
            print("\nInvalid option, try again.")
main()


Add a file using the GitHub website (quick, no local git)
Open the repository in your browser.
Click Add file → Create new file.
Type the filename (including any path, e.g., docs/notes.md), add content in the editor.
At the bottom: enter a commit message and choose to commit directly to the default branch or create a new branch and open a pull request.
Click Commit new file.