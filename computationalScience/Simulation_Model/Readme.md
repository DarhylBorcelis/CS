# 🐺🐇 Predator–Prey Model (Lotka–Volterra) — Detailed Manual

After **starting the program**, you will see the title:

```
=== Predator–Prey Model ===
```

The program will then ask:

```
Enter number of years to simulate:
```

---

## 1. What the Program Does
- Simulates predator–prey population changes over time using the **Lotka–Volterra equations**.
- Prints a year-by-year population table for both prey and predator.
- Displays a population graph showing how both change during the simulation.

---

## 2. User Inputs

### Step 1 — Simulation Duration
- You will be prompted to enter a number of years (can be a decimal).
- Example:
  ```
  Enter number of years to simulate: 10
  ```
  This means the program will simulate 10 years.

---

## 3. Model Parameters (Preset in Code)
| Parameter | Meaning | Value |
|-----------|---------|-------|
| `prey_init` | Initial prey population | 1000 |
| `pred_init` | Initial predator population | 50 |
| `alpha` | Prey growth rate | 0.5 |
| `beta` | Predation rate | 0.0005 |
| `gamma` | Predator death rate | 0.5 |
| `delta` | Predator growth rate (from consuming prey) | 0.0002 |

You can edit these values **inside the code** to change the simulation behavior.

---

## 4. Program Output

### a) Yearly Table
After you enter the number of years, the program prints:

```
Year | Prey       | Predator
   0 |  1000.00   |    50.00
   1 |   980.42   |    52.10
   2 |   960.34   |    54.22
  ... (continues until last year)
```

- **Year** — Simulation year number (0 is the start).
- **Prey** — Number of prey in that year.
- **Predator** — Number of predators in that year.

---

### b) Population Graph
After printing the table, a graph window will appear:
- **Green line** = Prey population.
- **Orange line** = Predator population.
- X-axis = Time in years.
- Y-axis = Population size.

---

## 5. Example Session

```
=== Predator–Prey Model ===
Enter number of years to simulate: 5

Year | Prey       | Predator
   0 |   1000.00  |    50.00
   1 |    980.21  |    51.80
   2 |    961.23  |    53.54
   3 |    943.01  |    55.20
   4 |    925.54  |    56.79
   5 |    908.78  |    58.31
```

_A graph will pop up showing prey (green) decreasing slightly, and predators (orange) increasing._

---

## 6. Notes & Tips
- You can modify initial populations or rates to explore different predator–prey dynamics.
- Closing the graph window ends the program.

---

