# 10. Write a program to create, concatenate and print a string and accessing sub-string from a given string

def main():
    # 1. Create strings from user input
    print("--- Creating Strings ---")
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    print(f"\nString 1: {string1}")
    print(f"String 2: {string2}")

    # 2. Concatenate strings
    # Merging the two strings with a space
    concatenated_string = string1 + " " + string2
    
    # 3. Print the concatenated string
    print("\n--- Concatenating and Printing ---")
    print("Concatenated String:", concatenated_string)

    # 4. Accessing a sub-string
    print("\n--- Accessing Sub-string ---")
    print(f"The combined string has {len(concatenated_string)} characters (indices 0 to {len(concatenated_string)-1}).")
    
    try:
        start_index = int(input("Enter starting index for the sub-string: "))
        end_index = int(input("Enter ending index for the sub-string: "))
        
        # Extract sub-string using string slicing
        sub_string = concatenated_string[start_index:end_index]
        
        print(f"\nExtracting sub-string from index {start_index} to {end_index} of '{concatenated_string}':")
        print("Resulting Sub-string:", sub_string)
    except ValueError:
        print("Invalid input! Please enter valid integer numbers for indices.")

if __name__ == "__main__":
    main()
