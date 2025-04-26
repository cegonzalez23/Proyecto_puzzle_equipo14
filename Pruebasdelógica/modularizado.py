
#MODULARIZADO
import random

def pedir_tamano():
    try:
        tamano = int(input("Ingresar cantidad de columnas/filas del rompecabezas, hasta 5: "))
    except ValueError:
        print("Entrada no válida. Se establece configuración predeterminada (3x3).")
        return 3

    if tamano > 5 or tamano < 2:
        print("No es posible esa configuración. Se establece configuración predeterminada (3x3).")
        return 3
    return tamano

def generar_letras(tamano):
    letras = [chr(ord('a') + i) for i in range(tamano * tamano - 1)]
    letras.append('-')  # espacio vacío
    random.shuffle(letras)  # Mezclado aleatorio
    return letras

def cargar_matriz(letras, tamano):
    matriz = []
    pos = 0
    for _ in range(tamano):
        fila = []
        for _ in range(tamano):
            fila.append(letras[pos])
            pos += 1
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(' | '.join(fila))
    print()

def encontrar_espacio_usado(matriz):
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == '-':
                return i, j
    return None

def mover(matriz, direccion):
    fila, columna = encontrar_espacio_usado(matriz)
    nueva_fila, nueva_columna = fila, columna

    if direccion == 'w':
        nueva_fila -= 1
    elif direccion == 's':
        nueva_fila += 1
    elif direccion == 'a':
        nueva_columna -= 1
    elif direccion == 'd':
        nueva_columna += 1
    else:
        print("Dirección inválida.")
        return False

    tamano = len(matriz)
    if 0 <= nueva_fila < tamano and 0 <= nueva_columna < tamano:
        matriz[fila][columna], matriz[nueva_fila][nueva_columna] = matriz[nueva_fila][nueva_columna], matriz[fila][columna]
        return True
    else:
        print("Movimiento fuera de los límites.")
        return False

def pedir_direccion():
    while True:
        direccion = input("Mover (w=arriba, s=abajo, a=izquierda, d=derecha): ").lower()
        if direccion in ['w', 'a', 's', 'd']:
            return direccion
        print("Entrada inválida. Usá solo 'w', 'a', 's' o 'd'.")

def rompecabezas_resuelto(matriz):
    tamano = len(matriz)
    orden_correcto = [chr(ord('a') + i) for i in range(tamano * tamano - 1)]
    orden_correcto.append('-')
    plano = [pieza for fila in matriz for pieza in fila]
    return plano == orden_correcto

def jugar_rompecabezas():
    tamano = pedir_tamano()
    letras = generar_letras(tamano)
    matriz = cargar_matriz(letras, tamano)

    while True:
        mostrar_matriz(matriz)
        if rompecabezas_resuelto(matriz):
            print("¡Felicidades! Resolviste el rompecabezas.")
            break
        direccion = pedir_direccion()
        mover(matriz, direccion)

# Punto de entrada
if __name__ == "__main__":
    jugar_rompecabezas()
