# Task-01: Implement Caesar Cipher - Prodigy Infotech Internship
# By Srushti Lamgunde - ENTC Engineer

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("--- Caesar Cipher ---")
    choice = input("Choose (E)ncrypt / (D)ecrypt: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))
    if choice == 'e':
        print(f"Encrypted: {encrypt(message, shift)}")
    elif choice == 'd':
        print(f"Decrypted: {decrypt(message, shift)}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()