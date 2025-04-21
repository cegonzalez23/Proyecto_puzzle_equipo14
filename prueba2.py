
import random


#Ingresar parámetros#
configuracion_inicial = []

cant_colum_filas= int(input("Ingresar cantidad de columnas/filas el rompecabezas, hasta 5: "))

if cant_colum_filas > 5:
    print ("No es posible esa configuración. Se establece configuración preterminada:")
    cant_colum_filas= 3


letras = []
carga_de_valores = ord('a') 

for pos in range(cant_colum_filas * cant_colum_filas-1): 
    letras.append (chr(carga_de_valores))
    carga_de_valores += 1 

letras.append('-')
random.shuffle(letras) ##MODIFICACION1

#import random
#random.shuffle(letras)


pos_matriz= 0 
for i in range (cant_colum_filas):
    fila= []
    for j in range (cant_colum_filas):
        fila.append(letras[pos_matriz])
        pos_matriz += 1
    configuracion_inicial.append(fila)


def mostrar_matriz(matriz):
    for fila in matriz:
        print(' | '.join(fila))
    print()



def encontrar_espacio_usado (matriz): 
    for i in range (len(matriz)): 
        for j in range (len(matriz[i])): 
            if matriz[i] [j]== '-':
                return i,j
    return None 

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
    
    if 0 <= nueva_fila < cant_colum_filas and 0 <= nueva_columna < cant_colum_filas:
        matriz[fila][columna], matriz[nueva_fila][nueva_columna] = matriz[nueva_fila][nueva_columna], matriz[fila][columna]
        return True
    else:
        print("Movimiento fuera de los límites")
        return False

#MODIFICACION2
def pedir_direccion():
    while True:
        direccion = input("Mover (w=arriba, s=abajo, a=izquierda, d=derecha): ").lower()
        if direccion in ['w', 'a', 's', 'd']:
            return direccion
        else:
            print("Entrada inválida. Usá solo 'w', 'a', 's' o 'd'.")

def rompecabezas_resuelto(matriz):
    orden_correcto = [chr(ord('a') + i) for i in range(cant_colum_filas * cant_colum_filas - 1)]
    orden_correcto.append('-')
    plano = [pieza for fila in matriz for pieza in fila]
    return plano == orden_correcto

#while True:
 #   mostrar_matriz(configuracion_inicial)
 #  direccion = input("Mover (w=arriba, s=abajo, a=izquierda, d=derecha): ")
 # mover(configuracion_inicial, direccion)



#MODIFICACION3
while True:
    mostrar_matriz(configuracion_inicial)
    if rompecabezas_resuelto(configuracion_inicial):
        print("¡Felicidades! Resolviste el rompecabezas.")
        break
    direccion = pedir_direccion()
    mover(configuracion_inicial, direccion)

#Agregar validaciones




