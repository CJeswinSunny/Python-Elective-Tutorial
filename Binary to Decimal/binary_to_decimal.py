def binary_to_decimal(binary_str):
    """
    Converts a binary string to its decimal equivalent.
    """
    try:
        if not all(char in '01' for char in binary_str):
            raise ValueError("Input must be a valid binary string containing only 0s and 1s.")
        
        decimal_value = int(binary_str, 2)
        return decimal_value
    except ValueError as e:
        return f"Error: {e}"

def main():
    print("--- Binary to Decimal Converter ---")
    while True:
        binary_input = input("Enter a binary number (or 'q' to quit): ").strip()
        
        if binary_input.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break
        
        if not binary_input:
            print("Please enter a valid binary number.")
            continue
            
        result = binary_to_decimal(binary_input)
        
        if isinstance(result, int):
            print(f"The decimal equivalent of binary '{binary_input}' is: {result}\n")
        else:
            print(f"{result}\n")

if __name__ == "__main__":
    main()
