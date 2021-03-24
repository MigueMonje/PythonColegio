
def main(r):
    """
        Funcion principal
    """
    # Variables nesesarias
    last = 0
    current = 1
    # Primer print (arreglo pesimo para un bug)
    print(last)
    # Bucle que va de 0 a r
    for _ in range(r):
        # Imprimir el numero en el que se esta
        print(current)
        # Guardar el numero actual en una variable temporal
        tmplast = current
        # Añadir el numero anterior
        current += last
        # Guardar la variable temporal en el numero anterior
        last = tmplast
if __name__ == "__main__":
    main(1000)