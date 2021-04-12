from random import randint
from time import sleep

attempt = 0
guess = 0
answer = randint(0,100)
print("Entering network...")
sleep(3)
print("Done")
print("Hacking system...")
sleep(3)
print("Done")
sleep(1)
print("Posible codes: 0-100")
sleep(1)
print("Attempts before system catches on: 10")
sleep(1)
while attempt < 10:
    print(f"Failed attempts: {attempt}")
    guess = int(input("Input code: "))
    if guess == answer:
        break
    elif guess > answer:
        print("Evaluation: to high")
    elif guess < answer:
        print("Evaluation: to low")
    attempt += 1
sleep(1)
if answer == guess:
    print("Acces aquired.")
    sleep(0.5)
    print("Downloading information...")
    sleep(2)
    print("Done")
    inf = open("info.txt","w")
    inf.write("You win!")
    inf.close()
else:
    print("Acces denied.")