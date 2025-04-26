
def mover(matriz, direccion):
    tamaño = len(matriz)
    fila, columna = encontrar_espacio(matriz)
    nueva_fila, nueva_columna = fila, columna

    if direccion == 'w': #arriba
        nueva_fila -= 1
    elif direccion == 's': #abajo
        nueva_fila += 1
    elif direccion == 'a': #izquierda
        nueva_columna -=1
    elif direccion == 'd': #derecha
        nueva_columna += 1
    else:
        print("Dirección errónea. Debés usar comandos del teclado 'w','s','a','d'.")
        return False
