import csv

CSV_FILE = 'inventory.csv'
LOW_STOCK_THRESHOLD = 5

def load_inventory():
    inventory = []
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            inventory.append({
                "name": row["Product Name"],
                "quantity": int(row["Quantity"]),
                "price": float(row["Price Per Unit"])
            })
    return inventory

def calculate_total_value(inventory):
    return sum(item['quantity'] * item['price'] for item in inventory)

def get_low_stock_items(inventory):
    return [item for item in inventory if item['quantity'] < LOW_STOCK_THRESHOLD]

def display_inventory(inventory):
    print(f"\n{'Product':<15} {'Qty':<5} {'Price':<8}")
    print("-" * 30)
    for item in inventory:
        print(f"{item['name']:<15} {item['quantity']:<5} ${item['price']:<8.2f}")
    print("-" * 30)

def main():
    print("📦 Inventory Summary Tool\n")
    inventory = load_inventory()
    display_inventory(inventory)

    total_value = calculate_total_value(inventory)
    print(f"💰 Total Inventory Value: ${total_value:.2f}")

    low_stock = get_low_stock_items(inventory)
    if low_stock:
        print("\n⚠️  Low Stock Items:")
        display_inventory(low_stock)
    else:
        print("\n✅ No low-stock items.")

if __name__ == "__main__":
    main()
