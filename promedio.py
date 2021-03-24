materia = input("Materia: ")
n = int(input("Numero de bimestres: "))
s = 0
for i in range(n):
    s += int(input(f"Bimestre #{i+1}: "))
s /= n
print(f"Promedio de {materia}: {s}")