# 🧮 Inventory Summary Tool

This is a command-line + API tool that helps you manage a basic inventory of products and record sales.

---

## 📦 What It Does

- Add or update products (CLI or API)
- View inventory and total stock value
- Highlights products with low stock (less than 5)
- Record product sales and update inventory
- Export inventory and sales to CSV files
- Use as an interactive CLI or REST API

---

## 🛠 How to Run

### ▶️ CLI Mode

```bash
python3 inventory_summary_tool.py
```

### 🌐 API Mode (Flask)

```bash
python3 inventory_summary_tool.py --api
```

Open your browser or Postman to test endpoints.

---

## 🔗 API Endpoints

### 📥 Add Product

`POST /inventory-summary/add`

**Body (JSON):**
```json
{ "name": "Apple", "qty": 10, "price": 0.75 }
```

---

### 📦 View Inventory

`GET /inventory-summary`

Returns JSON array of inventory items.

---

### 🛒 Record Sale

`POST /inventory-summary/sell`

**Body (JSON):**
```json
{
  "items": [
    { "name": "Apple", "qty": 2 },
    { "name": "Orange", "qty": 1 }
  ]
}
```

---

### ❌ Delete Product

`DELETE /inventory-summary/delete/<name>`

Example:
```
DELETE /inventory-summary/delete/Apple
```

---

### 📊 Inventory Summary

`GET /inventory-summary/summary`

Returns:
```json
{
  "total_inventory_value": 250.0,
  "low_stock_items": 2,
  "total_products": 5
}
```

---

### 🧾 Sales Report

`GET /sales-report`

Returns array of all sales from `sales.csv`.

---

## 📁 File Structure

- `inventory_summary_tool.py` – Main tool file
- `inventory.csv` – Inventory data
- `sales.csv` – Sales records

---

## 💡 Tips

- Use Postman or your browser to test the GET endpoints.
- Use `raw JSON` in Postman when sending POST/DELETE requests.

## 👨‍💻 Author

Built with ❤️ by [Sanolar](https://github.com/Sanolar)
