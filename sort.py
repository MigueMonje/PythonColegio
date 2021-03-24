from random import randint,shuffle
# Crear la lista y mesclarla
lint = list(range(1000))
shuffle(lint)
print(*lint)

def bubblesort(linput):
    """
        Ordenar una lista usando el algoritmo Bubblesort.
    """
    l = [i for i in linput]
    finish = False
    while not finish:
        finish = True
        i = 0
        while i < len(l):
            if (i + 1) < len(l):
                if l[i] > l[i+1]:
                    finish = False
                    l[i],l[i+1] = l[i+1],l[i]
            i += 1
    return l

def quicksort(l, pivot = None):
    """
        Ordenar una lista usando el algoritmo Quicksort.
    """
    if not pivot:
        pivot = l[randint(0,len(l)-1)]
        
    a = []
    b = []
    for e in l:
        if e < pivot:
            a.append(e)
        else:
            b.append(e)
    

    if len(a) > 1:
        a = quicksort(a)
    if len(b) > 1:
        b = quicksort(b)
    return a + b

# Ordenar la lista (aqui se puede cambiar cual algoritmo usar)
lint = quicksort(lint)
print("---------------------------------------------")
print(*lint)
