############ Importe de librerías ############
import random

######### Configuración inicial #############

#Dejo seteada una funcion que va a monitorear que se ingrese las cantidades correctas de filas para la matriz. En caso de que el usuario no elija una configuración definida, le tire la matriz 3z3 por default
def obtener_tamaño():
    try:
        cant_colum_filas= int(input("Ingresar cantidad de columnas/filas el rompecabezas, hasta 5: "))
        if cant_colum_filas > 5 or cant_colum_filas < 2:
            print("Tamaño no válido. Se establecerá una configuración por defecto de 3x3")
            return 3
        return cant_colum_filas
    except ValueError:
        print("La entrada no es válida. Se establecerá una configuracion por defecto de 3x3")
        return 3

#Dejo seteada otra funcion donde generamos la matriz aleatoria para las letras

def matriz_aleatoria(cant_colum_filas):
    letras = [chr(ord('a')+i)for i in range(cant_colum_filas * cant_colum_filas-1)] #chr() convierte un número a una letra, y ord('a') devuelve el número ASCII de 'a' (que es 97).
    letras.append('-')
    random.shuffle(letras) #mezclamos con el shuffle random

    matriz = [] #guardamos en una nueva lista vacía
    for i in range(cant_colum_filas):
        fila = letras[i*cant_colum_filas: (i+1)* cant_colum_filas]
        matriz.append(fila)
    return matriz


# ----- funciones para mejorar la estética ----- #

#mostramos el estado actual del rompecabezs matricialmente
def mostrar_matriz(matriz):
    """Muestra la matriz del rompecabezas en pantalla."""
    for fila in matriz:
        print('|'.join(fila)) #une los elementos de cada fila con | para uqe se vea bonito
    print() #salto de linea

#funcion que nos permite mover las fichas
def encontrar_espacio(matriz):
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == '-':
                return i, j
    return None

def mover(matriz, direccion):
    """Mueve el espacio vacío ('-') en la dirección dada si es válido."""
    movimientos = {
        'w': (-1, 0),  # subir
        's': (1, 0),   # bajar
        'a': (0, -1),  # izquierda
        'd': (0, 1)    # derecha
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


# ---------- PRUEBAS BÁSICAS ----------

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

# ---------- JUEGO PRINCIPAL ----------

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

# ---------- EJECUCIÓN ----------

if __name__ == "__main__":
    pruebas_movimientos()  # Descomentar para correr las pruebas
    jugar_rompecabezas()
#docstring
