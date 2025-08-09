# 🏪 Model
This is a simple **Model** to:
- Add products with an **auto-generated ID**.
- Search for products by **name** or **ID**.
- Show **all products**.
- Exit the program.


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
