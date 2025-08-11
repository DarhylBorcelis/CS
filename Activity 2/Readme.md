# 🐇🐺 Predator–Prey Model (Lotka–Volterra Equations)
---------------------------------------------------
This program simulates predator–prey population dynamics over time using the Lotka–Volterra equations.
It calculates values numerically and displays:
- A year-by-year table
- A graph of prey vs predator populations

How It Works:
-------------
Two populations:
  - Prey (e.g., rabbits) — grows naturally but decreases when eaten by predators.
  - Predators (e.g., wolves) — decrease naturally but increase when prey is available.
The populations interact according to:
  dPrey/dt     = α * Prey − β * Prey * Predator
  dPredator/dt = δ * Prey * Predator − γ * Predator

Where:
  α = prey growth rate
  β = predation rate
  γ = predator death rate
  δ = predator growth rate from eating prey

How to Use:
-----------
1. Run the program.
2. Enter the number of years to simulate.
3. View the population table.
4. See the population graph.

Default Settings:
-----------------
  Prey initial: 1000
  Predator initial: 50
  α = 0.5
  β = 0.0005
  γ = 0.5
  δ = 0.0002

Requirements:
-------------
  pip install numpy scipy matplotlib
"""

print(manual)

# ===============================================================
