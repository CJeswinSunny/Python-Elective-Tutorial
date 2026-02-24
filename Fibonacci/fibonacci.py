def fibonacci(n):
    """
    Prints the Fibonacci sequence up to n terms.
    """
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print() 

if __name__ == "__main__":
    try:
        terms = int(input("Enter the number of terms: "))
        if terms <= 0:
            print("Please enter a positive integer.")
        else:
            print(f"Fibonacci sequence up to {terms} terms:")
            fibonacci(terms)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
