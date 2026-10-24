def caesar(text, shift):
    result = []
    for ch in text:
        if ch.isupper():
            result.append(chr((ord(ch) - ord("A") + shift) % 26 + ord("A")))
        elif ch.islower():
            result.append(chr((ord(ch) - ord("a") + shift) % 26 + ord("a")))
        else:
            result.append(ch)
    return "".join(result)


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, -shift)


def ask_shift():
    while True:
        try:
            return int(input("Shift (e.g. 3): "))
        except ValueError:
            print("Please enter a whole number.")


def main():
    print("=" * 30)
    print("       CAESAR CIPHER")
    print("=" * 30)
    while True:
        print("\n1) Encrypt")
        print("2) Decrypt")
        print("3) Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            message = input("Message to encrypt: ")
            print("Encrypted:", encrypt(message, ask_shift()))
        elif choice == "2":
            message = input("Message to decrypt: ")
            print("Decrypted:", decrypt(message, ask_shift()))
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, pick 1, 2 or 3.")


if __name__ == "__main__":
    main()
