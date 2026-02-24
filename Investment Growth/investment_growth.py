# Ask the user to input the initial investment amount, annual interest rate, and number of years
investment_amount = float(input("Enter the initial investment amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (in percentage): "))
years = int(input("Enter the number of years: "))

# Print the header for the output
print(f"{'Year':<8}{'Amount'}")

amount = investment_amount
# Use a loop to calculate the amount at the end of each year
for year in range(1, years + 1):
    amount = amount + (amount * (annual_interest_rate / 100))
    # Display the year number and the amount rounded to two decimal places
    print(f"{year:<8}{amount:.2f}")
