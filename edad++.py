from datetime import datetime
date = datetime.now()
print("Fecha de nacimiento: ")
birth = {
    "day":int(input("Dia: ")),
    "month":int(input("Mes (numero): ")),
    "year":int(input("Año: "))
}
age = date.year - birth["year"]
if birth["month"] > date.month:
    age -= 1
elif birth["month"] == date.month and date.day > birth["day"]:
    age -= 1
if age <= 12:
    print("Niño")
elif age <= 16:
    print("Adolecente")
elif age <= 25:
    print("Joven")
elif age <= 55:
    print("Adulto")
elif age <= 80:
    print("Tercera edad")
else:
    print("Inmortal")
