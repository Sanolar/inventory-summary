import csv

CSV_FILE = "inventory.csv"

def load_inventory():
    with open(CSV_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        return [
            {
                "name": row["Product Name"],
                "quantity": int(row["Quantity"]),
                "price": float(row["Price Per Unit"])
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
