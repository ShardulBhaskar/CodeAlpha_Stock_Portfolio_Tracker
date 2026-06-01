# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

num_stocks = int(input("\nHow many different stocks do you own? "))

# Input portfolio
for i in range(num_stocks):
    stock_name = input(f"\nEnter stock {i+1} name: ").upper()

    if stock_name not in stock_prices:
        print("Stock not available in database.")
        continue

    quantity = int(input(f"Enter quantity of {stock_name}: "))

    portfolio[stock_name] = quantity

# Calculate total investment
print("\n===== PORTFOLIO SUMMARY =====")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_investment += value

    print(
        f"{stock} | Price: ${stock_prices[stock]} | "
        f"Quantity: {quantity} | Value: ${value}"
    )

print(f"\nTotal Investment Value = ${total_investment}")

# Optional file saving
save = input("\nDo you want to save the report? (yes/no): ").lower()

if save == "yes":
    filename = "portfolio_report.txt"

    with open(filename, "w") as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("----------------------\n")

        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            file.write(
                f"{stock} | Price: ${stock_prices[stock]} | "
                f"Quantity: {quantity} | Value: ${value}\n"
            )

        file.write(f"\nTotal Investment Value = ${total_investment}")

    print(f"Report saved successfully in '{filename}'")