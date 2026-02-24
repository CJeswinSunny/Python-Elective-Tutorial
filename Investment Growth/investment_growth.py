
investment_amount = float(input("Enter the initial investment amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (in percentage): "))
years = int(input("Enter the number of years: "))


print(f"{'Year':<8}{'Amount'}")

amount = investment_amount
for year in range(1, years + 1):
    amount = amount + (amount * (annual_interest_rate / 100))
    print(f"{year:<8}{amount:.2f}")
