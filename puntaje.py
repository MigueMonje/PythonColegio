p = int(input("Escribe yu nota final."))
if p < 0:
    print("uhhhhh....")
elif p <= 25:
    print("Mal. estudia mas.")
elif p <= 50:
    print("Reprovaste. Debes mejorar.")
elif p <= 75:
    print("Aprovaste. Debes mejorar.")
elif p <= 100:
    print("Muy bien.")
elif p > 100:
    print("si.")