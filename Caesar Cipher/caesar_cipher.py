def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts a text using Caesar Cipher.
    """
    result = ""
    # Reverse the shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        # Check if character is a letter
        if char.isalpha():
            # Determine the ASCII offset depending on uppercase or lowercase
            start = ord('a') if char.islower() else ord('A')
            # Calculate the new character
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            # Leave symbols, spaces, and numbers as they are
            result += char
            
    return result

def main():
    print("--- Caesar Cipher (Encrypt & Decrypt) ---")
    while True:
        mode_input = input("\nDo you want to (e)ncrypt or (d)ecrypt? (Enter 'q' to quit): ").lower().strip()
        
        if mode_input == 'q' or mode_input == 'quit':
            print("Goodbye!")
            break
            
        if mode_input not in ['e', 'd', 'encrypt', 'decrypt']:
            print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
            continue

        mode = 'encrypt' if mode_input in ['e', 'encrypt'] else 'decrypt'
        
        text = input("Enter the text: ")
        
        try:
            shift = int(input("Enter the shift number: "))
        except ValueError:
            print("Invalid shift number. Please enter a valid integer.")
            continue

        result = caesar_cipher(text, shift, mode)
        print(f"\nResult ({mode}ed text):")
        print(f"> {result}")

if __name__ == "__main__":
    main()
