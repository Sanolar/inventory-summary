import csv
import os
from datetime import datetime

INVENTORY_FILE = "inventory.csv"
SALES_FILE = "sales.csv"
LOW_STOCK_THRESHOLD = 5

def ensure_files_exist():
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
        return list(csv.DictReader(f))

def save_inventory(products):
    with open(INVENTORY_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "qty", "price"])
        writer.writeheader()
        for p in products:
            writer.writerow(p)

def modify_inventory():
    products = load_inventory()
    name = input("📝 Enter product name: ").strip()
    qty = int(input("🔢 Enter quantity to add/update: "))
    price = float(input("💵 Enter unit price: "))

    for p in products:
        if p["name"].lower() == name.lower():
            p["qty"] = str(int(p["qty"]) + qty)
            p["price"] = str(price)
            print(f"✅ Updated '{name}' with new quantity and price.")
            break
    else:
        products.append({"name": name, "qty": str(qty), "price": str(price)})
        print(f"🆕 Added new product '{name}' to inventory.")

    save_inventory(products)

def record_sale():
    products = load_inventory()
    sale_total = 0
    sale_log = []

    while True:
        name = input("🛒 Enter product sold (or 'done'): ").strip()
        if name.lower() == "done":
            break
        qty_sold = int(input(f"🔢 Quantity sold for '{name}': "))
        for p in products:
            if p["name"].lower() == name.lower():
                if int(p["qty"]) < qty_sold:
                    print(f"❌ Not enough stock for '{name}' (available: {p['qty']})")
                    break
                p["qty"] = str(int(p["qty"]) - qty_sold)
                total = qty_sold * float(p["price"])
                sale_total += total
                sale_log.append([datetime.now().isoformat(), name, qty_sold, total])
                print(f"✅ Sold {qty_sold} of '{name}' for ${total:.2f}")
                break
        else:
            print("❌ Product not found.")

    save_inventory(products)
    with open(SALES_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        for entry in sale_log:
            writer.writerow(entry)

    print(f"🧾 Total sale amount: ${sale_total:.2f}")

def display_inventory():
    products = load_inventory()
    total_value = 0
    print("\n📦 INVENTORY STATUS")
    print("{:<15} {:<10} {:<10}".format("Product", "Quantity", "Price"))
    print("-" * 35)
    for p in products:
        qty = int(p["qty"])
        price = float(p["price"])
        total_value += qty * price
        low = "🔴 LOW" if qty < LOW_STOCK_THRESHOLD else ""
        print(f"{p['name']:<15} {qty:<10} ${price:<10.2f} {low}")
    print(f"\n💰 Total Inventory Value: ${total_value:.2f}")

def main_menu():
    while True:
        print("\n📊 === INVENTORY TOOL MENU ===")
        print("1️⃣  Modify Inventory (Add/Update)")
        print("2️⃣  Record a Sale")
        print("3️⃣  View Inventory Status")
        print("4️⃣  Exit")
        choice = input("👉 Choose an option (1-4): ").strip()

        if choice == "1":
            modify_inventory()
        elif choice == "2":
            record_sale()
        elif choice == "3":
            display_inventory()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    ensure_files_exist()
    main_menu()
