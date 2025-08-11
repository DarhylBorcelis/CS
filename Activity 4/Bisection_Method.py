import os


def f(x):
    return x**3 - x - 2


while True:
    print("")
    print("***Numerical Analysis → Root-Finding Algorithms***")

    tolerance = float(input("Tolerance only start from 0.01: "))
    a = float(input("Start a: "))
    b = float(input("Start b: "))
    i = 0

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

    con = input("Repeat? y/n: ").lower()
    if con == "n":
        break
    else:
        os.system('cls')

