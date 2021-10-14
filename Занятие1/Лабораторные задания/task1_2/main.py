STAVKA = 0.13
oklad = float(input("Размер оклада? "))
nalog = oklad * STAVKA
na_ruki = oklad - nalog
print("Налог", nalog, "Зарплата", na_ruki)

