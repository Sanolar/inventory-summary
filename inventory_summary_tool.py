import csv

# Input
products = [
    {"name": "Apples", "qty": 12, "price": 1.5},
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