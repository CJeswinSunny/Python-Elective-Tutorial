def reverse_string(s):
    """
    Reverses the input string.
    """
    return s[::-1]

if __name__ == "__main__":
    print("--- String Reverser ---")
    text = input("Enter a string to reverse: ")
    reversed_text = reverse_string(text)
    print(f"\nOriginal string: {text}")
    print(f"Reversed string: {reversed_text}")
