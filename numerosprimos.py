def listmult(a,l):
    """ Ver si lista l contiene almenos UN multiplo de a"""
    for i in l:
        if a % i ==0:
            return True
    return False
def funclist(l,func):
    """
    Aplicar funcion func a cada miembro de la lista l
    """
    return [func(i) for i in l]

# Numeros primos encontrados
primes = []
# Entrada del usuario
upto = int(input(">> "))
# Por cada numero menor de la entrada del usuario...
for i in range(upto):
    # Si el numero es mayor que 1
    if i > 1:
        # y no es un multiplo de ninguno de los primos ya encontrados
        if not listmult(i,primes):
            # Añadirlo a la lista
            primes += [i]
# Imprimir la lista con saltos de linea entre cada numero
print("\n".join(funclist(primes,str)))
