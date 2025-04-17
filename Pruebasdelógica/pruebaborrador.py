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
