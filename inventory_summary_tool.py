import csv

# Input
products = [
    {"name": "Apples", "qty": 10, "price": 1.5},
    {"name": "Bananas", "qty": 2, "price": 0.5},
    {"name": "Oranges", "qty": 0, "price": 0.8},
]

LOW_STOCK_THRESHOLD = 5

# Output
total_value = sum(p["qty"] * p["price"] for p in products)
low_stock = [p for p in products if p["qty"] < LOW_STOCK_THRESHOLD]

print(f"Total Inventory Value: ${total_value:.2f}")
print("Low Stock Items:")
for p in low_stock:
    print(f"- {p['name']} (Qty: {p['qty']})")

# Bonus: Save to CSV
with open("inventory_summary.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Quantity", "Price per Unit"])
    for p in products:
        writer.writerow([p["name"], p["qty"], p["price"]])
