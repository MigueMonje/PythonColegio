import random
def cheatsort(l):
    # Minimo y maximo
    mn = l[0]
    mx = 0
    # Datos
    data = {}
    # Por cada elemento
    for e in l:
        # Si el elemento no esta en los datos, añadirlo
        if not (e in data):
            data[e] = 0
        # Añadir uno al elemento en los datos
        data[e] += 1
        # Si es mayor que el maximo hacer que sea el maximo
        if e > mx:
            mx = e
        # Si es menor que el minimo hacer que sea el minimo
        elif e < mn:
            mn = e
    # Generar una lista basada en los datos conseguidos
    result = []
    for i in range(mn,mx+1):
        if i in data:
            result += [i]*data[i]
    return result
randlist = [random.randint(1,1000) for _ in range(1000)]
print(randlist)
sortlist = cheatsort(randlist)
print(sortlist)