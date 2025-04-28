# main.py
from logica.configuracion import obtener_tamaño
from logica.matriz import matriz_aleatoria, mostrar_matriz
from logica.movimientos import mover

def jugar_rompecabezas():
    tamaño = obtener_tamaño()
    matriz = matriz_aleatoria(tamaño)

    print("\nConfiguración inicial del rompecabezas:")
    mostrar_matriz(matriz)

    while True:
        direccion = input("Mover (w=arriba, s=abajo, a=izquierda, d=derecha, x=Salir del juego): ").strip().lower()
        if direccion == 'x':
            print("¡Gracias por jugar!")
            break
        mover(matriz, direccion)
        mostrar_matriz(matriz)

if __name__ == "__main__":
    jugar_rompecabezas()
