def calculate_tax(income):
    """
    Calculates income tax at a flat rate of 16%.
    """
    return income * 0.16

def main():
    print("========================================")
    print("Welcome to the Income Tax Calculator")
    print("========================================")
    print("Type 'quit' or 'q' at any time to exit.\n")
    
    while True:
        user_input = input("Enter your annual income (in ₹): ").strip()
        
        if user_input.lower() in ['quit', 'q', 'exit']:
            print("Exiting calculator. Goodbye!")
            break
            
        try:
            # Remove commas if any, to parse the float properly
            income = float(user_input.replace(',', ''))
            if income < 0:
                print("Error: Income cannot be negative. Please try again.\n")
                continue
                
            tax = calculate_tax(income)
            net_income = income - tax
            
            effective_rate = (tax / income) * 100 if income > 0 else 0
            
            print("\n--- Tax Calculation Summary ---")
            print(f"Annual Income:      ₹ {income:,.2f}")
            print(f"Total Tax:          ₹ {tax:,.2f}")
            print(f"Net Income:         ₹ {net_income:,.2f}")
            print(f"Effective Tax Rate: {effective_rate:.2f}%\n")
            
        except ValueError:
            print("Error: Invalid input. Please enter a numerical value for your income.\n")

if __name__ == "__main__":
    main()
