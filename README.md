# 📦 Inventory Summary Tool

The Inventory Summary Tool is a web-based application built with FastAPI (backend) and HTML, CSS, JavaScript (frontend) that allows businesses to manage inventory, record sales, track stock levels, and generate sales receipts dynamically.

---

## ✅ Features

- **Role-Based Access Control**
   
   - **Admin**: Update inventory (add/modify products) and record sales.
   - **Sales Rep**: Record sales and view inventory only.

- **Inventory Management**

   - Add or update products with name, quantity, and price.
   - View real-time inventory in a tabular format.

- **Sales Recording**

   - Record product sales.
   - Auto-update inventory after sales.

- **Sales Receipt**

   - Displays after each sale:
      - Date & time of transaction.
      - Product name, quantity, price, and total.
      - Out-of-stock alerts.
      - “Thank you for your purchase” note.

- **Persistent Data Storage**
   
   - Uses **CSV files**:
      - inventory.csv for inventory data.
      - sales.csv for sales history.

- **Authentication**
   - Session-based login with **bcrypt** password hashing.

- **Responsive Frontend**
   - Built with vanilla HTML, CSS, and JavaScript.
   - Includes **Logout button** and dynamic UI per role.

---

## 🗂 Project Structure

<img width="1548" height="1158" alt="image" src="https://github.com/user-attachments/assets/efe92079-6c6f-4847-b67b-bab5f3857ed9" />

---

## ⚙ Installation & Setup

**1. Clone the Repository**

git clone https://github.com/Sanolar/inventory-summary.git

cd inventory-summary

**2. Create Virtual Environment**

python3 -m venv venv

source venv/bin/activate   # macOS/Linux

venv\Scripts\activate      # Windows

**3. Install Dependencies**

pip install fastapi uvicorn passlib[bcrypt] python-multipart

---

## ▶ Run the Application

PYTHONPATH=. uvicorn app.main:app --reload

Application runs at: http://127.0.0.1:8000

  - **Frontend (Login)**: http://127.0.0.1:8000/static/login.html
  - **API Docs**: http://127.0.0.1:8000/docs

---

## 🔑 Login Credentials

Default users:
  - **Admin**: admin00 / admin1234
  - **Sales Rep**: salesrep00 / salesrep1234

---

## 💾 Database
  - **inventory.csv** → Stores product name, quantity, price.
  - **sales.csv** → Logs sales transactions with timestamp and totals.

---

## 📜 API Endpoints

| Method | Endpoint                          | Description                     |
| ------ | --------------------------------- | ------------------------------- |
| POST   | `/inventory-summary/login`        | Login user                      |
| GET    | `/inventory-summary/logout`       | Logout user                     |
| GET    | `/inventory-summary/`             | View inventory                  |
| POST   | `/inventory-summary/update`       | Add or update inventory (Admin) |
| POST   | `/inventory-summary/sale`         | Record a sale & return receipt  |
| GET    | `/inventory-summary/current_user` | Get logged-in user information  |

---

## ✅ How It Works
- **Frontend**: Displays inventory, provides forms for updating inventory and recording sales, and dynamically shows sales receipts.
- **Backend**: Handles API calls, role-based permissions, session authentication, and updates CSV files for persistence.

---

## 🎯 Future Enhancements
- Add **downloadable reports** for sales and inventory.
- Implement **database integration (SQLite/PostgreSQL)**.
- Enhance **UI design** for improved user experience.

---

## ✅ Project Completed with:
- **Backend**: FastAPI
- **Frontend**: HTML, CSS, JavaScript
- **Database**: CSV files (inventory.csv, sales.csv)
- **Authentication**: Session-based login with bcrypt hashing

