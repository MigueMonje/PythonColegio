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
num = int(input("Numero: "))
unit1 = units[input("Unidad de entrada (abreviada): ").lower()]
unit2 = units[input("Unidad de salida (abreviada): ").lower()]
conv = unit1/unit2
print(num*conv)