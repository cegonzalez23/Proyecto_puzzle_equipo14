#ROMPECABEZAS. Integrantes: Egochine Dana, Pasman Micaela, Gonzalez Celeste#

#Ingresar parámetros#
configuracion_inicial = []

cant_colum_filas= int(input("Ingresar cantidad de columnas/filas el rompecabezas, hasta 5: "))

if cant_colum_filas > 5:
    print ("No es posible esa configuración. Se establece configuración preterminada:")
    cant_colum_filas= 3

# Crear lista de letras. Inicialmente probamos el rompecabezas con letras
letras = []
carga_de_valores = ord('a') #empiezo con a = 97

for pos in range(cant_colum_filas * cant_colum_filas-1): #Espacio total -1
    letras.append (chr(carga_de_valores))
    carga_de_valores += 1 # a + 1= b; b + 1= c, sucesivamente...

letras.append('-') #Es el espacio usado, el ultimo

#Desordenar letras con ramdom. Después mejoramos eso
import random
random.shuffle(letras)

# Cargar matriz:
pos_matriz= 0 #recorre la lista letras luego de que esté mezclado
for i in range (cant_colum_filas):
    fila= []
    for j in range (cant_colum_filas):
        fila.append(letras[pos_matriz])
        pos_matriz += 1
    configuracion_inicial.append(fila)

# Función para mostrar el rompecabezas.
def mostrar_matriz(matriz):
    for fila in matriz:
        print(' | '.join(fila))
    print()

'''#Visualización de la configuración#
print("\nConfiguración inicial del rompecabezas:")
for fila in configuracion_inicial:
    print(' | '.join(fila)) #string '''

#Función para encontrar el "-":
def encontrar_espacio_usado (matriz): #matriz es configuracion_inicial
    for i in range (len(matriz)):  #reccore las filas
        for j in range (len(matriz[i])): #reccore las columnas
            if matriz[i] [j]== '-':
                return i,j
    return None #Si no encuentra nada

def mover(matriz, direccion):
    fila, columna = encontrar_espacio_usado(matriz)
    nueva_fila = fila
    nueva_columna = columna

    if direccion == 'w':
        nueva_fila = fila - 1
    elif direccion == 's':
        nueva_fila = fila + 1
    elif direccion == 'a':
        nueva_columna = columna - 1
    elif direccion == 'd':
        nueva_columna = columna + 1
    else:
        print("Dirección inválida")
        return False

#Asegurar limites de la matriz:
    if 0 <= nueva_fila < cant_colum_filas and 0 <= nueva_columna < cant_colum_filas:
        matriz[fila][columna], matriz[nueva_fila][nueva_columna] = matriz[nueva_fila][nueva_columna], matriz[fila][columna]
        return True
    else:
        print("Movimiento fuera de los límites")
        return False

while True:
    mostrar_matriz(configuracion_inicial)
    direccion = input("Mover (w=arriba, s=abajo, a=izquierda, d=derecha): ")
    mover(configuracion_inicial, direccion)

#Agregar validaciones
