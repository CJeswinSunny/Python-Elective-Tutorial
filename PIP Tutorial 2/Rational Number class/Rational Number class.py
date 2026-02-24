class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
            
        # Determine the overall sign
        sign = -1 if (numerator < 0) ^ (denominator < 0) else 1
        
        # Work with absolute values
        num = abs(numerator)
        den = abs(denominator)
        
        # Reduce fraction using Euclid's Algorithm
        common_divisor = self._gcd(num, den)
        
        self.numerator = sign * (num // common_divisor)
        self.denominator = den // common_divisor

    def _gcd(self, a, b):
        """Helper method to calculate GCD using Euclid's Algorithm."""
        while b != 0:
            a, b = b, a % b
        return a

    def get_numerator(self):
        """Accessor for numerator."""
        return self.numerator

    def get_denominator(self):
        """Accessor for denominator."""
        return self.denominator

    def __str__(self):
        """String representation of the rational number."""
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if isinstance(other, Rational):
            new_num = self.numerator * other.denominator + other.numerator * self.denominator
            new_den = self.denominator * other.denominator
            return Rational(new_num, new_den)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Rational):
            new_num = self.numerator * other.denominator - other.numerator * self.denominator
            new_den = self.denominator * other.denominator
            return Rational(new_num, new_den)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Rational):
            new_num = self.numerator * other.numerator
            new_den = self.denominator * other.denominator
            return Rational(new_num, new_den)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Rational):
            # Direct comparison works because both are reduced upon initialization
            return self.numerator == other.numerator and self.denominator == other.denominator
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator < other.numerator * self.denominator
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator > other.numerator * self.denominator
        return NotImplemented


if __name__ == "__main__":
    # Get user input for first rational number
    print("Enter the first rational number:")
    num1 = int(input("Numerator: "))
    den1 = int(input("Denominator: "))
    r1 = Rational(num1, den1)

    # Get user input for second rational number
    print("\nEnter the second rational number:")
    num2 = int(input("Numerator: "))
    den2 = int(input("Denominator: "))
    r2 = Rational(num2, den2)
    
    print("\n--- Initializing & Reducing ---")
    print(f"r1 initialized to: {r1}")
    print(f"r2 initialized to: {r2}")
    
    print("\n--- Accessors ---")
    print(f"Numerator of r1: {r1.get_numerator()}")
    print(f"Denominator of r1: {r1.get_denominator()}")

    print("\n--- Arithmetic Operators Overloading ---")
    print(f"r1 + r2: {r1 + r2}")
    print(f"r1 - r2: {r1 - r2}")
    print(f"r1 * r2: {r1 * r2}")

    print("\n--- Comparison Operators Overloading ---")
    print(f"r1 == r2 : {r1 == r2}")
    print(f"r1 < r2  : {r1 < r2}")
    print(f"r1 > r2  : {r1 > r2}")
