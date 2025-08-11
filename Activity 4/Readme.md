# 📐 Bisection Method (Root-Finding) - Manual

After **starting the program**, you will see:

```
***Numerical Analysis → Root-Finding Algorithms***
```

---

## 1. What the Program Does
- Uses the **Bisection Method** to find a root of the equation:
  ```
  f(x) = x³ - x - 2
  ```
- Repeats until you choose to exit.

---

## 2. User Steps

### Step 1 — Enter tolerance
- Controls the accuracy of the result.
- Must be `0.01` or smaller.
- Example:
  ```
  Tolerance only start from 0.01: 0.01
  ```

---

### Step 2 — Enter range values
- Enter the starting interval **a** and **b** where you believe the root exists.
- Example:
  ```
  Start a: 1
  Start b: 2
  ```

---

### Step 3 — Range validation
- If `f(a) * f(b) >= 0`, the program will output:
  ```
  No root in this range.
  ```
  and return to the main menu.
- This means the signs at `a` and `b` are the same, so the root might not be inside.

---

### Step 4 — Bisection process
- If the range is valid, the program repeatedly:
  1. Finds the midpoint `c = (a + b) / 2`
  2. Checks if `|f(c)| < tolerance`
  3. Updates either `a` or `b` depending on the sign of `f(c)`
- Continues until the root is found within the tolerance.

---

### Step 5 — Output
- When the root is found, it displays:
  ```
  Root: [value] in [iterations] iterations.
  ```
- Example:
  ```
  Root: 1.521378 in 10 iterations.
  ```

---

### Step 6 — Repeat or exit
- After each run:
  ```
  Repeat? y/n:
  ```
- Type:
  - `y` → run the program again
  - `n` → exit

---

## 3. Example Session

```
***Numerical Analysis → Root-Finding Algorithms***

Tolerance only start from 0.01: 0.01
Start a: 1
Start b: 2
Root: 1.521378 in 10 iterations.
Repeat? y/n: n
```

---

## 4. Notes
- This implementation clears the console (`os.system('cls')`) on Windows after each repeat.
- Function `f(x)` can be changed to solve a different equation.
- Works with float inputs for both range and tolerance.

