epsilon = 1e-6
summa = 0.0
term = 1.0
n = 0

while term > epsilon:
    summa += term
    term /= 2
    n += 1

print(f"Summan blir ungefär {summa}")
print(f"Antal termer: {n}")