# 🧮 Inventory Summary Tool

A user-friendly command-line tool to manage your product inventory with interactive features and CSV tracking.

---

## ✅ Features

- 🛠 **Modify Inventory:** Add new products or update quantities and prices
- 🧾 **Record Sales:** Accept multiple product sales in one session and update stock
- 📦 **Inventory Status:** Display inventory list with color-highlighted low-stock warnings
- 💾 **Data Persistence:** Inventory and sales are saved in CSV files (`inventory.csv`, `sales.csv`)
- 🎨 **Interactive Terminal:** Emoji-enhanced prompts and styled output

---

## 🚀 How to Run

1. Make sure Python 3 is installed
2. Clone this repository:

```bash
git clone https://github.com/Sanolar/inventory-summary.git
cd inventory-summary
```

3. Run the tool:

```bash
python3 inventory_summary_tool.py
```

---

## 📂 Files Created

- `inventory.csv`: Stores current inventory (name, quantity, price)
- `sales.csv`: Logs product sales (date, name, qty, total price)

---

## 📸 Sample Terminal Output

```
📊 === INVENTORY TOOL MENU ===
1️⃣  Modify Inventory (Add/Update)
2️⃣  Record a Sale
3️⃣  View Inventory Status
4️⃣  Exit
```

```
📦 INVENTORY STATUS
Product         Quantity   Price     
-------------------------------
Apples          10         $0.50      
Bananas         2          $0.30      🔴 LOW

💰 Total Inventory Value: $6.10
```

---

## 👨‍💻 Author

Built with ❤️ by [Sanolar](https://github.com/Sanolar)
