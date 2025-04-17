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
