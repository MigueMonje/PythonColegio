from time import sleep
password = "1234"
guess = ""
while guess != password:
    attempt = 0
    while attempt < 3:
        guess = input("Contraseña: ")
        if guess == password:
            attempt = 3
        else:
            attempt += 1
    if password != guess:
        print("Espera 30 segundos...")
        sleep(30) 