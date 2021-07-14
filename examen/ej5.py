# Python muestra un error por si solo cuando se itenta dividir entre 0
a = int(input("Primer Numero: "))
b = int(input("Segundo Numero: "))
r = a//b
res = a%b
print(f"Resultado: {r}")
if res == 0:
    print("Exacta: Si")
else:
    print("Exacta: No")
    print(f"Resto: {res}")