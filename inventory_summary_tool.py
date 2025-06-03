import csv

# Input
products = [
    {"name": "Apples", "qty": 12, "price": 1.5},
    {"name": "Bananas", "qty": 2, "price": 0.5},
    {"name": "Oranges", "qty": 0, "price": 0.8},
    {"name": "Grapes", "qty": 20, "price": 2.0},
    {"name": "Pineapples", "qty": 3, "price": 3.0},
    {"name": "Mangoes", "qty": 8, "price": 1.2},
    {"name": "Strawberries", "qty": 15, "price": 2.5},
    {"name": "Blueberries", "qty": 1, "price": 4.0},
    {"name": "Watermelons", "qty": 6, "price": 5.0},
    {"name": "Peaches", "qty": 10, "price": 1.8}
]

LOW_STOCK_THRESHOLD = 5

# Output
total_value = sum(p["qty"] * p["price"] for p in products)
low_stock = [p for p in products if p["qty"] < LOW_STOCK_THRESHOLD]

print(f"Total Inventory Value: ${total_value:.2f}")
print("Low Stock Items:")
for p in low_stock:
    print(f"- {p['name']} (Qty: {p['qty']})")