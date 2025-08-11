# 📦 MODEL/DATABASE

A simple Python program to **add**, **search**, and **view** store products with an **auto-generated ID system**.

---

## 📜 Features

1. **Add Product**
   - Automatically generates a unique **product ID** starting from `20250000`.
   - Accepts:
     - **Product Name**
     - **Category** (Only: `Gadget`, `Clothing`, or `Food`)
   - Example:
     ```
     Product Name: Laptop
     Category (Gadget, Clothing, or Food): Gadget
     Product added! ID: 20250000, Name: LAPTOP, Category: GADGET
     ```

2. **Search Product**
   - Options:
     - Show **all products**.
     - Search by **Product Name** or **Product ID**.
   - Example search:
     ```
     Show all Products? y/n: n
     Enter the Product Name or ID to search: LAPTOP
     ID: [20250000] Name: [LAPTOP] Category: [GADGET]
     ```

3. **Clear Screen**
   - Clears the console and redisplays the menu.

4. **Exit Program**
   - Ends the application with a goodbye message.

---

## 📖 User Manual

### **1️⃣ Start the Program**
Run the script:
```bash
python store_products.py

