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
nElements = int(input("Numero de elementos: "))
inlist = [input(f"Elemento #{i}") for i in range(nElements)]