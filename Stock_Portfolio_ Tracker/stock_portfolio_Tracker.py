# Stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 200,
    "MSFT": 300
}

total = 0

print("📈 Stock Portfolio Tracker")
print("--------------------------")

while True:
    stock = input("Enter Stock Name (AAPL, TSLA, GOOGLE, AMZN, MSFT): ").upper()

    if stock not in stock_prices:
        print("❌ Stock not available.")
        continue

    quantity = int(input("Enter Quantity: "))

    value = stock_prices[stock] * quantity
    total += value

    print(f"{stock} Investment = ${value}")

    choice = input("Do you want to add another stock? (yes/no): ").lower()

    if choice == "no":
        break

print("\n✅ Total Investment = $", total)

# Save result to a file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment: ${total}")

print("📁 Result saved in portfolio.txt")