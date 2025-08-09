# 🏆 Computational science Activity

This repository contains **three activity**:

- **Act-1** → Model/Database
- **Act-2** → Bisection Method (Root-Finding)  
- **Act-3** → Number Sorter (Ascending/Descending)  

---

## ⭐ Act-1: Model

A simple program to:
- Add products with an **auto-generated ID**.
- Search for products by **name** or **ID**.
- Show **all products**.
- Exit the program.

### 📌 Features
1. **Add Product**
   - Automatically generates a unique product ID starting from `20250000`.
   - Stores:
     - ID
     - Product Name
     - Product Category (Only: Gadget, Clothing, Food)
   - Example:
     ```
     Product added! ID: 20250001, Name: LAPTOP, Category: GADGET
     ```

2. **Search Product**
   - Option to:
     - Show all products.
     - Search by **Product ID** or **Product Name**.
   - Example:
     ```
     Enter the Product Name or ID to search: LAPTOP
     ID: [20250001] Name: [LAPTOP] Category: [GADGET]
     ```

3. **Clear Screen**
   - Clears the console and shows the menu again.

4. **Exit**
   - Closes the program.

---

## ⭐ Act-2: Bisection Method

The **Bisection Method** is a numerical technique to find where a function equals **0**.

### 🚀 How It Works
1. **User Input:**
   - `Tolerance` → How close to zero you want the answer (e.g., `0.01`).
   - `a` → Start of the range.
   - `b` → End of the range.
   
2. **Check:**
   - If `f(a)` and `f(b)` have the same sign → no root in the range.
   - If different signs → start the search.

3. **Loop:**
   - Find midpoint `c = (a + b) / 2`.
   - If `|f(c)| < tolerance` → root found.
   - Otherwise, keep the half of the range where the sign changes.

---

## ⭐ Act-3: Number Sorter (Asc/Desc)

A program that allows the user to enter numbers and sort them in **ascending** or **descending** order.  
Although labeled "Bubble Sort", it uses Python’s built-in `.sort()` for simplicity.

### 📌 Features
- Accepts any number of integers from the user.
- Allows choice between:
  - `asc` → ascending order.
  - `des` → descending order.
- Option to repeat without restarting the program.

### 💻 Example Run

