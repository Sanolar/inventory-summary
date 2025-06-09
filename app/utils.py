import os, csv

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
