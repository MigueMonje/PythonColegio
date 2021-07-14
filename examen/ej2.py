ball = (int(input("Pelotas: ")) * 50) / 1000
doll = (int(input("Muñecas: ")) * 100) / 1000
w = ball + doll
print(f"Peso: {w}")
if w >= 15:
    print("Descuento: 10%")
else:
    print("Descuento: 0")