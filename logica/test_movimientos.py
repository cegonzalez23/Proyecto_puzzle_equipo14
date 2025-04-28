# pruebas/test_movimientos.py
from logica.matriz import mostrar_matriz
from logica.movimientos import mover

def pruebas_movimientos():
    print("Iniciando pruebas básicas...")
    matriz_prueba = [
        ['a', 'b', 'c'],
        ['d', '-', 'f'],
        ['g', 'h', 'i']
    ]
    mostrar_matriz(matriz_prueba)

    print("Mover izquierda (a):")
    mover(matriz_prueba, 'a')
    mostrar_matriz(matriz_prueba)

    print("Mover abajo (s):")
    mover(matriz_prueba, 's')
    mostrar_matriz(matriz_prueba)

    print("Mover derecha (d):")
    mover(matriz_prueba, 'd')
    mostrar_matriz(matriz_prueba)

    print("Mover arriba (w):")
    mover(matriz_prueba, 'w')
    mostrar_matriz(matriz_prueba)
