# 🏆 Computational science Activity

This repository contains **Activity**:

- **Act-1** → Model/Database
- **Act-2** → Simulation N/A
- **Act-3** → Bubble Sort (Ascending/Descending)
- **Act-4** → Bisection Method (Root-Finding) 
- **Act-5** → Tree bubble sort N/A
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

## ⭐ Act-2: Predator–Prey Simulation (Lotka–Volterra Model)

This activity simulates predator–prey population dynamics using the **Lotka–Volterra equations**.  
The user inputs the **number of years** to simulate, and the program:
- Calculates the populations over time using `scipy.integrate.odeint`.
- Displays a yearly population table.
- Plots a graph showing population changes.

### 📌 Features
- Fixed initial values:
  - Prey = 1000
  - Predator = 50
  - Prey growth rate = 0.5
  - Predation rate = 0.0005
  - Predator death rate = 0.5
  - Predator growth rate = 0.0002
- User only needs to enter **number of years**.
- Outputs:
  - **Table** of yearly prey & predator populations.
  - **Graph** with:
    - Green line → Prey
    - Orange line → Predator
    
---

## ⭐ Act-3: Bubble Sort (Asc/Desc)

A program that allows the user to enter numbers and sort them in **ascending** or **descending** order. 

### 📌 Features
- Accepts any number of integers from the user.
- Allows choice between:
  - `asc` → ascending order.
  - `des` → descending order.
- Option to repeat without restarting the program.
  
---


  ## ⭐ Act-4: Bisection Method

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


