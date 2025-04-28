
def encontrar_espacio(matriz):
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == '-':
                return i, j
    return None

def mover(matriz, direccion):
    """Mueve el espacio vacío ('-') en la dirección dada si es válido."""
    movimientos = {
        'w': (-1, 0),  # Subir
        's': (1, 0),   # Bajar
        'a': (0, -1),  # Izquierda
        'd': (0, 1)    # Derecha
    }

    calcular_nueva_posicion = lambda fila, columna, df, dc: (fila + df, columna + dc)

    if direccion not in movimientos:
        print("Dirección inválida. Usa 'w', 's', 'a' o 'd'.")
        return False

    fila, columna = encontrar_espacio(matriz)
    delta_fila, delta_columna = movimientos[direccion]

    nueva_fila, nueva_columna = calcular_nueva_posicion(fila, columna, delta_fila, delta_columna)

    tamaño = len(matriz)
    if 0 <= nueva_fila < tamaño and 0 <= nueva_columna < tamaño:
        matriz[fila][columna], matriz[nueva_fila][nueva_columna] = matriz[nueva_fila][nueva_columna], matriz[fila][columna]
        return True
    else:
        print("Movimiento fuera de los límites.")
        return False
