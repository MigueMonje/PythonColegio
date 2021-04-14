# Todas las unidades nesesarias (el dinero es relativo a dolares y las distancias relativas a metros)
units = {
    "m":1,
    "km":1000,
    "dm":1/10,
    "cm":1/100,
    "mm":1/1000,
    "$":1,
    "bs":1/6.9,
    "€":0.84,
    
}

# Conseguir las entradas y buscarlas en las unidades
num = float(input("Numero: "))
unit1 = units[input("Unidad de entrada (abreviada): ").lower()]
unit2 = units[input("Unidad de salida (abreviada): ").lower()]

# Convertir de unit1 a unit2
conv = unit1/unit2
print(num*conv)