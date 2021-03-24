import random
# Configuracion del juago
config = {
    "limitedAtempts": False,
    "atempts": 10,
    "from": 1,
    "to": 100
}

# Si el usario quiere cambiar la configuarcion...
if input("Options? (y/n): ")[0] == "y":
    # Cambiarla con los inputs apropiados
    config["limitedAtempts"] = input("Limited Attempts? (y/n): ")[0] == "y"
    if config["limitedAtempts"]:
        config["atempts"] = int(input("Number of atempts: "))
    config["from"] = int(input("Miminum Number: "))
    config["to"] = int(input("Maximum Number: "))

# Numero de la computadora
mNumber = random.randint(config["from"],config["to"])
# Numero del jugador
pNumber = -1
# Numero de intentos
attempts = config["atempts"]

# Repetir mientras el jugador no adivine correctamente y aun tenga intentos
while (pNumber != mNumber) and (attempts > 0):
    # Conseguir el numero del jugador
    pNumber = int(input("Guess number: "))
    # Desir si el numero es demaciado alto o bajo
    if pNumber > mNumber:
        print("to high")
    elif pNumber < mNumber:
        print("to low")
    # Si tiene intentos limitados bajar el numero de intentos
    if config["limitedAtempts"]:
        attempts -= 1
        print(f"Atempts left: {attempts}")
# Desir si ganó o perdio
if pNumber == mNumber:
    print("yes")
else:
    print("no")