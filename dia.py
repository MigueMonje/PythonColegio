dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miercoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sabado",
    7: "Domigo"
}
d = int(input("Dia #: "))
if d in dias:
    print(f"El dia es {dias[d]}")
else:
    print("no")