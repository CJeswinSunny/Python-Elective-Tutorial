def get_positive_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_prime_numbers_in_range(m, n):
    if m > n:
        m, n = n, m
    
    print(f"\nPrime numbers between {m} and {n} are:")
    found_prime = False
    for num in range(m, n + 1):
        if is_prime(num):
            print(num, end=" ")
            found_prime = True
    
    print() 
    if not found_prime:
        print("No prime numbers found in this range.")

def main():
    print("--- Prime Numbers Finder ---")
    m = get_positive_integer_input("Enter the start of the range (m): ")
    n = get_positive_integer_input("Enter the end of the range (n): ")
    
    print_prime_numbers_in_range(m, n)

if __name__ == "__main__":
    main()
