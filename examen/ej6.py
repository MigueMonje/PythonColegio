n = int(input("Numero: "))
p = "impar"
if n % 2 == 0:
    p = "par"
print(f"Es: {p}")
m = "no"
if n % 17 == 0:
    m = "si"
print(f"Multiplo de 17: {m}")
