import random
import os

def matriz_imagen_aleatoria(piezas):
    filas = len(piezas)
    columnas = len(piezas[0])
    piezas_flat = [pieza for fila in piezas for pieza in fila]
    random.shuffle(piezas_flat)
    matriz = []
    for i in range(filas):
        fila = piezas_flat[i * columnas: (i + 1) * columnas]
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    """Muestra la matriz del rompecabezas en pantalla."""
    for fila in matriz:
        print('|'.join([os.path.basename(p) if p != '-' else '-' for p in fila]))
    print()
