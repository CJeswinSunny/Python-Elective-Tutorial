def is_symmetrical(string):
    """
    Check if a string is symmetrical.
    A string is symmetrical if both halves are the same.
    For odd length strings, the middle character is ignored.
    """
    n = len(string)
    half = n // 2
    
    if n % 2 == 0:
        first_half = string[:half]
        second_half = string[half:]
    else:
        first_half = string[:half]
        second_half = string[half+1:]
        
    return first_half == second_half

def is_palindrome(string):
    """
    Check if a string is a palindrome.
    A string is a palindrome if it reads the same forwards and backwards.
    """
    return string == string[::-1]

def main():
    print("--- Symmetrical and Palindrome Checker ---")
    
    while True:
        string = input("\nEnter a string (or type 'quit' to exit): ")
        
        if string.lower() == 'quit':
            print("Exiting program...")
            break

        if is_symmetrical(string):
            print(f"-> The string '{string}' is Symmetrical.")
        else:
            print(f"-> The string '{string}' is NOT Symmetrical.")
            
        if is_palindrome(string):
            print(f"-> The string '{string}' is a Palindrome.")
        else:
            print(f"-> The string '{string}' is NOT a Palindrome.")

if __name__ == "__main__":
    main()
