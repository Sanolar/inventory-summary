import csv
import os
from datetime import datetime

INVENTORY_FILE = "inventory.csv"
SALES_FILE = "sales.csv"
LOW_STOCK_THRESHOLD = 5

# Ensure CSV files exist
if not os.path.exists(INVENTORY_FILE):
    with open(INVENTORY_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "qty", "price"])

if not os.path.exists(SALES_FILE):
    with open(SALES_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "name", "qty_sold", "total_price"])

def load_inventory():
    with open(INVENTORY_FILE, newline="") as f:
        reader = csv.DictReader(f)
        return [dict(row) for row in reader]

def save_inventory(products):
    with open(INVENTORY_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "qty", "price"])
        writer.writeheader()
        for p in products:
            writer.writerow(p)

def update_or_add_product():
    products = load_inventory()
    name = input("Enter product name: ").strip()
    qty = int(input("Enter quantity to add/update: "))
    price = float(input("Enter unit price: "))

    for p in products:
        if p["name"].lower() == name.lower():
            p["qty"] = str(int(p["qty"]) + qty)
            p["price"] = str(price)
            break
    else:
        products.append({"name": name, "qty": str(qty), "price": str(price)})

    save_inventory(products)
    print(f"✅ Product '{name}' updated or added.")

def record_sale():
    products = load_inventory()
    sale_total = 0
    sale_items = []

    while True:
        name = input("Enter product sold (or type 'done' to finish): ").strip()
        if name.lower() == "done":
            break

        qty_sold = int(input(f"Enter quantity sold for {name}: "))

        for p in products:
            if p["name"].lower() == name.lower():
                current_qty = int(p["qty"])
                if current_qty < qty_sold:
                    print(f"⚠️ Not enough stock. Only {current_qty} left.")
                    break
                p["qty"] = str(current_qty - qty_sold)
                total_price = qty_sold * float(p["price"])
                sale_total += total_price
                sale_items.append((name, qty_sold, total_price))
                print(f"✔️ Recorded {qty_sold} x {name} (${total_price:.2f})")
                break
        else:
            print("❌ Product not found.")

    save_inventory(products)

    # Save to sales.csv
    with open(SALES_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        for name, qty_sold, total_price in sale_items:
            writer.writerow([datetime.now().isoformat(), name, qty_sold, total_price])

    print(f"\n🧾 Total Sale: ${sale_total:.2f}")1

def display_inventory():
    products = load_inventory()
    print("\n📦 INVENTORY STATUS")
    print("{:<15} {:<10} {:<10}".format("Product", "Quantity", "Price"))

    total_value = 0
    for p in products:
        qty = int(p["qty"])
        price = float(p["price"])
        total_value += qty * price

        if qty < LOW_STOCK_THRESHOLD:
            print(f"\033[91m{p['name']:<15} {qty:<10} ${price:<10.2f} 🔴 Low stock\033[0m")
        else:
            print(f"{p['name']:<15} {qty:<10} ${price:<10.2f}")

    print(f"\n💰 Total Inventory Value: ${total_value:.2f}\n")

def main_menu():
    while True:
        print("\n=== INVENTORY SUMMARY TOOL ===")
        print("1. Add/Update Products")
        print("2. Record a Sale")
        print("3. View Inventory Status")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            update_or_add_product()
        elif choice == "2":
            record_sale()
        elif choice == "3":
            display_inventory()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()