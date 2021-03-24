try:
    # Conseguir la edad
    edad = int(input("Edad: "))
except ValueError:
    # Si se escribe un texto en luguar de un numero se ejecuta este codigo
    print("Si")
    quit()

# Imprimir el grupo de edad al que pertenese el usuario
print("Eres un ",end="")
if edad >= 65:
    print("Adulto Mayor")
elif edad >= 18:
    print("Mayor de Edad")
else:
    print("Menor de edad")