"""
# 🏪 Model/Database — User Manual

This program is a **Python console-based inventory manager** that allows you to:
- Add products with an **auto-generated ID**.
- Search for products by **Name** or **ID**.
- Display all products.
- Clear the console screen.
- Exit the application.

---

## 📜 Program Overview

The program maintains a **list of products** in memory while running.  
Each product record consists of:
1. **Product ID** — Auto-generated starting from `20250000` and incrementing by 1 for each product added.
2. **Product Name** — Entered by the user and stored in **uppercase**.
3. **Product Category** — Must be one of:
   - `GADGET`
   - `CLOTHING`
   - `FOOD`

Once the program ends, **all stored data is lost** since it’s not saved to a file or database.

---

## 📋 Menu Options

