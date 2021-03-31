# Diccionario semaforo
semaforo = {
    "rojo": "Parar",
    "amarillo": "Precausion",
    "verde": "Pasar"
}
# Color del usuario
color = input("Color: ").lower()
# Imprimir resultado
print(semaforo[color])