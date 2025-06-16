import csv

CSV_FILE = "inventory.csv"
LOW_STOCK_THRESHOLD = 5


def load_inventory():
    with open(CSV_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        return [
            {
                "name": row["Product Name"],
                "quantity": int(row["Quantity"]),
                "price": float(row["Price Per Unit"]),
            }
            for row in reader
        ]


def save_inventory(inventory):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Product Name", "Quantity", "Price Per Unit"])
        writer.writeheader()
        for item in inventory:
            writer.writerow({
                "Product Name": item["name"],
                "Quantity": item["quantity"],
                "Price Per Unit": item["price"]
            })


def display_inventory(inventory):
    print("\n📦 Current Inventory:")
    print(f"{'Product':<15} {'Qty':<5} {'Price':<8}")
    print("-" * 32)
    for item in inventory:
        low_flag = "⚠️ " if item["quantity"] < LOW_STOCK_THRESHOLD else "✅"
        print(f"{low_flag} {item['name']:<13} {item['quantity']:<5} ${item['price']:<.2f}")
    print("-" * 32)


def modify_inventory(inventory):
    name = input("Enter product name to add/update: ").strip()
    for item in inventory:
        if item["name"].lower() == name.lower():
            quantity = int(input(f"Current qty: {item['quantity']}. Enter new quantity: "))
            price = float(input(f"Current price: ${item['price']}. Enter new price: "))
            item["quantity"] = quantity
            item["price"] = price
            print("✅ Inventory updated.")
            return inventory

    # New item
    quantity = int(input("New item! Enter quantity: "))
    price = float(input("Enter price per unit: "))
    inventory.append({"name": name, "quantity": quantity, "price": price})
    print("✅ New item added to inventory.")
    return inventory


def record_sale(inventory):
    cart = []
    print("\n🛒 Record a Sale (Enter 'done' to finish)")
    while True:
        name = input("Product name: ").strip()
        if name.lower() == "done":
            break
        qty = int(input("Quantity sold: "))
        for item in inventory:
            if item["name"].lower() == name.lower():
                if qty > item["quantity"]:
                    print("❌ Not enough stock!")
                else:
                    item["quantity"] -= qty
                    cart.append({"name": name, "qty": qty, "price": item["price"]})
                break
        else:
            print("❌ Product not found!")

    if cart:
        total = sum(x["qty"] * x["price"] for x in cart)
        print("\n🧾 Sale Summary:")
        for item in cart:
            print(f"- {item['name']}: {item['qty']} @ ${item['price']} = ${item['qty'] * item['price']:.2f}")
        print(f"\n💰 Total Sale: ${total:.2f}")
    else:
        print("No items sold.")

    return inventory


def main():
    while True:
        inventory = load_inventory()
        print("\n📊 Inventory Summary Tool")
        print("1. Modify Inventory")
        print("2. Record Sale")
        print("3. Show Inventory Status")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            inventory = modify_inventory(inventory)
            save_inventory(inventory)
        elif choice == "2":
            inventory = record_sale(inventory)
            save_inventory(inventory)
        elif choice == "3":
            display_inventory(inventory)
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")


if __name__ == "__main__":
    main()
