
n = int(input("Cuantos numeros: "))
s = 0
for i in range(n):
    s += int(input(f"#{i+1}: "))
s /= n
print(f"Promedio es: {s}")
