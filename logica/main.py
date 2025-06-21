from configuracion import obtener_tamaño
from importe_imagenes import partir_imagen
from matriz import matriz_imagen_aleatoria, mostrar_matriz
from movimientos import mover

def jugar_rompecabezas_con_imagen():
    tamaño = obtener_tamaño()
    ruta_imagen = input("Ingrese la ruta de la imagen (por ejemplo, 'mi_imagen.png'): ")
    piezas = partir_imagen(ruta_imagen, tamaño, tamaño)
    matriz = matriz_imagen_aleatoria(piezas)

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
    jugar_rompecabezas_con_imagen()
