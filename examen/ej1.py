from datetime import datetime
date = datetime.now()
print(f"Bienvenido, {input('Nombre: ')}.")
print("Fecha en la que empeso a trabajar: ")
birth = {
    "day":int(input("Dia: ")),
    "month":int(input("Mes (numero): ")),
    "year":int(input("Año: "))
}
t = date.year - birth["year"]

print(f"Trabajado: {t}años\nBono: {1000 if t > 10 else 0}bs")