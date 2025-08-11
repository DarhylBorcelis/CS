from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


def lotka_volterra(state, t, alpha, beta, gamma, delta):
    prey, predator = state
    dprey_dt = alpha * prey - beta * prey * predator
    dpred_dt = delta * prey * predator - gamma * predator
    return [dprey_dt, dpred_dt]


print(" ")
print("=== Predator–Prey Model ===")
t_max = float(input("Enter number of years to simulate: "))

prey_init = 1000       # initial prey population
pred_init = 50         # initial predator population
alpha = 0.5            # prey growth rate
beta = 0.0005          # predation rate
gamma = 0.5            # predator death rate
delta = 0.0002         # predator growth rate

steps = 500
t = np.linspace(0, t_max, steps)

solution = odeint(lotka_volterra, [prey_init, pred_init], t, args=(
    alpha, beta, gamma, delta))
prey = solution[:, 0]
predator = solution[:, 1]

print("\nYear | Prey       | Predator")
for year in range(int(t_max) + 1):
    if year == int(t_max):
        idx = -1
    else:
        idx = int(year * steps / t_max)
    print(f"{year:4d} | {prey[idx]:10.2f} | {predator[idx]:10.2f}")

plt.figure(figsize=(10, 6))
plt.plot(t, prey, label="Prey Population", color="green")
plt.plot(t, predator, label="Predator Population", color="orange")
plt.xlabel("Time (years)")
plt.ylabel("Population")
plt.title("Predator–Prey Model (Lotka–Volterra)")
plt.legend()
plt.grid(True)
plt.show()
