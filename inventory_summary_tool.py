import csv
import os
from datetime import datetime

INVENTORY_FILE = "inventory.csv"
SALES_FILE = "sales.csv"
LOW_STOCK_THRESHOLD = 5

# Ensure CSV files exist
def ensure_files_exist():
    if not os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "qty", "price"])
    if not os.path.exists(SALES_FILE):
        with open(SALES_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "name", "qty_sold", "total_price"])

# Load inventory from file
def load_inventory():
    with open(INVENTORY_FILE, newline="") as f:
        return list(csv.DictReader(f))

# Save updated inventory
def save_inventory(products):
    with open(INVENTORY_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "qty", "price"])
        writer.writeheader()
        for p in products:
            writer.writerow(p)

# Display inventory with total value
def display_inventory():
    products = load_inventory()
    total_value = 0
    print("\n📦 INVENTORY STATUS")
    print("{:<15} {:<10} {:<10}".format("Product", "Quantity", "Price"))
    for p in products:
        qty = int(p["qty"])
        price = float(p["price"])
        total_value += qty * price
        status = "🔴 Low stock" if qty < LOW_STOCK_THRESHOLD else ""
        print(f"{p['name']:<15} {qty:<10} ${price:<10.2f} {status}")
    print(f"\n💰 Total Inventory Value: ${total_value:.2f}")

# Add or update product
def add_or_update_product():
    products = load_inventory()
    name = input("Enter product name: ").strip()
    qty = int(input("Enter quantity: "))
    price = float(input("Enter unit price: "))

    for p in products:
        if p["name"].lower() == name.lower():
            p["qty"] = str(int(p["qty"]) + qty)
            p["price"] = str(price)
            break
    else:
        products.append({"name": name, "qty": str(qty), "price": str(price)})

    save_inventory(products)
    print(f"✅ '{name}' added or updated successfully.")

# Record a sale and update stock
def record_sale():
    products = load_inventory()
    sale_total = 0
    sales = []

    while True:
        name = input("Enter product sold (or 'done'): ").strip()
        if name.lower() == "done":
            break

        qty_sold = int(input(f"Enter quantity sold for {name}: "))
        for p in products:
            if p["name"].lower() == name.lower():
                if int(p["qty"]) < qty_sold:
                    print("❌ Not enough stock.")
                    break
                p["qty"] = str(int(p["qty"]) - qty_sold)
                total = qty_sold * float(p["price"])
                sale_total += total
                sales.append([datetime.now().isoformat(), name, qty_sold, total])
                print(f"✅ Sold {qty_sold} x {name} (${total:.2f})")
                break
        else:
            print("❌ Product not found.")

    save_inventory(products)
    with open(SALES_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        for s in sales:
            writer.writerow(s)
    print(f"\n🧾 Total Sale: ${sale_total:.2f}")

# CLI Menu
def main_menu():
    while True:
        print("\n=== INVENTORY TOOL ===")
        print("1. View Inventory")
        print("2. Add or Update Product")
        print("3. Record Sale")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            display_inventory()
        elif choice == "2":
            add_or_update_product()
        elif choice == "3":
            record_sale()
        elif choice == "4":
            print("👋 Exiting.")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    ensure_files_exist()
    main_menu()
