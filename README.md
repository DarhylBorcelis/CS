# 🏪 Store Products Manager – Python Program

This is a simple **console-based Python program** to:
- Add products with an **auto-generated ID**.
- Search for products by **name** or **ID**.
- Show **all products**.
- Exit the program.

It’s a beginner-friendly project for learning **lists, loops, and functions in Python**.

---

## 📌 Features

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
   - Example search:
     ```
     Enter the Product Name or ID to search: LAPTOP
     ID: [20250001] Name: [LAPTOP] Category: [GADGET]
     ```

3. **Clear Screen**
   - Clears the console and shows the menu again.

4. **Exit**
   - Closes the program.

---

## 📂 Code
```python
import os
data = []

def add_data():
    ID = len(data) + 20250000
    name = input("Product Name: ").upper()
    category = input("Category (Gadget, Clothing, or Food): ").upper()

    if category not in ['GADGET', 'CLOTHING', 'FOOD']:
        print("Invalid category. Please enter 'Gadget', 'Clothing', or 'Food'.")
        return

    data.append([ID, name, category])
    print(f"Product added! ID: {ID}, Name: {name}, Category: {category}")

def search_data():
    show = input('Show all Products? y/n: ').lower()
    num = 0
    if show == 'y':
        print("***All Products***")
        for x in data:
            num += 1
            print(f"{num} ID: [{x[0]}] Name: [{x[1]}] Category: [{x[2]}]")
    else:
        con = input("Enter the Product Name or ID to search: ").upper()
        found = False
        for x in data:
            if con == str(x[0]) or con == x[1]:
                print(f"ID: [{x[0]}] Name: [{x[1]}] Category: [{x[2]}]")
                found = True
        if not found:
            print("No matching product found.")

while True:
    print("\n******** Store Products Menu ********")
    print("1. Add Product")
    print("2. Search Product")
    print("3. Clear (Show Menu Again)")
    print("4. Exit Program")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_data()
    elif choice == '2':
        search_data()
    elif choice == '3':
        os.system('cls')
        continue
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

---

## 📌 What is the Bisection Method?

The **Bisection Method** is a numerical technique to find where a function equals **0**.  
It works by:
1. Picking two points **a** and **b** where the function values have opposite signs.
2. Cutting the interval in half.
3. Choosing the half that contains the root.
4. Repeating until the answer is close enough (based on the tolerance).

---

## 🚀 How It Works
1. **User Input:**
   - `Tolerance` → How close to zero you want the answer (e.g., `0.01`).
   - `a` → Start of the range.
   - `b` → End of the range.
   
2. **Check**:
   - If `f(a)` and `f(b)` have the same sign → no root in the range.
   - If different signs → start the search.

3. **Loop**:
   - Find midpoint `c = (a + b) / 2`.
   - If `|f(c)| < tolerance` → root found.
   - Otherwise, keep the half of the range where the sign changes.

---

## 📂 Code
```python
print("")
print("***Numerical Analysis → Root-Finding Algorithms***")

tolerance = float(input("Tolerance only start from 0.01: "))
a = float(input("Start a: "))
b = float(input("Start b: "))
i = 0

def f(x):
    return x**3 - x - 2

if f(a) * f(b) >= 0:
    print("No root in this range.")
else:
    while True:
        i += 1
        c = (a + b) / 2
        fc = f(c)
        if abs(fc) < tolerance:
            print(f"Root: {c:.6f} in {i} iterations.")
            break
        if f(a) * fc < 0:
            b = c
        else:
            a = c
