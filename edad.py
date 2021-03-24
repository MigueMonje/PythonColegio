try:
    edad = int(input("Edad: "))
    print("Eres un ",end="")
except ValueError:
    print("Si")
    quit()
if edad >= 65:
    print("Adulto Mayor")
elif edad >= 18:
    print("Mayor de Edad")
else:
    print("Menor de edad")