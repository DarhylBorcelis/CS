
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
