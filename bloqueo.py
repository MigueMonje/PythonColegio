from time import sleep
# Contraseña e input del usuario
password = "1234"
guess = ""
# Mientras que el usuario no ponga la contraseña correcta
while guess != password:
    # Mientras tenga intentos
    attempt = 0
    while attempt < 3:
        # Conseguir el input
        guess = input("Contraseña: ")
        # Si es correcto salir del bucle
        if guess == password:
            attempt = 3
        # Si no, perder un intento
        else:
            attempt += 1
    # Si despues de perder 3 veces no lo logra
    if password != guess:
        # Bloquearse por 30 segundos
        print("Espera 30 segundos...")
        sleep(30) 