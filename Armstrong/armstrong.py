def is_armstrong_number(num):
    # Convert number to string to easily iterate over digits and find length
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of digits raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return sum_of_powers == num

def main():
    print("--- Armstrong Number Checker ---")
    try:
        user_input = input("Enter a positive integer to check if it's an Armstrong number: ")
        num = int(user_input)
        
        if num < 0:
            print("Please enter a positive integer.")
            return

        if is_armstrong_number(num):
            print(f"{num} is an Armstrong number.")
        else:
            print(f"{num} is not an Armstrong number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
