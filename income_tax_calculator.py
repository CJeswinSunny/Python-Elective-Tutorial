def calculate_tax(income):
    """
    Calculates the income tax based on a progressive tax bracket system.
    """
    # Define tax brackets as (upper_bound, tax_rate)
    # 'None' as the upper_bound implies the top bracket (infinity)
    brackets = [
        (10000, 0.0),    # 0% tax on the first $10,000
        (50000, 0.10),   # 10% tax on income between $10,001 and $50,000
        (100000, 0.20),  # 20% tax on income between $50,001 and $100,000
        (None, 0.30)     # 30% tax on everything over $100,000
    ]
    
    tax = 0.0
    previous_bound = 0
    
    for bound, rate in brackets:
        if bound is None:
            # Reached the top bracket
            tax += (income - previous_bound) * rate
            break
        
        if income > bound:
            # If the income is greater than the current bracket's upper bound,
            # we tax the maximum amount for this specific bracket.
            tax += (bound - previous_bound) * rate
            previous_bound = bound
        else:
            # If the income falls within the current bracket, 
            # we just tax the remaining amount above the previous bound.
            tax += (income - previous_bound) * rate
            break
            
    return tax

def main():
    print("--- 💰 Income Tax Calculator ---")
    print("Note: This uses a sample progressive tax bracket system.")
    print(" $0 - $10,000: 0%")
    print(" $10,001 - $50,000: 10%")
    print(" $50,001 - $100,000: 20%")
    print(" Over $100,000: 30%\n")

    while True:
        try:
            user_input = input("Enter your annual income (or 'q' to quit): $")
            
            if user_input.lower() == 'q':
                print("Exiting calculator. Goodbye!")
                break
                
            income = float(user_input.replace(',', '')) # Allow commas in input
            
            if income < 0:
                print("Income cannot be negative. Please try again.\n")
                continue
                
            tax = calculate_tax(income)
            net_income = income - tax
            effective_tax_rate = (tax / income * 100) if income > 0 else 0
            
            print("-" * 30)
            print(f"Gross Income:       ${income:,.2f}")
            print(f"Total Tax:          ${tax:,.2f}")
            print(f"Net Income:         ${net_income:,.2f}")
            print(f"Effective Tax Rate: {effective_tax_rate:.1f}%")
            print("-" * 30 + "\n")
            
        except ValueError:
            print("Invalid input. Please enter a valid numerical value.\n")

if __name__ == "__main__":
    main()
