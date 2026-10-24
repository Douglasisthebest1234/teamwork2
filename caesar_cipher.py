from sha256 import sha_256


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
        print("4) SHA-256 hash")
        print("5) SHA-256 check (does a message match a hash?)")
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
        elif choice == "4":
            message = input("Message to hash: ")
            print("SHA-256:", sha_256(message))
        elif choice == "5":
            message = input("Message: ")
            digest = input("Hash to compare against: ").strip().lower()
            if sha_256(message) == digest:
                print("Match! That message produces this hash.")
            else:
                print("No match.")
        else:
            print("Invalid option, pick 1, 2, 3, 4 or 5.")


if __name__ == "__main__":
    main()
