def square_root(n, tolerance=1e-10):
    """
    Calculates the square root of a number using Newton's method (Babylonian method).
    """
    if n < 0:
        return "Cannot compute square root of a negative number"
    if n == 0:
        return 0.0

    # Initial guess
    guess = n / 2.0 if n > 1 else 1.0

    while True:
        next_guess = 0.5 * (guess + n / guess)
        # If the difference between the next guess and the current guess is less than the tolerance,
        # we have found the square root to our desired precision.
        if abs(guess - next_guess) < tolerance:
            return next_guess
        guess = next_guess

if __name__ == "__main__":
    try:
        num = float(input("Enter a number to find its square root: "))
        result = square_root(num)
        if isinstance(result, str):
            print(result)
        else:
            print(f"The square root of {num} is approximately {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
