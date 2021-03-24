import random

config = {
    "limitedAtempts": False,
    "atempts": 10,
    "from": 1,
    "to": 100
}

if input("Options? (y/n): ")[0] == "y":
    config["limitedAtempts"] = input("Limited Attempts? (y/n): ")[0] == "y"
    if config["limitedAtempts"]:
        config["atempts"] = int(input("Number of atempts: "))
    config["from"] = int(input("Miminum Number: "))
    config["to"] = int(input("Maximum Number: "))

mNumber = random.randint(config["from"],config["to"])
pNumber = -1
attempts = config["atempts"]
while (pNumber != mNumber) and (attempts > 0):
    pNumber = int(input("Guess number: "))
    if pNumber > mNumber:
        print("to high")
    elif pNumber < mNumber:
        print("to low")
    if config["limitedAtempts"]:
        attempts -= 1
        print(f"Atempts left: {attempts}")

if pNumber == mNumber:
    print("yes")
else:
    print("no")