pts = int(input("Puntuacion: "))
if pts < 51:
    print("Reprovaste!")
    print(f"Falta {51-pts} puntos para aprovar.")
elif pts < 100:
    print("Aprovaste!")
    print(f"Falta {100-pts} puntos para 100.")

else:
    print("Perfecto")