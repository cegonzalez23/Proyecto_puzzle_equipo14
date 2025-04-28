import random

def matriz_aleatoria(cant_colum_filas):
    letras = [chr(ord('a') + i) for i in range(cant_colum_filas * cant_colum_filas - 1)]
    letras.append('-')
    random.shuffle(letras)

    matriz = []
    for i in range(cant_colum_filas):
        fila = letras[i * cant_colum_filas: (i + 1) * cant_colum_filas]
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    """Muestra la matriz del rompecabezas en pantalla."""
    for fila in matriz:
        print('|'.join(fila))
    print()
