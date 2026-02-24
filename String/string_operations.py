def main():
    print("--- Creating Strings ---")
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    print(f"\nString 1: {string1}")
    print(f"String 2: {string2}")

    concatenated_string = string1 + " " + string2
    
    print("\n--- Concatenating and Printing ---")
    print("Concatenated String:", concatenated_string)

    print("\n--- Accessing Sub-string ---")
    print(f"The combined string has {len(concatenated_string)} characters (indices 0 to {len(concatenated_string)-1}).")
    
    try:
        start_index = int(input("Enter starting index for the sub-string: "))
        end_index = int(input("Enter ending index for the sub-string: "))
        
        sub_string = concatenated_string[start_index:end_index]
        
        print(f"\nExtracting sub-string from index {start_index} to {end_index} of '{concatenated_string}':")
        print("Resulting Sub-string:", sub_string)
    except ValueError:
        print("Invalid input! Please enter valid integer numbers for indices.")

if __name__ == "__main__":
    main()
